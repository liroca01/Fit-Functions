# Fit_functions.py

This module provides a collection of functions for fitting and analyzing time series data from various sources, including GNSS data and tide gauge data. It includes functions for fitting linear models, estimating velocities, extracting coordinates, and more.

## Functions

### `fit_timeseries(tlist, yliglogst)`

This function fits a linear model to a time series and returns the least-squares velocity and uncertainty.

### `fit_velocities(filename)`

This function reads time series data from a CSV file, estimates the East, North, and Up components of velocity, and returns the results along with uncertainties.

### `get_coordinates(filename)`

This function extracts the average latitude, longitude, and elevation from a CSV file containing coordinate data.

### `fit_tide_gauge(filename)`

This function fits a tide gauge data file and returns the velocity.

### `fit_all_velocities(folder, pattern, type)`

This function processes multiple data files in a specified folder based on a given pattern and type (e.g., GNSS or tide gauge). It calculates velocities, uncertainties, and coordinates for GNSS data or velocities for tide gauge data and returns the results in a DataFrame.

## Usage

You can import this module and use the provided functions in your Python scripts or notebooks for analyzing and processing time series data.

```python
import fit_functions

# Example usage
velocities = fit_functions.fit_velocities('data.csv')
print(velocities)

```

## Requirements

- Python 3.x
- NumPy
- SciPy
- Pandas


