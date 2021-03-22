import click
import json
from .githubutil import GithubUtil
from .fileutil import FileUtil

gh = GithubUtil()
fu = FileUtil()

@click.command()
@click.argument('name', type=click.Path())
@click.option('--dry-run', is_flag=True)
@click.option('--template-file', default='templates.json', help='Name of template json file')
@click.option('--template', default='basic', help='Name of template to use')
def cli(name, dry_run, template_file, template):
    """Create new project from template"""
    
    ## Do some checks to see if this is something swe should try

    if fu.checkPath(name)==True:
        click.echo("Path already exits!")
        return 0
    
    user_data = gh.getRepoData()
    
    if "errors" in user_data:
        click.echo(f'Error in github connection:\n {json.dumps(user_data, indent=2, sort_keys=True)}')
        return 0
    else:
        last_repo = user_data[-1]
        click.echo(f"Authenticated user: {last_repo['owner']['login']}")

    templates = fu.read_templates(template_file)
    try:
        template_repo = templates[template]
    except KeyError:
        print("Key error: specified template does not exits")
        return 0

    click.echo(f'Cloning repo: {template_repo} \nInto directory: {name}/ ')
    
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
        out = ["dry-run-remote-out"]
    else:
        out = gh.changeRemote(name, clone_url)
    
    for o in out:
        click.echo(f"Change remote out: {o} \n")
    
    click.echo("Opening project . . .")

    if dry_run:
        out = "dry-run-open-code"
    else:
        out = fu.openWithCode(name)

    click.echo(f"Code open out: {out}")