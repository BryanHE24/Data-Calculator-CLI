# Here we implement mathematical functions

from typing import List
import math

# Function to calculate the mean 
def calculate_mean(data: List[float]) -> float:
    """Arithmetic mean."""
    if not data:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(data) / len(data) # Return the mean value

# Function to calculate the median
def calculate_median(data: List[float]) -> float:
    """Middle value of sorted list."""
    if not data:
        raise ValueError("Cannot calculate median of empty list")
    sorted_data = sorted(data) # Sort the data
    n = len(sorted_data) 
    mid = n // 2 #
    # If odd, return middle element; if even, return lower middle element
    if n % 2 == 1:
        return sorted_data[mid]
    return sorted_data[mid - 1] + sorted_data[mid] / 2

# Function to calculate the variance
def calculate_variance(data: List[float]) -> float:
    """Measure of data spread."""
    if not data:
        raise ValueError("Cannot calculate variance of empty list")
    # this part handles the case where there's only one element
    if len(data) < 2:
        return 0.0 # Variance of single element list is 0
    mean = calculate_mean(data) # Calculate the mean
    return sum((x - mean) ** 2 for x in data) / len(data) # Return variance value

# Function to calculate the standard deviation
def calculate_std_dev(data: List[float]) -> float:
    return math.sqrt(calculate_variance(data)) # Standard deviation is the square root of variance