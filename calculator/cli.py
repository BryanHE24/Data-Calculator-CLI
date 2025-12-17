import click

@click.group() # Defines the main command group for the CLI
def main():
    """
    Data Calculator CLI
    A tool for performing statistical and matrix operations on data.
    """
    pass
@main.command() # Subcommand to check installation
def verify():
    """
    Verify the installation of the Data Calculator package.
    """
    click.echo("Data Calculator package is installed correctly.")

if __name__ == "__main__":
    main()
