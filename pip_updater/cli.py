"""Console script for pip_updater."""
import sys
import click
import PipUpdater

@click.command()
def main(args=None):
    x = PipUpdater()
    x.update_all()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
