## Ex3-9.date and time


from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()
print(datetime.toString()) # 토 7 1 20:03:10 2023
print(datetime.toString('d.M.yy hh:mm:ss')) # 1.7.23 20:03:10
print(datetime.toString('dd.MM.yyyy, hh:mm:ss')) # 01.07.2023, 20:03:10
print(datetime.toString(Qt.DefaultLocaleLongDate)) # 2023년 7월 1일 토요일 오후 8:03:10
print(datetime.toString(Qt.DefaultLocaleShortDate)) # 2023-07-01 오후 8:03