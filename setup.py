from setuptools import setup

setup(
    name='splash',
    version='0.0.4',
    packages=['splash', 'splash.commands'],
    entry_points={
        'console_scripts': [
            'splash = splash.cli:cli'
        ]
    }
)
