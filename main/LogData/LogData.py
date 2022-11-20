"""
A solution for LogData.

Log user request/response events including run, save, revert, and other events (as they exist in your project)
with time and date stamp, to a log file. Also indicate which code segment is active/on view,
on the user page, at the time of the event in the log entry.

Library used:
    datetime

Author: Ruixiao Lu
Date: Nov. 2022
"""
from datetime import datetime


class Logdata:
    def __init__(self, file):
        """
        :param file: String, the name of target log file.
        """
        self._file = file

    def record_log(self, *elements):
        """
        Receives one or more strings as parameters and append them to a file,
        including the time of when it is recording.

        :param elements: String, any string to be recorded.
        """
        holder = str(datetime.now().ctime())
        with open(self._file, 'a') as sfile:
            for x in elements:
                holder += "    " + x
            holder += "\n"
            sfile.write(holder)


if __name__ == "__main__":
    logger = Logdata("log.txt")
    for i in range(10):
        logger.record_log("A", "B", "C")
