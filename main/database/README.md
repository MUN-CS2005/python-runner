## Create a User object
Params: 
- username: str
- password: str
- code: str

The username must be unique for all objects, and will be used to uniquely identify users.


## Usage
To create the database:
```py
User.create_table()
```
To add a user to the database:
```py
User.create("User1", "pass1", "code1")
```
To update any parameter associated with the username provided; This will create a new entry in the database if user with specified username does not exist.
```py
User("User1", "updated_pass", "updated_code").save()
```
To get a User object from the database:
```py
User.get("User1")
```
To check if User exists:
```py
User.has_user("User1")
```
To delete a user:
```py
User.del_user("User1")
```


To run the tests from the terminal, write in the terminal:
```py
python -m unittest
```
