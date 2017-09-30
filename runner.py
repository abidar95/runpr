import click
import json
import os
from sys import platform

PROJECTS_FILE = "projects.json"

name = "vias_intranet"
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
