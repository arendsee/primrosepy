from setuptools import setup

from primrosepy.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="primrosepy",
    version=__version__,
    description="simple manipulation of trees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arendsee/primrosepy",
    author="Zebulun Arendsee",
    author_email="zbwrnz@gmail.com",
    packages=["primrosepy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["primrosepy=primrosepy.ui:main"]},
    installation_requires=["click"],
    py_modules=["primrosepy"],
    zip_safe=False,
)
