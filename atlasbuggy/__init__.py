import sys
from .datastream.datastream import DataStream
from .datastream.asyncstream import AsyncStream
from .datastream.threadedstream import ThreadedStream
from .robot import Robot
from .logparser import LogParser


def get_platform():
    """Use for platform specific operations"""
    if sys.platform.startswith('darwin'):  # OS X
        return "mac"
    elif (sys.platform.startswith('linux') or sys.platform.startswith(
            'cygwin')):
        return "linux"
    elif sys.platform.startswith('win'):  # Windows
        return "windows"
    else:
        return None
