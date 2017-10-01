import click
import json
import os
from sys import platform

PROJECTS_FILE = "projects.json"

# name = "vias_intranet"
# try:
#     mode = "r" if os.path.exists(PROJECTS_FILE) else "w"
#     with open("projects.json", mode=mode, encoding="utf-8") as json_projects:
#         if os.stat(PROJECTS_FILE).st_size > 0:
#             projects = json.load(json_projects)
#             selected_project = projects.get(name)
#             if selected_project:
#                 activate_venv = os.path.join(
#                     selected_project["venv"],
#                     "bin" if not platform.startswith("win") else "Scripts",
#                     "activate")
#                 commande = '{} "{}" && cd "{}" && code .'.format(
#                     "source" if not platform.startswith("win") else "",
#                     activate_venv, selected_project["path"])
#                 os.system(commande)
#             else:
#                 click.echo("No project with this name.")
#         else:
#             click.echo("No project added yet.")
# except FileNotFoundError:
#     click.echo("No project added yet.")
# except Exception as ex:
#     click.echo(str(ex))


def load_projects():
    """return Json contains all projects"""
    with open(PROJECTS_FILE, mode="a+", encoding="utf-8") as json_projects:
        if mode == "r+" and os.stat(PROJECTS_FILE).st_size > 0:
            projects = json.load(json_projects)
        if not projects.get(project["name"]):
            projects[name] = {"path": path, "venv": venv}
            json.dump(projects, json_projects)

        else:
            click.echo("Project already exists")


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


dump_project({
    "name": "vias_int{}".format(122),
    "path": "/home/rey/Desktop/Projects/vias_intranet/vias_app",
    "venv": "/home/rey/Desktop/Projects/vias_intranet/venv"
})
