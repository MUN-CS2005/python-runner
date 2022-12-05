"""Test LogData Module"""

import unittest
import os
from main import LogData


class TestLogData(unittest.TestCase):

    logger = None

    def setUp(self):
        self.logger = LogData.Logdata('test_logdata.txt')  # specify log file name

    def test_case_1(self):
        self.logger.record_log("A", "B", "C")   # record some data
        self.assertEqual(True, os.path.isfile(r'./test_logdata.txt'))  # check if log file exist
        with open("test_logdata.txt", "r") as sfile:    # read the log file
            for x in sfile:
                assert "A" in x
                assert "B" in x
                assert "C" in x
        os.remove("test_logdata.txt")  # Remove log file of the test


if __name__ == "__main__":
    unittest.main()
