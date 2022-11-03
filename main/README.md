## C Team Submission 5

- Scrum meeting notes can be found on the kanban board under "Meeting minutes 1" and "Meeting minutes 2" respectively.
- User stories can be found on the kanban board under "User stories". the comments feature an @ "GIT_USER_NAME" to represent who wrote the stories in the comment. 
- Tasks generated from the stories can be found under "Todo future submissions" with the tag suggestion and a brief description of its objective and an @ "GIT_USER_NAME" for whose story the suggestion came from
- The performance review for cycle 5 is a part of "Meeting minutes 2" on the kanban board. As a group we discussed the strengths and weaknesses each member faced
- All other documentation is within the kanban board or meeting minutes

## Installation

To set up "codeServer" it is recommended to have a virtual environment

run
```
pip install -e .
```

in order to run the setup file and install a development environment

 run
```
python -m unittest discover
```
 to run the tests from the command line.
 
to run unit tests:
    unit tests are located within the tests folder and can be used by 
```
$ python3 -m unittest discover moleflask.tests
```