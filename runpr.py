import click
import json
import os
from sys import platform

PROJECTS_FILE = "projects.json"


@click.group()
def run():
    """Script for running Python projects with Virtualenv
    Via Visual Studio Code"""
    pass


@run.command()
@click.argument("name", type=click.STRING, default="-", required=False)
def exec(name):
    """Execute a project via VSCODE"""

    try:
        mode = "r" if os.path.exists(PROJECTS_FILE) else "w"
        json_projects = open("projects.json", mode='r', encoding="utf-8")
        if os.stat(PROJECTS_FILE).st_size > 0:
            projects = json.load(json_projects)
            selected_project = projects.get(name)
            if selected_project:
                if platform.startswith("win"):
                    selected_project["venv"].replace("/", "\\")
                    selected_project["path"].replace("/", "\\")
                    activate_venv = "{}\\Scripts\\activate".format(selected_project["venv"])
                else:
                    activate_venv = "{}/bin/activate".format(selected_project["venv"])
                commande = "{} && cd {} && code .".format(activate_venv, selected_project["path"])
                click.echo(commande)
                os.system(commande)
            json_projects.close()
        else:
            click.echo("No project added yet.")
    except FileNotFoundError:
        click.echo("No project added yet.")


@run.command()
@click.argument("name", type=click.STRING)
@click.argument("path", type=click.Path(exists=True))
@click.argument("venv", type=click.Path(exists=True))
def add(name, path, venv):
    """
    Add a project to Run-Project
    Parameters:
        name: the name of project
        path: the path of project
        venv: the path of project
    """
    projects = {}
    mode = "r+" if os.path.exists(PROJECTS_FILE) else "w"
    json_projects = open("projects.json", mode=mode, encoding="utf-8")
    if mode == "r+" and os.stat(PROJECTS_FILE).st_size > 0:
        projects = json.load(json_projects)
    if not projects.get(name):
        projects[name] = {"path": path, "venv": venv}
        json.dump(projects, json_projects)

    else:
        click.echo("Project already exists")
    json_projects.close()
