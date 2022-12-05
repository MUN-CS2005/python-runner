"""Tests for flask server - admin page functionality"""

import unittest
from main import flask_server
from main.database.user import User


class TestUserLogin(unittest.TestCase):
    """Tests for User login"""

    def setUp(self) -> None:
        User.create_table()
        flask_server.app.testing = True
        self.app = flask_server.app.test_client()

    def tearDown(self) -> None:
        User._del_table()

    def test_admin_account_creation(self):
        """Test creation of user account through page accessed from admin page"""
        self.app.post('/create', data=dict(
            username='userTest1',
            password='userTest1pw',
        ), follow_redirects=True)
        self.assertTrue(User.has_user("userTest1"))

    def test_admin_account_deletion(self):
        """Test removal of user account through page accessed from admin page"""
        User.create("userTesting12345", "54321")
        self.assertTrue(User.has_user("userTesting12345"))
        self.app.post('/delete', data=dict(
            username='userTesting12345',
        ), follow_redirects=True)
        self.assertFalse(User.has_user("userTesting12345"))

    def test_admin_access_to_accounts_data(self):
        """Test admin access to user's code in database"""
        User.create("orange", "skype", "print(123456789)")
        rv = self.app.post('/admin', data=dict(
            username='orange',
        ))
        assert b'print(123456789)' in rv.data


if __name__ == "__main__":
    unittest.main()
