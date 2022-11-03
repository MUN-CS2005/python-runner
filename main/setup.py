from setuptools import setup, find_packages

setup(
    name='codeServer',
    version='0.1.0',
    description='A small coding based web application',
    author='Team C',
    packages=find_packages(include=['main', 'main.*']),
    install_requires=["sqlite3", "flask"],
    package_data={
        '': ['*.txt', '*.pdf']},

    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
