#!/usr/bin/env python

import os

from setuptools import find_packages, setup

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setup(
    name="vnc2flv-rec",
    version="0.1.0",
    description="Python3 wrapper for flvrec.py tool of vnc2flv",
    author="Iman Azari",
    author_email="azari@mahsan.co",
    url="https://github.com/imanazari70/vnc2flv-rec",
    packages=find_packages(),
    package_data={
        "vnc2flv_rec": ["lib/flvrec"],
    },
    entry_points={
        "console_scripts": [
            "vnc2flv-rec = vnc2flv_rec:main",
        ]
    },
)
