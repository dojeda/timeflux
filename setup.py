""" Setup """

import versioneer
from setuptools import setup, find_packages

with open('README.md', 'rb') as f:
    DESCRIPTION = f.read().decode('utf-8')

DEPENDENCIES = [
    'networkx>=2.3',
    'PyYAML>=5.1',
    'numpy>=1.17',
    'pandas>=0.25',
    'xarray>=0.13',
    'bottleneck>=1.2',
    'scipy>=1.3',
    'pyzmq>=0.1.3',
    'coloredlogs>=10.0',
    'tables>=3.5',
    'pylsl>=1.13',
    'python-osc>=1.7',
    'python-dotenv>=0.10',
    'jsonschema>=3.1'
]

setup(
    name='timeflux',
    packages=find_packages(),
    package_data={
        'timeflux': ['schema/app.json']
    },
    entry_points={
        'console_scripts': ['timeflux = timeflux.timeflux:main']
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Timeflux: acquisition and real-time processing of biosignals.',
    long_description=DESCRIPTION,
    author='Pierre Clisson',
    author_email='contact@timeflux.io',
    url='https://timeflux.io',
    install_requires=DEPENDENCIES
)
