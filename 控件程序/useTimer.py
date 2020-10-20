from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel,QFont
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime,QTimer
import sys

# 动态显示当前时间
# 多线程：同时处理多个任务

class useTimer(QMainWindow):
    def __init__(self):
        super(useTimer, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.resize(360, 100)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.timer = QTimer()
        # 设置计时器间隔时间
        self.timer.start(1000)
        # 当时间过一秒后发送一个信号
        self.timer.timeout.connect(self.showTime)
        self.label = QLabel(QDateTime.currentDateTime().toString('当前时间：yyyy年MM月dd日 dddd HH:mm:ss'))
        self.label.setFont(QFont('华文行楷',13))
        self.setCentralWidget(self.label)
    def showTime(self):
        self.label.setText(QDateTime.currentDateTime().toString('当前时间：yyyy年MM月dd日 dddd HH:mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = useTimer()
    window.show()
    app.exec_()