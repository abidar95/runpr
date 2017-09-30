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
        with open("projects.json", mode=mode, encoding="utf-8") as json_projects:
            if os.stat(PROJECTS_FILE).st_size > 0:
                projects = json.load(json_projects)
                selected_project = projects.get(name)
                if selected_project:
                    activate_venv = os.path.join(
                        selected_project["venv"],
                        "bin" if not platform.startswith("win") else "Scripts",
                        "activate")
                    commande = '{} "{}" && cd "{}" && code .'.format(
                        "source" if not platform.startswith("win") else "",
                        activate_venv, selected_project["path"])
                    os.system(commande)
                else:
                    click.echo("No project with this name.")
            else:
                click.echo("No project added yet.")
    except FileNotFoundError:
        click.echo("No project added yet.")
    except Exception as ex:
        click.echo(str(ex))


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
    with open("projects.json", mode=mode, encoding="utf-8") as json_projects:
        if mode == "r+" and os.stat(PROJECTS_FILE).st_size > 0:
            projects = json.load(json_projects)
        if not projects.get(name):
            projects[name] = {"path": path, "venv": venv}
            json.dump(projects, json_projects)

        else:
            click.echo("Project already exists")
