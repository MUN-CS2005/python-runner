   ## C Team Submission 5

- Scrum meeting notes can be found on the kanban board under "Meeting minutes 1" and "Meeting minutes 2" respectively.
- User stories can be found on the kanban board under "User stories". the comments feature an @ "GIT_USER_NAME" to represent who wrote the stories in the comment. 
- Tasks generated from the stories can be found under "Todo future submissions" with the tag suggestion and a brief description of its objective and an @ "GIT_USER_NAME" for whose story the suggestion came from
- The performance review for cycle 5 is a part of "Meeting minutes 2" on the kanban board. As a group we discussed the strengths and weaknesses each member faced
- All other documentation is within the kanban board or meeting minutes

   ## C Team Submission 6
- The log file can be found under main/log.txt
- Code review was acomplished by reviewing each pull request
- The team meeting notes can be found on the kanban board under "Meeting minutes 3" and "Meeting minutes 4" respectively.
- The performance review for cycle 6 is a part of "Meeting minutes 4" on the kanban board. As a group we discussed how progress happended within cycle 6
- The next task can be found in a comment on "meeting minutes 4"
- previous tasks were updated upon request of new features 
- intial due date for Cycle is Novemeber 19th with updates based on code review due 10 PM Novemeber 20th

   ## C Team Submission 7
- The admin page can create new users and view all users found on the database
- The admin page can be accssed with Username: admin Password: software
- The upload can take any kind of file but works best with .py or .txt
- The download will download files as .py files
- The timing system adds a default 10 minute timer that can be edited within the timing module
- Displays pylint to the user on the webpage
- Code review was acomplished by reviewing each pull request
- The team meeting notes can be found on the kanban board under "Meeting minutes 5" and "Meeting minutes 6" respectively.
- The performance review for cycle 7 is a part of "Meeting minutes 6" on the kanban board. reviewing the work that was done
- previous tasks were updated upon request of new features
- intial due date for Cycle is Decemebr 4th with review of pull requests at 9 PM December 5th

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
$ python3 -m unittest discover tests
```

To start the server run the follwing file
```
main/flask_server.py
```

To gain access to the admin page:
   Username: "admin"
   Password: "software"
   
