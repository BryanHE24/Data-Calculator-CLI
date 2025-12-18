import pytest
from calculator.stats import (
    calculate_mean, 
    calculate_median, 
    calculate_mode, 
    normalize_min_max
)

# ==========================================
# TEST GROUP 1: Basic Descriptive Statistics
# ==========================================

def test_calculate_mean():
    # SCENARIO: A standard list of positive integers.
    # We use simple numbers [1, 2, 3, 4, 5] so the math is obvious.
    data = [1, 2, 3, 4, 5]
    
    # ACTION: Call the function
    result = calculate_mean(data)
    
    # ASSERTION: The sum is 15, count is 5. 15 / 5 = 3.0.
    # We verify exact equality because these are clean integers.
    assert result == 3.0

def test_calculate_median_odd():
    # SCENARIO: A list with an ODD number of elements.
    # The median should be the exact middle element.
    data = [1, 3, 5]
    
    # ASSERTION: Middle element is 5.
    assert calculate_median(data) == 3

def test_calculate_median_even():
    # SCENARIO: A list with an EVEN number of elements.
    # The median should be the average of the two middle elements (2 and 3).
    data = [1, 2, 3, 4]
    
    # ASSERTION: (2 + 3) / 2 = 2.5
    assert calculate_median(data) == 2.5

def test_calculate_mode_single():
    # SCENARIO: A list where one number appears more than others.
    data = [1, 2, 2, 3]
    
    # ASSERTION: The number 2 is the clear winner.
    # The function returns a list, so we check against [2].
    assert calculate_mode(data) == [2]

def test_calculate_mode_tie():
    # SCENARIO: A "bimodal" dataset (two numbers tie for first place).
    data = [1, 1, 2, 2, 3]
    
    # ACTION: Get the mode(s)
    result = calculate_mode(data)
    
    # ASSERTION: Both 1 and 2 should be returned.
    # We sort the result to ensure the list order doesn't fail the test.
    assert sorted(result) == [1, 2]

# ==========================================
# TEST GROUP 2: Error Handling (Edge Cases)
# ==========================================

def test_stats_empty_input():
    # SCENARIO: The user provides an empty list to the mean function.
    # This represents a common data error (e.g., empty CSV file).
    empty_data = []

    # ASSERTION: The code must NOT crash with a "DivisionByZero" error.
    # It must raise a specific ValueError that we can catch nicely later.
    with pytest.raises(ValueError):
        calculate_mean(empty_data)

# ==========================================
# TEST GROUP 3: Data Normalization
# ==========================================

def test_normalize_min_max():
    # SCENARIO: A simple range from 0 to 10.
    # We want to scale these numbers to fit exactly between 0.0 and 1.0.
    data = [0, 5, 10]
    
    # ACTION: Apply Min-Max normalization
    result = normalize_min_max(data)
    
    # ASSERTION:
    # 0 is the min, so it becomes 0.0
    # 5 is exactly halfway, so it becomes 0.5
    # 10 is the max, so it becomes 1.0
    assert result == [0.0, 0.5, 1.0]