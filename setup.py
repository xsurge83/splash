from setuptools import setup

setup(
    name='splash',
    version='0.0.4',
    packages=['splash'],
    entry_points={
        'console_scripts': [
            'splash = splash.main:cli'
        ]
    }
)
