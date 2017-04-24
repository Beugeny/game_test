from PyQt5 import QtCore
from time import time

import SignalMng

cur_time = 0.0
frame_per_sec = 30
ms_by_frame = 1 / frame_per_sec * 1000
timer = None


def tick():
    global cur_time
    cur_time += ms_by_frame
    SignalMng.TICK.dispatch(ms_by_frame)


def start():
    global timer
    timer = QtCore.QTimer()
    timer.setSingleShot(False)
    timer.timeout.connect(tick)
    timer.start(ms_by_frame)  # every ms_by_frame milliseconds
