import click
import json
from .githubutil import GithubUtil
from .fileutil import FileUtil



@click.command()
@click.argument('name', type=click.Path())
@click.option('-d', '--dry-run', is_flag=True)
@click.option('-o', '--open-with-code', is_flag=True)
@click.option('-v', '--verbose', is_flag=True)
@click.option('--template-file', default='templates.json', help='Name of template json file')
@click.option('-t', '--template', default='basic', help='Name of template to use')
def cli(name, dry_run, open_with_code, verbose,  template_file, template):
    """Create new project from template"""
    gh = GithubUtil(dry_run)
    fu = FileUtil()
    way_point = []
    success = True
    ## Preflight checks

    if fu.checkPath(name)==True:
        click.echo("Path already exits!")
        return 0
    
    res = gh.getRepoData()
    click.echo(res['message'])
    if verbose:
        click.echo(f"{res['data']}")

    templates = fu.read_templates(template_file)
    try:
        template_repo = templates[template]
    except KeyError:
        print("Key error: specified template does not exits")
        return 0

   
    ###################
    click.echo(f'Cloning {template_repo} into directory {name}/ . . .')

    res = gh.cloneRepo(template_repo, name)
    click.echo(res['message'])
    if verbose:
        click.echo(f"{res['data']}") 

    way_point.append('clone')



    ###################
    click.echo(f'Creating new remote: {name} . . .')

    res = gh.createRepo(name)
    click.echo(res['message'])
    if verbose:
        click.echo(f"Create repo response {json.dumps(res['data'], indent=2, sort_keys=True)}")
    clone_url = res['data']['clone_url']
    click.echo("Attach new remote to local template . . .")
    
    res = gh.changeRemote(name, clone_url)
    if verbose:
        for o in out:
            click.echo(f"Change remote out: {o} \n")
    

    if open_with_code:
        click.echo("Opening project . . .")
        if dry_run:
            out = "dry-run-open-code"
        else:
            out = fu.openWithCode(name)

    if verbose:
        click.echo(f"Code open out: {out}")

    click.echo("Done.")