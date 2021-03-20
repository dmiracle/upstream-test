import click
import githubutil as gh
import fileutil as fu

@click.command()
def cli():
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Ah snap')
