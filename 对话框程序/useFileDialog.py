from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
import sys

#
class useFileDialog(QWidget):
    def __init__(self):
        super(useFileDialog, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('文件对话框')
        self.resize(250,350)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))
        self.button1 = QPushButton('打开图片文件')
        self.button1.clicked.connect(self.openimage)
        self.button2 = QPushButton('打开文本文件')
        self.button2.clicked.connect(self.opentext)
        self.label1 = QLabel()
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2 = QTextEdit()
        self.label2.setReadOnly(True)
        Vlayout = QVBoxLayout()
        Vlayout.addWidget(self.button1)
        Vlayout.addWidget(self.label1)
        Vlayout.addWidget(self.button2)
        Vlayout.addWidget(self.label2)
        self.setLayout(Vlayout)

    def openimage(self):
        #def getOpenFileName(self, parent=None, caption='', directory='', filter='', initialFilter='', options,
        #                   QFileDialog_Options=None, QFileDialog_Option=None, *args,
        #                   **kwargs):  # real signature unknown; NOTE: unreliabl
        # parent:窗口，caption:窗口标题，directory:默认路径，filter:筛选器，->返回一个元组
        filename = QFileDialog.getOpenFileName(self,'打开图像','.','图像文件(*.png *.jpg *.ico)')
        self.label1.setPixmap(QPixmap(filename[0]))
    def opentext(self):
        filename = QFileDialog.getOpenFileName(self,'选择文本','.')
        with open(filename[0],encoding='utf-8') as fp:
            self.label2.setText(fp.read())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = useFileDialog()
    window.show()
    app.exec_()