import os
import unittest
from main import flask_server
from main.database.user import User
from io import BytesIO


class TestSaveLoad(unittest.TestCase):

    def setUp(self) -> None:
        flask_server.app.testing = True
        self.app = flask_server.app.test_client()
        try:
            User.create("test1", "pass1")
        except KeyError:
            User.del_user("test1")
            User.create("test1", "pass1")
        user = User.get("test1")
        self.app.post("/login", data=dict(
            username=user.username,
            password=user.password
        ))

    def tearDown(self) -> None:

        User.del_user("test1")

    def testDownload(self):
        """
        tests the download in flask_server
        downloads file and checks if it matches
        then removes file
        """
        self.app.post("/download", data=dict(codestuff="text = 'words'"))
        try:
            import download
            self.assertEqual(download.text, 'words')
            os.remove("download.py")
        except Exception:
            self.fail("Could not find the file")

    def testUpload(self):
        """
        tests the upload in flask_server
        uploads file to server before saving to database
        and comparing database
        """
        data = self.app.post("/upload",
                             data={'filename': (BytesIO(b'data = "some data"'), 'testFile.py')},
                             )
        assert b'some data' in data.data
