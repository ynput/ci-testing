# -*- coding: utf-8 -*-
"""Setup info for building OpenPype 3.0."""
import os
import sys
import re
from pathlib import Path

version = {}

openpype_root = Path(os.path.dirname(__file__))

with open(openpype_root / "openpypeCItest" / "version.py") as fp:
    exec(fp.read(), version)

version_match = re.search(r"(\d+\.\d+.\d+).*", version["__version__"])
__version__ = version_match.group(1)


from setuptools import setup, find_packages

setup(
    name='openpypeCItest',
    version=__version__,
    url='https://github.com/pypeclub/ci-test.git',
    author='Pype Club',
    author_email='info@pype.club',
    description='Testing openpype CI setup',
    packages=find_packages()
)
