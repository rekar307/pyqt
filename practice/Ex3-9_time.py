## Ex3-9. time display


import sys
from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString()) # 20:00:20
print(time.toString('h.m.s')) # 20.0.20
print(time.toString('hh.mm.ss')) # 20.00.20
print(time.toString('hh.mm.ss.zzz')) # 20.00.20.776
print(time.toString(Qt.DefaultLocaleLongDate)) # 오후 8:00:20
print(time.toString(Qt.DefaultLocaleShortDate)) # 오후 8:00