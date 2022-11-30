"""Tests for flask server"""

import unittest
from main import flask_server


class TestFlask(unittest.TestCase):
    """
        Unit test for flask_server.py
    """

    def setUp(self):
        flask_server.app.testing = True
        self.app = flask_server.app.test_client()

    def test_response(self):
        rv = self.app.post('/run_code', data=dict(
            codestuff='print(1)',
        ), follow_redirects=True)
        assert b'print(1)' in rv.data
        assert b'1' in rv.data


if __name__ == "__main__":
    unittest.main()
