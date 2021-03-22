import click
import json
from .githubutil import GithubUtil
from .fileutil import FileUtil

gh = GithubUtil()
fu = FileUtil()

def read_templates(fname):
    print("reading templates")
    with open(fname) as json_file:
        return json.load(json_file)

@click.command()
@click.argument('name', type=click.Path())
@click.option('--dry-run', type=click.BOOL, default=False)
@click.option('--template-file', default='templates.json', help='Name of template json file')
@click.option('--template', default='basic', help='Name of template to use')
def cli(name, dry_run, template_file, template):
    """Create new project from template"""
    
    if fu.checkPath(name)==True:
        click.echo("Path already exits!")
        return 0

    templates = read_templates(template_file)
    try:
        template_repo = templates[template]
    except KeyError:
        print("Key error: specified template does not exits")
        return
    except Exception as e:
        print(f"Error: {type(e)}")
        return

    click.echo(f'Cloning repo: {template_repo} \nInto directory: {name} . . .')
    
    if dry_run:
        clone_out = "dry-run-clone-out" 
    else:
        clone_out = gh.cloneRepo(template_repo, name)

    click.echo(f'Clone result: {clone_out}')

    click.echo(f'Creating repo: {name} . . .')

    if dry_run:
        clone_url = "dry-run-clone-url" 
    else:
        res = gh.createRepo(name)
        if "errors" in res:
            click.echo(f'Error response {json.dumps(res, indent=2, sort_keys=True)}')
            return 0
        else:
            clone_url = res['clone_url']
    
    click.echo(f'Create repo respose: {clone_url}')

    click.echo("Update remote . . .")
    
    if dry_run:
        out = "dry-run-remote-out"
    else:
        out = gh.changeRemote(name, clone_url)
    
    for o in out:
        click.echo(f"Change remote out: {json.dumps(o, indent=2, sort_keys=True)} \n\n")
    
    click.echo("Opening project . . .")

    if dry_run:
        out = "dry-run-open-code"
    else:
        out = fu.openWithCode(name)

    click.echo(f"Code open out: {out}")