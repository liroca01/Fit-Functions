import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

from fit_all_velocities import *

def plot_velocities(df):
    latitudes = df['latitude'].values
    longitudes = df['longitude'].values
    east_velocities = np.array([item[0] for item in df['east component velocity'].values])
    north_velocities = np.array([item[0] for item in df['north component velocity'].values])
    up_component = np.array([item[0] for item in df['up component velocity'].values])
    
    # Create a map-like figure
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim([-110, -100])
    ax.set_ylim([30, 40])
    
    # Plotting using quiver for east and north velocities
    scale_factor = 1e10 
    Q = ax.quiver(longitudes, latitudes, east_velocities, north_velocities, up_component, scale_units='xy', scale=0.005, width=0.005, headwidth=5, headlength=6, headaxislength=5, cmap='coolwarm')
    
    cbar = fig.colorbar(Q, ax=ax)
    cbar.set_label('Up Component Velocity')
    # Plotting using scatter for up component velocities and color coding
   # scatter = ax.scatter(longitudes, latitudes, c=up_component, cmap='RdBu')
   # plt.colorbar(scatter, ax=ax, label="Up Component Velocity")
    
    # Setting title and labels
    ax.set_title("Velocities Plot")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    plt.show()
    
    