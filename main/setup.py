from setuptools import setup, find_packages

setup(
    name='codeServer',
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)