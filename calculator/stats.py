from typing import List
import math

# ==========================================
# MODULE: Statistics Logic
# RESPONSIBILITY: Pure mathematical functions.
# ==========================================

# --- Descriptive Statistics ---

def calculate_mean(data: List[float]) -> float:
    """Calculates the arithmetic mean (average)."""
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(data) / len(data)

def calculate_median(data: List[float]) -> float:
    """Calculates the median (middle value)."""
    if not data:
        raise ValueError("Cannot calculate median of an empty list.")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

def calculate_mode(data: List[float]) -> List[float]:
    """Calculates the mode (most frequent value)."""
    if not data:
        raise ValueError("Cannot calculate mode of an empty list.")
    
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    
    max_count = max(frequency.values())
    return [k for k, v in frequency.items() if v == max_count]

def calculate_variance(data: List[float]) -> float:
    """Calculates the Population Variance."""
    if not data:
        raise ValueError("Cannot calculate variance of an empty list.")
    if len(data) < 2:
         return 0.0
         
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std_dev(data: List[float]) -> float:
    """Calculates the Population Standard Deviation."""
    return math.sqrt(calculate_variance(data))

# --- Data Normalization (New for Phase 6) ---

def normalize_min_max(data: List[float]) -> List[float]:
    """
    Scales data to the range [0, 1].
    Formula: (x - min) / (max - min)
    """
    if not data:
        raise ValueError("Cannot normalize an empty list.")
    
    min_val = min(data)
    max_val = max(data)
    
    # Avoid division by zero if all numbers are identical
    if min_val == max_val:
        return [0.0] * len(data)
        
    return [(x - min_val) / (max_val - min_val) for x in data]

def normalize_z_score(data: List[float]) -> List[float]:
    """
    Scales data using Z-Score (Standard Score).
    Formula: (x - mean) / std_dev
    """
    if not data:
        raise ValueError("Cannot normalize an empty list.")
    
    if len(data) < 2:
        return [0.0] * len(data)

    mean = calculate_mean(data)
    std_dev = calculate_std_dev(data)
    
    # Avoid division by zero
    if std_dev == 0:
        return [0.0] * len(data)
        
    return [(x - mean) / std_dev for x in data]