#!/usr/bin/python3
"""Main module."""
import os
import subprocess
import json
from typing import Dict, List, Union


class PipUpdater:
    """Automates checking for and, updating PyPI packages.\n
    packages: Dict[str, Dict[str, str]]
        - { "current":{}, "new":{}, "old":{} }\n
    See functions for additional information.\n
    *Note - PipUpdater.scan() is a static method.
    """

    DEFAULT_LOCATION: str = f"{os.getcwd()}/.updater_history.json"

    def __init__(self) -> None:
        """Load installed PyPI packages & check for data from previous run.\n
        Sets:
            packages["current"] = {pkg, ver ...}
        """
        self.packages = PipUpdater.scan()

        self.save_changes()

    @staticmethod
    def scan() -> List[Dict[str, str]]:
        """ Using `pip list --outdated` scan() returns a list of updatable packages.
        """
        _keys = ("name", "current_version", "newer_version")
        _pip_pkgs = (
            subprocess.run(["pip", "list", "--outdated"], capture_output=True)
            .stdout.decode()
            .splitlines()
        )

        return [
            dict(zip(_keys, pkg)) for pkg in [tuple(t.split()[:3]) for t in _pip_pkgs[2:]]
        ]

    def update_all(self) -> None:
        for pkg in self.packages:
            print(pkg["name"])

    def save_changes(self, *args: str) -> None:
        """Saves the self.packages dictionary as a JSON file.
        - Takes a filepath optional argument
            - Or, uses default (cwd) location w/ name .updater_history
        """
        _save_path: str

        if len(args) == 0:
            _save_path = PipUpdater.DEFAULT_LOCATION

        elif len(args) > 1:
            raise IndexError("save_changes() accepts one file path argument")

        else:
            _save_path = args[0]

        with open(_save_path, "w") as s:
            json.dump(self.packages, s, indent=4)

def main():
    updater = PipUpdater()
    updater.update_all()
