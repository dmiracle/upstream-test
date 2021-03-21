# Project starter
Command line utility for starting projects from boilerplate repos. Something like this almost certainly already exists, idgaf.

Imagine that it is invoked something like this 
```
projectr create --base=github.com/dmiracle/boiler-plate --name new-project 
```

## Current Invocation
```
projectr my-project-name --template basic --template-file templates.json
```
Defaults are set for the options

## Install
```
. venv/bin/activate
pip install -e .
```

## Steps
1. create git repo
    - gitignore
1. download boilerplate
1. create and push remote

## Environmental Vars
Projectr uses `python-decouple` to deal with authentication tokens. Add `.env` to `.gitignore`. Make a `.env` file and add your tokens.
```
GITHUB_TOKEN=<token>
AWS_KEY_ID=<>
AWS_SECRET_KEY=<>
```

## To do

- check for `project-path` and if it exists bail
- check for existing repo and if it exits bail
- add entry to `templates.json` from cli
- dry-run mode

