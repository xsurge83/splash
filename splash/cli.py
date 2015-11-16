import click
from .commands import menu, download


@click.group()
def cli():
    pass

cli.add_command(menu.cli)
cli.add_command(download.cli)

