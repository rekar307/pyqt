## Ex3-9. date display

import sys
from PyQt5.QtCore import QDate, Qt


now = QDate.currentDate()
print(now.toString()) # 토 7 1 2023
print(now.toString('d.M.yy')) # 1.7.23
print(now.toString('dd.MM.yyyy')) # 01.07.2023
print(now.toString('ddd.MMMM.yyyy')) # 토.7월.2023
print(now.toString(Qt.ISODate)) # 2023-07-01
print(now.toString(Qt.DefaultLocaleLongDate)) # 2023년 7월 1일 토요일