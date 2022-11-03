"""Tests for flask"""

import unittest
import requests
import os
from main import flaskServer

class TestFlask(unittest.TestCase):
    """
        Unit test for flaskServer.py
    """
    def setUp(self):
        flaskServer.app.testing = True
        self.app = flaskServer.app.test_client()

    def testResponse(self):
        rv = self.app.post('/run_code', data=dict(
           codestuff='print(1)',
       ), follow_redirects=True)
        assert b'print(1)' in rv.data
        assert b'1' in rv.data


if __name__=="__main__":
    unittest.main()
