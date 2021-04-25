#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jesse Fogarty",
    author_email='jfogarty@tuta.io',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A python module that automates the updating of installed PyPI modules.",
    entry_points={
        'console_scripts': [
            'pip_updater=pip_updater.pip_updater:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pip_updater',
    name='pip_updater',
    packages=find_packages(include=['pip_updater', 'pip_updater.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jessefogarty/pip_updater',
    version='0.0.1',
    zip_safe=False,
)
