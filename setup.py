import os
import re

from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="githubActionTest",
    version=get_version("githubActionTest"),
    description="some",
    url="https://github.com/zzozzolev/githubActionTest",
    author="zzlev",
    license="Unlicense",
    packages=["githubActionTest",],
    install_requires=[
    ],
    dependency_links=[
    ],
    include_package_data=True,
    zip_safe=False,
)