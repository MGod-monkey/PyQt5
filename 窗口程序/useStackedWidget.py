from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys

# 堆栈窗口控件实例
class StackedWidget(QWidget):
    def __init__(self):
        super(StackedWidget, self).__init__()
        self.setWindowTitle('堆栈控件案例')
        self.resize(360, 100)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.listview = QListWidget()
        self.listview.addItems(['联系方式','个人信息','教育程度'])

        # 创建3个窗口
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.widget3 = QWidget()
        self.initUI()

        # 创建堆栈窗口对象
        self.stacked = QStackedWidget()
        self.stacked.addWidget(self.widget1)
        self.stacked.addWidget(self.widget2)
        self.stacked.addWidget(self.widget3)

        # 创建一个水平布局
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.listview)
        Hlayout.addWidget(self.stacked)
        self.setLayout(Hlayout)

        # 设置列表控件点击事件
        self.listview.currentRowChanged.connect(self.changeStacked)
    # 初始化3个窗口界面
    def initUI(self):
        Flayout = QFormLayout()
        Flayout.addRow('姓名',QLineEdit())
        Flayout.addRow('学号',QLineEdit())
        com1 = QComboBox()
        com1.addItems(['男','女','其他'])
        Flayout.addRow('性别',com1)
        Flayout.addRow(QPushButton('登录'),QPushButton('注册'))
        self.widget2.setLayout(Flayout)
        Flayout1 = QFormLayout()
        Flayout1.addRow('电话',QLineEdit())
        Flayout1.addRow('邮箱',QLineEdit())
        self.widget1.setLayout(Flayout1)
        Flayout2 = QFormLayout()
        com2 = QComboBox()
        com2.addItems(['研究生','本科','高中','小学'])
        Flayout2.addRow('个人学历',com2)
        self.widget3.setLayout(Flayout2)

    # 堆栈窗口改变事件
    def changeStacked(self,row):
        self.stacked.setCurrentIndex(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = StackedWidget()
    window.show()
    app.exec_()