#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


with open("README.md", "r", encoding="UTF-8") as f:
    readme = f.read()

with open("requirements.txt", "r", encoding="UTF-8") as f:
    requirements = f.read().splitlines()

setup(
    name="pyscp",
    version="0.1.0",
    description="a wrapper around scp to make life easier",
    long_description=readme,
    long_description_content_type="test/markdown",
    author="Joe Yesselman",
    author_email="jyesselm@unl.edu",
    url="https://github.com/jyesselm/pyscp",
    packages=[
        "pyscp",
    ],
    package_dir={"pyscp": "pyscp"},
    py_modules=["pyscp/cli"],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="pyscp",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={"console_scripts": ["pyscp = pyscp.cli:cli"]},
)
