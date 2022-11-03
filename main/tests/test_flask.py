"""Tests for flask"""

import unittest
import requests
from .flaskServer import *

class TestFlask(unittest.TestCase):
    """
        Unit test for flaskServer.py
    """
    def testResponse(self):
        flaskServer()
        x = requests.get("http://127.0.0.1:5000/run_code")
        print(x.text)

    def testData(self):
        url = 'http://127.0.0.1:5000/'
        code = "print('1+1')"
        x = requests.post(url, data=code)
        print(x.text)

if __name__=="__main__":
        unittest.main()
