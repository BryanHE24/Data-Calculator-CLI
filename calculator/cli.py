import click
import ast # Abstract Syntax Tree: Used to safely parse string inputs like "[[1,2]]"
from calculator.utils import load_data

# Import Logic Modules
from calculator.matrix import get_transpose, get_dot_product
from calculator.stats import ( 
    calculate_mean, 
    calculate_median, 
    calculate_mode,
    calculate_std_dev, 
    calculate_variance,
    normalize_min_max, 
    normalize_z_score
)

# ==========================================
# MODULE: CLI Entry Point
# RESPONSIBILITY: Parse User Input -> Call Logic -> Print Output
# FRAMEWORK: Click (Decorators define commands)
# ==========================================

@click.group()
def main():
    """
    Data Calculator CLI
    
    A tool for performing statistical and matrix operations on data.
    """
    # The main group doesn't do work; it holds the sub-commands.
    pass

# --- Basic Commands ---

@main.command()
def verify():
    """Simple command to check if CLI is installed and working."""
    click.echo("✅ CLI entry point is functional!")

# --- Statistics Commands ---

@main.command()
# Define arguments: --file is required, --column is optional
@click.option("--file", required=True, type=click.Path(exists=True), help="Path to CSV file.")
@click.option("--column", default=None, help="Column name to analyze (if multi-column).")
def stats(file, column):
    """
    Calculate descriptive statistics (Mean, Median, Mode, etc.).
    """
    try:
        # STEP 1: Load Data
        data = load_data(file, column)

        # STEP 2: Calculate Metrics (Pure Logic)
        mean_val = calculate_mean(data)
        median_val = calculate_median(data)
        mode_val = calculate_mode(data)
        std_dev = calculate_std_dev(data)
        variance = calculate_variance(data)

        # STEP 3: Display Results
        click.echo(f"📊 Statistics for {file}:")
        click.echo(f"--------------------------")
        click.echo(f"Mean:      {mean_val:.4f}")
        click.echo(f"Median:    {median_val:.4f}")
        click.echo(f"Mode:      {mode_val}")
        click.echo(f"Std Dev:   {std_dev:.4f}")
        click.echo(f"Variance:  {variance:.4f}")

    except Exception as e:
        # If anything goes wrong, print it in RED
        click.secho(f"Error: {str(e)}", fg="red")

# --- Normalization Commands (Phase 6) ---

@main.command()
@click.option("--file", required=True, type=click.Path(exists=True), help="Path to CSV file.")
@click.option("--column", default=None, help="Column name to normalize.")
@click.option("--type", "method", type=click.Choice(['min-max', 'z-score']), default='min-max', help="Method: min-max or z-score.")
def normalize(file, column, method):
    """
    Normalize a data column for AI training.
    """
    try:
        # 1. Load Data
        data = load_data(file, column)
        
        # 2. Apply Normalization Strategy
        if method == 'min-max':
            result = normalize_min_max(data)
            click.echo(f"📉 Min-Max Normalized Data ({file}):")
        else:
            result = normalize_z_score(data)
            click.echo(f"📉 Z-Score Normalized Data ({file}):")
        
        # 3. Print a preview (first 10 items) to keep terminal clean
        click.echo(f"Preview (First 10): {result[:10]}")
        
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red")

# --- Matrix Commands (Phase 5) ---

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

if __name__ == "__main__":
    main()