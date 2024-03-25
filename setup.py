from setuptools import setup, find_packages

setup(
    name="fuckoff-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fuckoff=fuckoff.cli:main",
        ],
    },
    install_requires=[
        'prompt_toolkit>=3.0.0',
        'questionary==2.0.1',
    ],
    author="Sai Gokula Krishnan",
    description="A CLI tool to manage Zsh history",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Imgkl/fuckoff",
)
