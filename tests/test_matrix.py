import pytest
import numpy as np
from calculator.matrix import get_transpose, get_dot_product

# ==========================================
# TEST GROUP 1: Matrix Transformation
# ==========================================

def test_get_transpose():
    # SCENARIO: A 2x3 matrix (2 rows, 3 columns).
    # We want to flip it over its diagonal.
    matrix = [
        [1, 2, 3], 
        [4, 5, 6]
    ]
    
    # EXPECTED RESULT: A 3x2 matrix (3 rows, 2 columns).
    # Row 1 [1,2,3] becomes Column 1.
    expected = [
        [1, 4], 
        [2, 5], 
        [3, 6]
    ]
    
    # ASSERTION: Check if the function returns the expected list structure.
    assert get_transpose(matrix) == expected

# ==========================================
# TEST GROUP 2: Matrix Multiplication
# ==========================================

def test_get_dot_product():
    # SCENARIO: Multiplying a matrix by the Identity Matrix.
    # Concept: Any matrix multiplied by Identity must remain unchanged.
    matrix_a = [[1, 2], [3, 4]]
    
    # Identity Matrix: 1s on diagonal, 0s elsewhere.
    identity = [[1, 0], [0, 1]]
    
    # ACTION: Calculate Dot Product
    result = get_dot_product(matrix_a, identity)
    
    # ASSERTION: The result should be identical to the original matrix_a.
    assert result == [[1, 2], [3, 4]]

def test_dot_product_mismatch():
    # SCENARIO: Incompatible Matrix Shapes.
    # Matrix A is 2x2. Matrix B is 3x2.
    # Rule: Dot product requires Cols(A) == Rows(B). 
    # Here: 2 != 3, so it's mathematically impossible.
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[1, 2], [3, 4], [5, 6]]
    
    # ASSERTION: The function must protect us by raising a ValueError.
    with pytest.raises(ValueError):
        get_dot_product(matrix_a, matrix_b)