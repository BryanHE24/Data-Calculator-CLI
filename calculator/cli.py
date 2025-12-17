import ast  # Abstract Syntax Tree: Used to safely parse string inputs into Python objects
import click
from calculator.matrix import get_transpose, get_dot_product

# ... (Keep your stats imports and commands above) ...

# ==========================================
# COMMAND GROUP: Matrix Operations
# ==========================================

@main.group()
def matrix():
    """
    Perform matrix operations (linear algebra).
    Uses NumPy for efficient calculation.
    """
    # This acts as a container for 'transpose' and 'dot' subcommands.
    pass

@matrix.command()
@click.argument("matrix_str")
def transpose(matrix_str):
    """
    Transpose a matrix (rows -> columns).
    
    ARGUMENT:
        matrix_str: A string representation of a list of lists.
        Example: "[[1, 2], [3, 4]]"
    """
    try:
        # 1. Parse String to List
        # ast.literal_eval is safer than eval() because it only processes
        # data structures (lists, numbers), not code execution.
        matrix_data = ast.literal_eval(matrix_str)
        
        # 2. Call Logic
        result = get_transpose(matrix_data)
        
        # 3. Output
        click.echo("🔄 Transposed Matrix:")
        for row in result:
            click.echo(row)
            
    except Exception as e:
        click.secho(f"Error processing matrix: {e}", fg="red")

@matrix.command()
@click.argument("matrix_a_str")
@click.argument("matrix_b_str")
def dot(matrix_a_str, matrix_b_str):
    """
    Calculate the Dot Product of two matrices.
    
    ARGUMENTS:
        matrix_a_str: First matrix string (e.g., "[[1, 2]]")
        matrix_b_str: Second matrix string (e.g., "[[1], [2]]")
    """
    try:
        # 1. Parse Strings to Lists
        matrix_a = ast.literal_eval(matrix_a_str)
        matrix_b = ast.literal_eval(matrix_b_str)
        
        # 2. Call Logic
        result = get_dot_product(matrix_a, matrix_b)
        
        # 3. Output
        click.echo("❌ Dot Product Result:")
        for row in result:
            click.echo(row)
            
    except Exception as e:
        click.secho(f"Error calculating dot product: {e}", fg="red")