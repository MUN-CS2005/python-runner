"""User Module"""
from __future__ import annotations
from .connection import Connection


class User:
    """Stores a User in the database"""
    con = Connection.get_instance()

    def __init__(self, username: str, password: str, code: str = "") -> None:
        self.username = username
        self.password = password
        self.code = code

    @classmethod
    def create_table(cls) -> None:
        """Method for setup and testing"""
        cur = cls.con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS user
            (username VARCHAR(255) PRIMARY KEY, 
            password VARCHAR(255), 
            code VARCHAR(255));
        """)
        cls.con.commit()
        cur.close()

    @classmethod
    def create(cls, username: str, password: str, code: str = "") -> User:
        """
        Class method to create a user. Also saves to database.
        Raises KeyError if user already exists.
        """
        cur = cls.con.cursor()
        result = cur.execute("SELECT * from user WHERE username = ?;", (username,)).fetchone()
        if result:
            cur.close()
            raise KeyError("User already exists")
        cur.execute("""
                INSERT INTO user(username, password, code) values (?,?,?);
            """, (username, password, code))
        cls.con.commit()
        cur.close()
        return cls(username, password)

    def save(self) -> None:
        """Method to update a user in the database. Creates a new user if it does not exist"""
        cur = User.con.cursor()
        result = cur.execute("SELECT * from user WHERE username = ?;",
                             (self.username,)).fetchone()
        if result:
            cur.execute("UPDATE user SET password = ?, code = ? WHERE username = ?;",
                        (self.password, self.code, self.username))
        else:
            cur.execute("""
            INSERT INTO user(username, password, code) values (?,?,?);
        """, (self.username, self.password, self.code))
        User.con.commit()
        cur.close()

    @classmethod
    def get(cls, username: str) -> User:
        """
        Return a user object with the provided username.
        Raises KeyError if user does not exist.
        """
        cur = cls.con.cursor()
        result = cur.execute("SELECT * from user WHERE username = ?;", (username,)).fetchone()
        if not result:
            cur.close()
            raise KeyError("User does not exist")
        cur.close()
        return cls(*result)

    @classmethod
    def has_user(cls, username: str) -> bool:
        """
        Checks if user with username in database, returns bool
        """
        cur = cls.con.cursor()
        result = cur.execute("SELECT * from user WHERE username = ?;", (username,)).fetchone()
        cur.close()
        if not result:
            return False
        return True

    @classmethod
    def fetch_all(self):
        """
        Returns iterator of every user found in database
        """
        cur = self.con.cursor()
        result = cur.execute("SELECT * from user;", cur.fetchall())
        if not result:
            cur.close()
            raise KeyError("No users in database")
        iterator = iter(result)
        return iterator

    @classmethod
    def _del_table(cls) -> None:
        """Private method for setup and testing"""
        cur = cls.con.cursor()
        cur.execute("DROP TABLE user;")
        cls.con.commit()
        cur.close()

    @classmethod
    def del_user(cls, username: str) -> None:
        """Method to delete a user form"""
        cur = cls.con.cursor()
        cur.execute("DELETE FROM user WHERE username = ?;", (username,))
        cls.con.commit()
        cur.close()
