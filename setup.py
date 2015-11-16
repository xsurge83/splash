from setuptools import setup, find_packages

setup(
    name='splash',
    version='0.0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'splash = splash.cli:cli'
        ]
    }
)
