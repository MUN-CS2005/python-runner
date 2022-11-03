## Create a User object
Params: 
- username: str
- password: str
- code: str

The username must be unique for all objects, and will be used to uniquely identify users.


## Usage
To add a user to the database:
```py
User.create("User1", "pass1", "code1")
```
To update:
```py
User("User1", "updated_pass", "updated_code").save()
```

To run the tests from the terminal, write:
```py
python -m unittest
```
in the main directory