from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys

# 设置时间中和案例，运用到了QCalendar,QDateTimeEdit,QDateEdit,QTimeEdit

class setDateTime(QWidget):
    def __init__(self):
        super(setDateTime, self).__init__()
        self.setWindowTitle('日历显示')
        self.resize(300, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.calendar = QCalendarWidget()
        # 设置显示的最小日期
        self.calendar.setMinimumDate(QDate(1990,1,1))
        # 设置显示的最大日期
        self.calendar.setMaximumDate(QDate(2050,1,1))
        # 设置日历以网格形式显示
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(lambda :self.changeDate(self.calendar))
        # 不同风格的日期时间设置
        # 默认时间
        dateEidt = QDateTimeEdit()
        # 当前时间+日期
        self.dateEidt_now = QDateTimeEdit(QDateTime.currentDateTime())
        self.dateEidt_now.dateChanged.connect(lambda:self.changeDate(self.dateEidt_now))
        self.dateEidt_now.timeChanged.connect(lambda:self.changeTime(self.dateEidt_now))
        # 当前日期
        self.dateEidt_nowDate = QDateTimeEdit(QDate.currentDate())
        self.dateEidt_nowDate.dateChanged.connect(lambda :self.changeDate(self.dateEidt_nowDate))
        # 当前时间
        self.dateEidt_nowTime = QDateTimeEdit(QTime.currentTime())
        self.dateEidt_nowTime.timeChanged.connect(lambda:self.changeTime(self.dateEidt_nowTime))
        # 重置按钮
        self.button = QPushButton('重置')
        self.button.clicked.connect(self.resetDateTime)
        # 显示当前时间
        self.label = QLabel()
        self.label.setText('<font size=4 color=blue>{}</font>'.format(self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))
        self.label.setAlignment(Qt.AlignCenter)
        Vlayout = QVBoxLayout()
        Flayout = QFormLayout()
        Hlayout = QHBoxLayout()
        Vlayout.addWidget(self.calendar)
        Vlayout.addWidget(dateEidt)
        Flayout.addRow(self.label,self.button)
        Vlayout.addWidget(self.dateEidt_now)
        Hlayout.addWidget(self.dateEidt_nowDate)
        Hlayout.addWidget(self.dateEidt_nowTime)
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Flayout)
        self.setLayout(Vlayout)

    def changeDate(self,date):
        if date == self.calendar:
            self.dateEidt_now.setDate(date.selectedDate())
            self.dateEidt_nowDate.setDate(date.selectedDate())
            self.label.setText('<font size=4 color=blue>{}</font>'.format(
                self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))
        else:
            self.calendar.setSelectedDate(date.date())
            self.dateEidt_now.setDate(date.date())
            self.dateEidt_nowDate.setDate(date.date())
            self.label.setText('<font size=4 color=blue>{}</font>'.format(
                self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))
    def changeTime(self,time):
        if time == self.dateEidt_now:
            self.dateEidt_nowTime.setTime(time.time())
            self.label.setText('<font size=4 color=blue>{}</font>'.format(
                self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))
        else:
            self.dateEidt_now.setTime(time.time())
            self.label.setText('<font size=4 color=blue>{}</font>'.format(
                self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))
    def resetDateTime(self):
        self.calendar.setSelectedDate(QDate.currentDate())
        self.dateEidt_now.setDateTime(QDateTime.currentDateTime())
        self.dateEidt_nowDate.setDate(QDate.currentDate())
        self.dateEidt_nowTime.setTime(QTime.currentTime())
        self.label.setText('<font size=4 color=blue>{}</font>'.format(
            self.dateEidt_now.dateTime().toString('yyyy-MM-dd dddd HH:mm')))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('.\image\ios.ico'))
    window = setDateTime()
    window.show()
    app.exec_()
