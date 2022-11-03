"""
The setup for team c's submission.
uses setup tools
"""


from setuptools import setup, find_packages

setup(
    name='codeServer',
    version='0.1.0',

    packages=find_packages(include=['main', 'main.*']),
    # make sure required packages are installed
    install_requires=["sqlite3", "flask"],
    package_data={
        '': ['*.txt', '*.pdf', '*.md']},

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    author='Team C',
    description='A small coding based web application submitted for 2005 coursework',


)
