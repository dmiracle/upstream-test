import click
import json
from .githubutil import GithubUtil

gh = GithubUtil()
def read_templates(fname="templates.json"):
    print("reading templates")
    with open(fname) as json_file:
        return json.load(json_file)

test_dict = {'a':'thing 1', 'b':'thing 2'}
@click.command()
def cli():
    """Example script."""
    aa = json.dumps(read_templates())
    click.echo(f'Templates: \n{aa}')
