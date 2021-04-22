#!/usr/bin/python3
"""Main module."""

import os
import subprocess
import logging

def installed_pkgs():
    raw_list = subprocess.run(["pip", "freeze"], capture_output=True)
    old_list = raw_list.stdout.decode()
    print(old_list.splitlines())
if __name__ == "__main__":
    installed_pkgs()
