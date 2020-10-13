from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
import calendar
import sys

class useInoutDialog(QWidget):
    def __init__(self):
        super(useInoutDialog, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('输入对话框')
        self.resize(100,360)
        self.screen_size = QDesktopWidget().geometry()
        self.win_size = self.geometry()
        self.move(int(self.screen_size.width() / 2 - self.win_size.width() / 2),
                  int(self.screen_size.height() / 2 - self.win_size.height() / 2))
        # 姓名输入
        self.label1 = QLabel('姓名')
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText('请输入姓名')
        self.button1 = QPushButton('输入')
        self.button1.clicked.connect(lambda :self.gettext(self.lineEdit1))
        # 性别选择
        self.label2 = QLabel('性别')
        self.combox1 = QComboBox()
        self.combox1.addItems(['男','女','其他'])
        self.button2 = QPushButton('选择')
        self.button2.clicked.connect(self.getitem)
        # 出生日期设定
        self.label3 = QLabel('出生日期')
        # 年份
        self.combox2 = QComboBox()
        self.combox2.addItems(list(map(str,list(range(1950,2550)))))
        self.combox2.setEditText('1990')
        self.combox2.currentIndexChanged.connect(self.setday)
        self.button3 = QPushButton('年')
        self.button3.clicked.connect(lambda :self.getBurid(self.button3))
        # 月份
        self.combox3 = QComboBox()
        self.combox3.addItems(list(map(str,list(range(1, 13)))))
        self.combox3.setEditText('1')
        self.combox3.currentIndexChanged.connect(self.setday)
        self.button4 = QPushButton('月')
        self.button4.clicked.connect(lambda: self.getBurid(self.button4))
        # 日份
        # 最大日期数
        self.maxday = 31
        self.combox4 = QComboBox()
        self.combox4.addItems(list(map(str,list(range(1, self.maxday+1)))))
        self.combox4.setEditText('1')
        self.button5 = QPushButton('日')
        self.button5.clicked.connect(lambda: self.getBurid(self.button5))
        # 个人宣言
        self.label4 = QLabel('个人宣言')
        self.textEdit = QTextEdit()
        self.textEdit.setText('这个人很懒，什么都没写！')
        self.textEdit.setReadOnly(True)
        self.textEdit.setAlignment(Qt.AlignLeft)
        self.setFont(QFont('宋体',12))
        self.button6 = QPushButton('输入内容')
        self.button6.clicked.connect(lambda :self.gettext(self.textEdit))

        # 添加布局
        Glayout = QGridLayout()
        Glayout.addWidget(self.label1,0,0,1,1)
        Glayout.addWidget(self.label2,1,0,1,1)
        Glayout.addWidget(self.label3,2,0,1,1)
        Glayout.addWidget(self.label4,3,0,1,1)
        Glayout.addWidget(self.lineEdit1,0,1,1,6)
        Glayout.addWidget(self.button1,0,7,1,1)
        Glayout.addWidget(self.combox1,1,1,1,2)
        Glayout.addWidget(self.button2,1,3,1,2)
        Glayout.addWidget(self.combox2,2,1,1,2)
        Glayout.addWidget(self.button3,2,3,1,1)
        Glayout.addWidget(self.combox3,2,4,1,1)
        Glayout.addWidget(self.button4,2,5,1,1)
        Glayout.addWidget(self.combox4,2,6,1,1)
        Glayout.addWidget(self.button5,2,7,1,1)
        Glayout.addWidget(self.textEdit,3,1,2,6)
        Glayout.addWidget(self.button6,3,7,1,7)
        self.setLayout(Glayout)
    # 文本输入框
    def gettext(self,widget):
        # def getText(self, QWidget, p_str, p_str_1, echo=None, text='', flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs)
        # p_str->标题，p_str1->内容
        # return:输入的文本，状态
        if widget == self.button1:
            text,ok = QInputDialog.getText(self,'姓名','请输入你的姓名')
        else:
            text, ok = QInputDialog.getText(self, '宣言', '请输入你的宣言')
        if text and ok:
            widget.setText(text)
    # 选择框
    def getitem(self):
        #def getItem(self, QWidget, p_str, p_str_1, Iterable, p_str=None, *args, **kwargs)
        # p_str->标题，p_str1->内容,Iterable->选项
        # return:选项结果，状态
        item,ok = QInputDialog.getItem(self,'性别','请选择你的性别',['男','女','其他'])
        if item and ok:
            self.combox1.setCurrentText(item)


    # 选择框
    def getBurid(self,widget):
        # def getItem(self, QWidget, p_str, p_str_1, Iterable, p_str=None, *args, **kwargs)
        # p_str->标题，p_str1->内容,Iterable->选项
        # return:选项结果，状态
        if widget.text() == '年':
            item, ok = QInputDialog.getItem(self, '年份', '请选择你的出生年份',list(map(str,list(range(1950,2550)))))
            if item and ok:
                self.combox2.setCurrentText(item)
        elif widget.text() == '月':
            item, ok = QInputDialog.getItem(self, '月份', '请选择你的出生月份',list(map(str,list(range(1,13)))))
            if item and ok:
                self.combox3.setCurrentText(item)
        else:
            item, ok = QInputDialog.getItem(self, '天份', '请选择你的出生天份', list(map(str,list(range(1, self.maxday+1)))))
            if item and ok:
                self.combox4.setCurrentText(item)
    def setday(self):
        year = int(self.combox2.currentText())
        month = int(self.combox3.currentText())
        # def monthrange(year, month)
        # 输入一个元组(1,31)
        self.maxday = calendar.monthrange(year,month)[1]
        self.combox4.setMaxCount(self.maxday)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('M:\Project File\PyQt5\image\ios.ico'))
    window = useInoutDialog()
    window.show()
    app.exec_()