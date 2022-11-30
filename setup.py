from setuptools import setup, find_packages
from main.database.user import User

setup(
    name='codeServer',
    version='0.2.0',
    description='A small coding based web application',
    author='Team C',
    packages=find_packages(include=['main', 'main.*']),
    install_requires=['Flask'],
    package_data={
        '': ['*.txt', '*.pdf']},
)
User.create_table()
