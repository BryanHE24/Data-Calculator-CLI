import numpy as np
from typing import List

# ==========================================
# MODULE: Matrix Operations
# RESPONSIBILITY: Linear Algebra logic using NumPy.
# RULE: Inputs are standard Python lists, internal logic uses NumPy arrays.
# ==========================================

# Type Alias: A Matrix is a list of lists of floats.
# Example: [[1.0, 2.0], [3.0, 4.0]] represents a 2x2 matrix.
Matrix = List[List[float]]

def get_transpose(matrix: Matrix) -> Matrix:
    """
    Calculates the transpose of a matrix.
    Transpose means flipping the matrix over its diagonal (rows become columns).
    
    Args:
        matrix (Matrix): A list of lists representing the matrix.
        
    Returns:
        Matrix: The transposed matrix as a standard Python list.
    """
    if not matrix:
        raise ValueError("Cannot transpose an empty matrix.")
    
    # 1. Convert standard Python list to NumPy array for performance
    # NumPy arrays are much faster for math operations than Python lists.
    np_matrix = np.array(matrix)
    
    # 2. Perform Transpose
    # .T is a NumPy property that returns the transposed view of the array.
    transposed = np_matrix.T
    
    # 3. Convert back to Python List
    # We return a standard list to keep our "Pure Function" contract
    # and not force the rest of the app to deal with NumPy objects.
    return transposed.tolist()

def get_dot_product(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """
    Calculates the Dot Product (Matrix Multiplication) of two matrices.
    
    Rule: For A x B, the number of columns in A must equal the number of rows in B.
    
    Args:
        matrix_a (Matrix): The first matrix.
        matrix_b (Matrix): The second matrix.
        
    Returns:
        Matrix: The resulting matrix product.
    """
    if not matrix_a or not matrix_b:
        raise ValueError("Cannot perform dot product of empty matrices.")
    
    # Convert inputs to NumPy arrays
    a = np.array(matrix_a)
    b = np.array(matrix_b)
    
    try: 
        # np.dot(a, b) performs standard matrix multiplication.
        # It automatically sums the products of rows and columns.
        result = np.dot(a, b)
        
        # Convert result back to a standard list
        return result.tolist()
        
    except ValueError as e:
        # NumPy raises a ValueError if shapes are incompatible (e.g., 2x2 vs 3x2).
        # We catch it and raise a more descriptive error for our user.
        raise ValueError(f"Shape mismatch for dot product: {a.shape} vs {b.shape}. Columns of A must match rows of B.")