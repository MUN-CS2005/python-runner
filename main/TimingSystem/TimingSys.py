import time
"""
A solution for TimingSystem.
Library used:
    time
    
This module can provide a solution for timing and record the duration for each student.

Author: Ruixiao Lu
Date: Nov. 2022

Update History: Dec.4 2022 - Added get_time_remaining() function.
                Nov 2022 - initial commit.
"""


class Timing:
    """
    An instance of this Timing class stores a time of when it is created, an ending time when it is stopped, a time
    limit, and status if a student using this class finished its quiz or not.

    Examples:
        t = Timing(timelimit = 600)
    """
    def __init__(self, timelimit=600):
        """
        :param timelimit: The time limit for a student taking the quiz
        """
        self.start = time.time()
        self.timelimit = timelimit
        self.status = False
        self.duration = None

    def stop(self):
        """
        :return: The duration of a student taking a quiz.
        """
        if not self.status:
            self.duration = (time.time() - self.start)
            self.status = True
            return self.duration
        else:
            return self.duration

    def get_start(self):
        """
        :return: The starting time of its instantiation.
        """
        return self.start

    def get_time_passed(self):
        """
        :return: The time gap between the instantiation and now, or the duration if the quiz is finished.
        """
        if not self.status:
            return time.time() - self.start
        else:
            return self.duration

    def get_time_remaining(self):
        """
        :return: The time remaining.
        """
        if not self.status:
            return self.timelimit - (time.time() - self.start)
        else:
            return 0

    def check_time_exceed(self):
        """
        :return: Boolean if the quiz is over.
        """
        if not self.status:
            timegap = time.time() - self.start
            if timegap >= self.timelimit:
                self.duration = timegap
                self.status = True

            return self.status
        else:
            return True

    def get_time_limit(self):
        """
        :return: an integer number which represents time limit in seconds for this instance.
        """
        return self.timelimit


if __name__ == '__main__':
    t = Timing(1)   # 1 second limit
    time.sleep(2)   # sleep 2 seconds
    print(t.check_time_exceed())  # return true cuz it exceeds
    print(t.stop())  # return 2 seconds as the quiz ends. the student exceeds the quiz limit for 1 second.
