import sqlite3


class Connection:
    """A connection to the database"""
    con = sqlite3.connect("database.db")

    @classmethod
    def get_instance(cls) -> sqlite3.Connection:
        return cls.con
