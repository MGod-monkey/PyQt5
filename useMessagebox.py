from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
import sys

class useMessagebox(QWidget):
    def __init__(self):
        super(useMessagebox, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('消息对话框')
        self.resize(100,180)
        self.screen_size = QDesktopWidget().geometry()
        self.win_size = self.geometry()
        self.move(int(self.screen_size.width() / 2 - self.win_size.width() / 2),
                  int(self.screen_size.height() / 2 - self.win_size.height() / 2))
        button1 = QPushButton('关于对话框')
        button1.clicked.connect(self.showMessagebox)
        button2 = QPushButton('错误对话框')
        button2.clicked.connect(self.showMessagebox)
        button3 = QPushButton('警告对话框')
        button3.clicked.connect(self.showMessagebox)
        button4 = QPushButton('提问对话框')
        button4.clicked.connect(self.showMessagebox)
        button5 = QPushButton('消息对话框')
        button5.clicked.connect(self.showMessagebox)
        Vlayout = QVBoxLayout()
        Vlayout.addWidget(button1)
        Vlayout.addWidget(button2)
        Vlayout.addWidget(button3)
        Vlayout.addWidget(button4)
        Vlayout.addWidget(button5)
        self.setLayout(Vlayout)
    def showMessagebox(self):
        sender = self.sender()
        if sender.text() == '关于对话框':
            # def about(self, QWidget, p_str, p_str_1)->p_str:标题，p_str_1:内容，仅有一个OK按钮
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif sender.text() == '消息对话框':
            #def information(self, QWidget, p_str, p_str_1, buttons, QMessageBox_StandardButtons=None,QMessageBox_StandardButton=None, *args, **kwargs)
            #p_str->标题，p_str_1->内容,buttons->QMessageBox.Yes/QMessageBox.No等等
            result = QMessageBox.information(self,'消息','这是一个消息对话框对么？',QMessageBox.Yes|QMessageBox.No)
            if result == QMessageBox.Yes:
                print('消息框返回信息为'+ str(result == QMessageBox.Yes))
            else:
                print('消息框返回信息为' + str(result == QMessageBox.No))
        elif sender.text() == '错误对话框':
            QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Ok)
        elif sender.text() == '警告对话框':
            QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Ok)
        else:
            QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('M:\Project File\PyQt5\image\ios.ico'))
    window = useMessagebox()
    window.show()
    app.exec_()