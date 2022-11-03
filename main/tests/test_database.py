"""Tests for the project"""
import unittest
from main.database.user import User


class TestDatabase(unittest.TestCase):
    """Tests for Persistent Storage"""

    def setUp(self) -> None:
        User._create_table()

    def tearDown(self) -> None:
        User._del_table()

    def test_create(self) -> None:
        """Test creation of a User object"""
        User.create("User1", "pass1")
        User.create("User2", "pass2", "code2")
        user1 = User.get("User1")
        user2 = User.get("User2")

        self.assertEqual(("User1", "pass1"), (user1.username, user1.password))
        self.assertEqual(("User2", "pass2", "code2"), (user2.username, user2.password, user2.code))

    def test_save(self) -> None:
        """Test User object being updated properly"""
        User("User3", "pass3", "code3").save()
        user1 = User.get("User3")
        self.assertEqual(("User3", "pass3", "code3"),
                         (user1.username, user1.password, user1.code))
        User("User3", "changed_pass", "changed_code3").save()
        user2 = User.get("User3")
        self.assertEqual(("User3", "changed_pass", "changed_code3"),
                         (user2.username, user2.password, user2.code))


if __name__ == '__main__':
    unittest.main()
