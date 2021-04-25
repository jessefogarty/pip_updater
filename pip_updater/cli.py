"""Console script for pip_updater."""
from pip_updater.pip_updater import PipUpdater
import sys
import click
from rich import console


# TODO - utilize rich console for a TUI
@click.command()
def main(args=None):
    x = PipUpdater()
    x.update_all()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
