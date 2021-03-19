# Project starter
Command line utility for starting projects from boilerplate repos. Something like this almost certainly already exists, idgaf.

Imagine that it is invoked something like this 
```
projectr create --base=github.com/dmiracl/boiler-plate --name new-project 
```

## Steps
1. create git repo
    - gitignore
1. download boilerplate
1. create and push remote

## Variables
1. repo-name
1. description
1. 

## Environmental Vars
Make a `.env` file. Add your tokens
```
GITHUB_TOKEN=<token>
AWS_KEY_ID=<>
AWS_SECRET_KEY=<>
```

## To do

- add dev container branch
- add boiler plate projects
- dry-run mode
- cli
