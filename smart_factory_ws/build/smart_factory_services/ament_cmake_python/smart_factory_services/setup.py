from setuptools import find_packages
from setuptools import setup

setup(
    name='smart_factory_services',
    version='0.0.0',
    packages=find_packages(
        include=('smart_factory_services', 'smart_factory_services.*')),
)
