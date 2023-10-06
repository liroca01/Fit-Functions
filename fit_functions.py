import scipy as scp
import numpy as np
import pandas as pd
import glob
import os

def my_line(x,a,b):
    return a + b*x

def fit_timeseries(tlist,yliglogst):
    m,mcov = scp.optimize.curve_fit(my_line,tlist,yliglogst,p0=[0,0])
    return m[0], np.sqrt(mcov[0, 0])


def fit_velocities(filename):
    timeseries = pd.read_csv(filename, delim_whitespace = True)
    #print(timeseries.columns)
    
    E = timeseries["__east(m)"]
    N = timeseries["_north(m)"]
    U = timeseries["____up(m)"]
    
    E_v, E_uv = fit_timeseries(timeseries['yyyy.yyyy'],E)
    N_v, N_uv = fit_timeseries(timeseries['yyyy.yyyy'],N)
    U_v, U_uv = fit_timeseries(timeseries['yyyy.yyyy'],U)

    
    return [E_v, N_v,  U_v], [E_uv, N_uv, U_uv] 
    

def get_coordinates(filename):
    timeseries = pd.read_csv(filename, delim_whitespace = True)
    return [timeseries[i].mean() for i in ["_latitude(deg)" ,"_longitude(deg)","__height(m)"]]

def fit_tide_gauge(filename):
    timeseries = pd.read_csv(filename, header = None, delimiter = ";")
    velocity, _ = fit_timeseries(timeseries[0], timeseries[1])
    return velocity

def fit_all_velocities(folder, pattern, type):
    results = []
    file_list = glob.glob(folder + pattern)
    if type == "GNSS":
        for file_path in file_list:
            site_name, _ = os.path.splitext(os.path.basename(file_path))
            velocities, uncertainties = fit_velocities(file_path)
            avg_latitude, avg_longitude, avg_elevation = get_coordinates(file_path)
            results.append([site_name, avg_latitude, avg_longitude, avg_elevation, velocities[0], velocities[1], velocities[2], uncertainties[0],uncertainties[1],uncertainties[2]])
    
        df = pd.DataFrame(results, columns=['Site', 'Latitude', 'Longitude', 'Elevation', 'Velocity_E','Velocity_N' ,'Velocity_U', 'Uncertainty_E','Uncertainty_N','Uncertainty_U'])
    elif type == "tide":
        for file_path in file_list:
            site_name, _ = os.path.splitext(os.path.basename(file_path))
            velocity = fit_tide_gauge(file_path)
            results.append([site_name, velocity])
        df = pd.DataFrame(results, columns =['Filename','Velocity'])
        
    return df