from setuptools import setup

setup(
    name='acacia',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'acacia = cli.main:main'
        ]
    }
)
