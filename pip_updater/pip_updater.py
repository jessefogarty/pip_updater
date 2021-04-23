#!/usr/bin/python3
"""Main module."""

import os
import subprocess
import re
import json
from typing import Dict


def _installed_pkgs() -> Dict[str, str]:
    old_pkgs = (
        subprocess.run(["pip", "freeze"], capture_output=True)
        .stdout.decode()
        .splitlines()
    )
    return {n: v for n, v in [re.split("==", p) for p in old_pkgs]}


class PipUpdater:
    """ Automates checking for and, updating PyPI packages.\n
        packages: Dict[str, Dict[str, str]]
            - { "current":{}, "new":{}, "last":{} }\n
        See functions for additional information.
    """

    DEFAULT_LOCATION: str = f"{os.getcwd()}/.updater_history"

    def __init__(self) -> None:
        """ Load installed PyPI packages & check for data from previous run.\n
            Sets:
                packages["current"] = {pkg, ver ...}
        """

        self.packages = {}  # type: Dict[str, Dict[str, str]]

        # TODO: _prev_data load = same dict format as packages
        # Check for update history -
        if os.path.exists(PipUpdater.DEFAULT_LOCATION) != False:
            with open(PipUpdater.DEFAULT_LOCATION) as f:
                _prev_data = json.loads(f.read())

        self.packages["current"] = _installed_pkgs()


    def save_changes(self, *args: str) -> None:
        """ Saves the self.packages dictionary as a JSON file.
                - Takes a filepath optional argument
                    - Or, uses default (cwd) location w/ name .updater_history
        """
        if len(args) is 0:
            with open(PipUpdater.DEFAULT_LOCATION, "w") as s:
                json.dump(self.packages, s, indent=4)



if __name__ == "__main__":
    t = PipUpdater()
    t.save_changes()
