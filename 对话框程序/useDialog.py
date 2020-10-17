from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
import sys
import random

class useDialog(QMainWindow):
    def __init__(self):
        super(useDialog, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('弹出对话框')
        self.resize(100,180)
        self.screen_size = QDesktopWidget().geometry()
        self.win_size = self.geometry()
        self.move(int(self.screen_size.width() / 2 - self.win_size.width() / 2),
                  int(self.screen_size.height() / 2 - self.win_size.height() / 2))
        button = QPushButton('点击弹出对话框')
        button.clicked.connect(self.showdialog)
        self.setCentralWidget(button)
    def showdialog(self):
        # 添加对话框
        random_x = random.randrange(0,self.screen_size.width()-self.win_size.width())
        random_y = random.randrange(0,self.screen_size.height()-self.win_size.height())
        dialog = QDialog()
        dialog.resize(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)  # 设置对话框弹出时主窗口所有控件不可用
        label = QLabel('请问你是SB么？')
        label.setFont(QFont('黑体',13))
        label.setAlignment(Qt.AlignCenter)
        button1 = QPushButton('是')
        button2 = QPushButton('不是')
        button1.clicked.connect(dialog.close)
        button2.clicked.connect(self.showdialog)
        Glayout = QGridLayout()
        Glayout.addWidget(label,0,0,1,2)
        Glayout.addWidget(button1,1,0,1,1)
        Glayout.addWidget(button2,1,1,1,1)
        dialog.setLayout(Glayout)
        dialog.move(random_x,random_y)
        dialog.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('/image/ios.ico'))
    window = useDialog()
    window.show()
    app.exec_()