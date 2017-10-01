import click
import json
import os
from sys import platform

PROJECTS_FILE = "projects.json"


def venv_commande(venv):
    if venv:
        activate_venv = os.path.join(
            venv,
            "bin" if not platform.startswith("win") else "Scripts",
            "activate")
        return '{} "{}"'.format(
            "source" if not platform.startswith("win") else "",
            activate_venv
        )
    else:
        return None


def dump_project(project):
    """
    Add a Project to the projects list
    project's format: {"name": name, "path": path, "venv": venv}
    """
    try:
        with open(PROJECTS_FILE, mode="r+", encoding="utf-8") as json_projects:
            projects = []
            if os.stat(PROJECTS_FILE).st_size > 0:
                projects = json.load(json_projects)
            if any(pr["name"] == project["name"] for pr in projects):
                click.echo("Project already exists")
            else:
                projects.append(project)
                json_projects.seek(0)
                json.dump(projects, json_projects)
    except ValueError as ex:
        click.echo("Invalid JSON File.!")
    except Exception as ex:
        click.echo(str(ex))


def load_projects():
    """return list of saved projects"""
    with open(PROJECTS_FILE, mode="w+", encoding="utf-8") as json_projects:
        if os.stat(PROJECTS_FILE).st_size > 0:
            return json.load(json_projects)
        return None


def load_project(name):
    """return Project from saved project list"""
    with open(PROJECTS_FILE, mode="r", encoding="utf-8") as json_projects:
        if os.stat(PROJECTS_FILE).st_size > 0:
            projects = json.load(json_projects)
            for project in projects:
                if project.get("name") == name:
                    return project
        return None


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
        project = load_project(name)
        if project:
            commande = '{} && cd "{}" && code .'.format(
                venv_commande(project.get("venv")),
                project.get("path"))
            os.system(commande)
        else:
            click.echo("No project with this name.")
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
    dump_project({
        "name": name,
        "path": path,
        "venv": venv
    })


@run.command()
@click.argument("name", type=click.STRING)
def delete(name):
    """
    Add a project to Run-Project
    Parameters:
        name: the name of project
        path: the path of project
        venv: the path of project
    """
    dump_project({
        "name": name,
        "path": path,
        "venv": venv
    })


@run.command()
def list():
    projects = load_projects()
    if projects:
        click.echo(projects)
    else:
        click.echo("No project added yet.")


@run.command()
def file_path():
    click.echo(os.path.abspath(PROJECTS_FILE))
