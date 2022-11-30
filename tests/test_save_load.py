import unittest
from main import flask_server
from main.database.user import User


class TestSaveLoad(unittest.TestCase):

    def setUp(self) -> None:
        flask_server.app.testing = True
        self.app = flask_server.app.test_client()
        try:
            User.create("test1", "pass1")
        except KeyError:
            User.del_user("test1")
            User.create("test1", "pass1")

    def tearDown(self) -> None:
        User.del_user("test1")

    def testSave(self):
        """
        tests the user saving the code
        must first log the user in
        then saves the code
        updates user and tests to see if
        code has been saved
        """

        user = User.get("test1")
        self.app.post("/login", data=dict(
            username=user.username,
            password=user.password
        ))
        self.app.post("/save_code", data=dict(
            codestuff="print(\"saving\")"
        ), follow_redirects=True)
        user = User.get("test1")
        self.assertEqual("print(\"saving\")", user.code)

    def testLoad(self):
        """
        tests the loading function
        first saves test values directly to database
        then tries to retrieve the data
        asserts data has been loaded
        """

        user = User.get("test1")
        user.code = "print(\"loading\")"
        user.save()
        self.app.post("/login", data=dict(
            username=user.username,
            password=user.password
        ))
        load = self.app.post("/load_code", follow_redirects=True)
        assert b'loading' in load.data
