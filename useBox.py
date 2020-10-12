from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class usebox(QWidget):
    def __init__(self):
        super(usebox, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('选框按钮（总）')
        self.resize(340,400)
        self.setCent()
        # 添加组件
        Glayout = QGridLayout()
        label1 = QLabel('职位:')
        label1.setToolTip('单选框')
        self.rbutton = QRadioButton('学生')
        self.rbutton.setChecked(True)
        self.rbutton.toggled.connect(lambda:self.judgetChecked(self.rbutton))
        self.rbutton1 = QRadioButton('教师')
        self.rbutton1.toggled.connect(lambda:self.judgetChecked(self.rbutton1))
        label2 = QLabel('爱好:')
        label2.setToolTip('复选框')
        self.chbox = QCheckBox('乒乓球')
        # 设置复选框为半选中状态
        self.chbox.setTristate(True)
        self.chbox.toggled.connect(lambda :self.judgetChecked(self.chbox))
        # self.chbox.setChecked(Qt.PartiallyChecked)
        self.chbox1 = QCheckBox('羽毛球')
        self.chbox1.toggled.connect(lambda :self.judgetChecked(self.chbox1))
        self.chbox2 = QCheckBox('足球')
        self.chbox2.toggled.connect(lambda :self.judgetChecked(self.chbox2))
        # 下拉框
        label3 = QLabel('院系:')
        label3.setToolTip('下拉框')
        self.combox = QComboBox()
        self.combox.addItems(['机械工程学院','信息与通信学院','计算机学院','商学院'])
        self.combox.currentIndexChanged.connect(self.idexchange)
        # 文本框
        self.textEdit = QTextEdit()
        # self.textEdit.resize(320,100)
        # 添加按钮
        self.button = QPushButton('获取信息')
        self.button.setToolTip('点击获取信息')
        self.button.clicked.connect(self.getmessage)
        Glayout.addWidget(label1,0,0,1,1)
        Glayout.addWidget(self.rbutton,0,1,1,1)
        Glayout.addWidget(self.rbutton1,0,2,1,1)
        Glayout.addWidget(label2,1,0,1,1)
        Glayout.addWidget(self.chbox,1,1,1,1)
        Glayout.addWidget(self.chbox1,1,2,1,1)
        Glayout.addWidget(self.chbox2,1,3,1,1)
        Glayout.addWidget(label3,2,0,1,1)
        Glayout.addWidget(self.combox,2,1,1,2)
        Glayout.addWidget(self.textEdit,3,0,2,4)
        Glayout.addWidget(self.button,5,0,1,4)
        self.setLayout(Glayout)

    # 判断单选框是否变化事件
    def judgetChecked(self,bt):
        print(str(bt.text())+str(bt.isChecked()))
    # 下拉框索引改变事件
    def idexchange(self,i):
        print('院系是：'+str(self.combox.currentText()))
    def getmessage(self):
        if self.rbutton.isChecked():
            job = self.rbutton.text()
        else:
            job = self.rbutton.text()
        habit = str()
        if self.chbox.isChecked():
            habit += ' ' + str(self.chbox.text())
        if self.chbox1.isChecked():
            habit += ' ' + str(self.chbox1.text())
        if self.chbox2.isChecked():
            habit += ' ' + str(self.chbox2.text())
        yx = self.combox.currentText()
        self.textEdit.setHtml(f'<font color=blue size=14>获取到的信息：<br/>职位：{job}<br/>爱好：{habit}<br/>院系：{yx}</font>')
        print('我被点击了')
    def setCent(self):
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width()/2-win_size.width()/2),int(screen_size.height()/2-win_size.height()/2))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('M:\Project File\PyQt5\image\微信.png'))
    window = usebox()
    window.show()
    app.exec_()