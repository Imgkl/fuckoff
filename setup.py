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
    ],
    author="Your Name",
    description="A CLI tool to manage Zsh history",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/fuckoff-cli",
)
