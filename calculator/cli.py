import click
from calculator.utils import load_data
# Import statistical functions
from calculator.stats import ( 
    calculate_mean, 
    calculate_median, 
    calculate_mode,
    calculate_std_dev, 
    calculate_variance
)
# Define CLI using Click
@click.group()
def main():
    """Data Calculator CLI: Perform stats on CSV files."""
    pass

# Simple verification command
@main.command()
def verify():
    """Simple command to check if CLI is working."""
    click.echo("✅ CLI entry point is functional!")

# Statistics command
@main.command()
@click.option("--file", required=True, type=click.Path(exists=True), help="Path to CSV file.")
@click.option("--column", default=None, help="Column name to analyze (if multi-column).")
def stats(file, column):
    """Calculate descriptive statistics for a dataset."""
    try:
        # 1. Load Data (The Hands)
        data = load_data(file, column)

        # 2. Perform Math (The Brain)
        mean_val = calculate_mean(data)
        median_val = calculate_median(data)
        mode_val = calculate_mode(data)
        std_dev = calculate_std_dev(data)
        variance = calculate_variance(data)

        # 3. Report Results (The Face)
        click.echo(f"📊 Statistics for {file}:")
        click.echo(f"--------------------------")
        click.echo(f"Mean:      {mean_val:.4f}")
        click.echo(f"Median:    {median_val:.4f}")
        click.echo(f"Mode:      {mode_val}")
        click.echo(f"Std Dev:   {std_dev:.4f}")
        click.echo(f"Variance:  {variance:.4f}")
    # Handle exceptions
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red")

if __name__ == "__main__":
    main()