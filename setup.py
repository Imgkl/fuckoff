from setuptools import setup, find_packages

setup(
    name="fuckoff",
    version="1.0.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fuckoff=fuckoff.cli:main",
        ],
    },
    install_requires=[
        'questionary==2.0.1',
    ],
    author="Sai Gokula Krishnan",
    description="A CLI tool to manage Zsh history",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Imgkl/fuckoff",
)
