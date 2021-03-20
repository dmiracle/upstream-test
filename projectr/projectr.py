import click
import json
from .githubutil import GithubUtil

gh = GithubUtil()
def read_templates(fname):
    print("reading templates")
    with open(fname) as json_file:
        return json.load(json_file)

@click.command()
@click.argument('dir', type=click.Path())
@click.option('--template-file', default='templates.json', help='Name of template json file')
@click.option('--template', default='basic', help='Name of template to use')
def cli(dir, template_file, template):
    """Create new project from template"""
    templates = read_templates(template_file)
    try:
        template_repo = templates[template]
    except KeyError:
        print("Key error: specified template does not exits")
        return
    except Exception as e:
        print(f"Error: {type(e)}")
        return
    click.echo(f'repo: {template_repo} \ndir: {dir}')
