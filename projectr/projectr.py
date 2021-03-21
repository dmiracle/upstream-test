import click
import json
from .githubutil import GithubUtil

gh = GithubUtil()
def read_templates(fname):
    print("reading templates")
    with open(fname) as json_file:
        return json.load(json_file)

@click.command()
@click.argument('name', type=click.Path())
@click.option('--template-file', default='templates.json', help='Name of template json file')
@click.option('--template', default='basic', help='Name of template to use')
def cli(name, template_file, template):
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

    try:
        click.echo(f'Cloning repo: {template_repo} \nInto directory: {name}')
        gh.cloneRepo(template_repo, name)
    except:
        print(f"Error: {type(e)}")
        return

    click.echo(f'Creating repo: {name}')
    res = gh.createRepo(name)
    clone_url = res['clone_url']
    click.echo(f'Respose: {clone_url}')

    out = gh.changeRemote(name, clone_url)
    print(out)
    gh.openWithCode(project_path)