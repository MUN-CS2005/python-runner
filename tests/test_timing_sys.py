"""Test for TimingSystem Module"""
import unittest
from main.TimingSystem import TimingSys
import time


class TestTimingSys(unittest.TestCase):

    timing = None

    def setUp(self):
        self.timing = TimingSys.Timing(10)  # specify log file name

    def test_case_1(self):
        self.assertEqual(10, self.timing.get_time_limit())
        time.sleep(1)  # record some data
        self.assertEqual(9, round(self.timing.get_time_remaining()))
        self.assertEqual(False, self.timing.check_time_exceed())
        self.assertEqual(1, round(self.timing.get_time_passed()))


if __name__ == "__main__":
    unittest.main()
