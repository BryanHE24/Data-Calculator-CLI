import pandas as pd
import click
from typing import List

def load_data(filepath: str, column: str = None) -> List[float]:
    """
    Loads numerical data from a CSV file.
    Returns a clean list of floats for the math engine.
    """
    try:
        # Attempt to read the CSV file
        df = pd.read_csv(filepath)

        # Scenario A: The CSV has only one column of numbers.
        if len(df.columns) == 1:
            # Select the first column, convert to float, then to list
            return df.iloc[:, 0].astype(float).tolist()

        # Scenario B: The CSV has multiple columns.
        if column:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found. Available: {list(df.columns)}")
            return df[column].astype(float).tolist()

        # Scenario C: Ambiguity (Multi-column but user didn't choose one)
        raise ValueError("File has multiple columns. Please specify which one to use.")

    except FileNotFoundError:
        # We use click.BadParameter to show a nice error in the CLI
        raise click.BadParameter(f"File does not exist: {filepath}")
    except ValueError as e:
        raise click.BadParameter(str(e))
    except Exception as e:
        raise click.BadParameter(f"Unexpected error: {str(e)}")