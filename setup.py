import os
from setuptools import find_packages
from distutils.core import setup

readmeText = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

# Pass all the above to the setup script
setup(
    name="DemoDemo",
    version="1.2.3",
    author="meawoppl",
    author_email="Demo@demo.com",
    description="Demo",
    license="BSD-2",
    url="https://github.com/3scan",
    packages=find_packages(),
    long_description=readmeText
)
