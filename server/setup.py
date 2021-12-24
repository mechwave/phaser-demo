"""Setup."""

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='phaser_server_app',
    version='0.0.1',
    url='https://github.com/mechwave/phaser-demo',
    platforms='all',
    python_requires='>=3.8',
    packages=['phaser_server_app'],
    install_requires=required
)
