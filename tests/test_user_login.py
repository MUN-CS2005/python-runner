"""Tests for flask server"""

import unittest
from main import flaskServer
from main.database.user import User


class TestUserLogin(unittest.TestCase):
    """Tests for User login"""

    def setUp(self) -> None:
        User._create_table()
        flaskServer.app.testing = True
        self.app = flaskServer.app.test_client()

    def tearDown(self) -> None:
        User._del_table()

    def test_create_user(self):
        """Test creation of user account through flask server"""
        self.app.post('/register', data=dict(
            username='userTest1',
            password='userTest1pw',
            confirm='userTest1pw'
        ), follow_redirects=True)
        self.assertTrue(User.has_user("userTest1"))

    def test_change_password(self):
        """Test password change through flask server"""
        User.create('userTest1', 'userTest1pw')
        self.app.post('/change_password', data=dict(
            username='userTest1',
            old_password='userTest1pw',
            new_password='avocado'
        ), follow_redirects=True)
        user = User.get('userTest1')
        self.assertEqual(user.password, 'avocado')


if __name__ == "__main__":
    unittest.main()
