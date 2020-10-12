from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
import sys

class useTextEdit(QMainWindow):
    def __init__(self):
        super(useTextEdit, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(250,350)
        # self.setWindowIcon(QIcon(r'image/w.ico'))
        # 屏幕居中
        screen = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen.width()/2-win_size.width()/2),int(screen.height()/2-win_size.height()/2))
        # 添加组件
        self.TextEdit = QTextEdit()
        # self.TextEdit.setAlignment(Qt.AlignHCenter)
        button1 = QPushButton('显示文本')
        button2 = QPushButton('获取文本')
        button3 = QPushButton('显示HTML')
        button4 = QPushButton('获取HTML')
        button1.clicked.connect(self.showtext)
        button2.clicked.connect(self.gettext)
        button3.clicked.connect(self.showhtml)
        button4.clicked.connect(self.gethtml)
        # 添加垂直布局
        widget = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.TextEdit)
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addWidget(button4)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
    # 槽方法
    def showtext(self):
        self.TextEdit.setPlainText('这是一个文本显示框')
    def gettext(self):
        print(self.TextEdit.toPlainText())
    def showhtml(self):
        self.TextEdit.setHtml('<font color=blue size=18>这是一个带色的文本显示框</font>')
    def gethtml(self):
        print(self.TextEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('M:\Project File\PyQt5\image\微信.png'))
    window = useTextEdit()
    window.show()
    app.exec_()