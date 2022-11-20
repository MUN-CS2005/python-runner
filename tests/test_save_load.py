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
        user = User.get("test1")
        self.app.post("/save_code", data=dict(
            username=user.username,
            codestuff="print(\"saving\")"
        ), follow_redirects=True)
        self.assertEqual("print(\"saving\")", user.code)

    def testLoad(self):
        user = User.get("test1")
        user.code = "print(\"loading\")"
        user.save()
        load = self.app.post("/load_code", data=dict(
            username=user.username,
        ), follow_redirects=True)
        assert b'loading' in load.data
