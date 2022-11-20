"""Creates SQL Connection"""
import sqlite3
import os


class Connection:
    """A connection to the database"""
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    con = sqlite3.connect(os.path.join(ROOT_DIR, 'database.db'), check_same_thread=False)

    @classmethod
    def get_instance(cls) -> sqlite3.Connection:
        """Returns an SQL Connection to the database"""
        return cls.con
