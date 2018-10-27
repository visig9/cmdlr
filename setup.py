#!/usr/bin/env python3

"""Install script."""

import sys

from setuptools import setup, find_packages

from src.cmdlr.info import PROJECT_NAME
from src.cmdlr.info import VERSION
from src.cmdlr.info import AUTHOR
from src.cmdlr.info import AUTHOR_EMAIL
from src.cmdlr.info import LICENSE
from src.cmdlr.info import PROJECT_URL
from src.cmdlr.info import DESCRIPTION


if not sys.version_info >= (3, 5, 3):
    print("ERROR: You cannot install because python version < 3.5.3")

    sys.exit(1)


setup(
    name=PROJECT_NAME,
    version='.'.join(map(lambda x: str(x), VERSION)),

    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=PROJECT_URL,
    description=DESCRIPTION,
    long_description='''''',
    keywords='comic download archive',

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Archiving"],

    install_requires=[
        'pyyaml >=3, <4',
        'aiohttp >=3, <4',
        'voluptuous',
        'wcwidth',
        'lxml >=3.8, <4',
        'beautifulsoup4',
        ],
    setup_requires=[],

    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,

    entry_points={
        'console_scripts': ['cmdlr = cmdlr.cmdline:main'],
        'setuptools.installation': ['eggsecutable = cmdlr.cmdline:main']
        },
    )
