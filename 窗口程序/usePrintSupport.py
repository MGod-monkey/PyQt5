from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *  # 打印机模块
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

# 调用打印机模块
class usePrintSupport(QMainWindow):
    def __init__(self):
        super(usePrintSupport, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('打印机打印案例')
        screen_size = QDesktopWidget().geometry()
        self.setGeometry(int(screen_size.width() / 2 - 360 / 2),int(screen_size.height() / 2 - 450 / 2),360,450)

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('待打印文本')
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(10,10,180,420)
        button1 = QPushButton('打开文件',self)
        button2 = QPushButton('打印文件',self)
        button1.setGeometry(220,160,100,40)
        button2.setGeometry(220,220,100,40)
        button1.clicked.connect(self.openFile)
        button2.clicked.connect(self.printFile)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,'打开文本文件','.','文本文件(*.txt *.py)')
        if filename:
            with open(filename[0],'r',encoding='utf-8') as fp:
                self.textEdit.setText(fp.read())
    def printFile(self):
        printer = QPrinter()    # 创建打印类
        printerDialog = QPrintDialog(printer,self)
        if printerDialog.Accepted == printerDialog.exec():
            self.textEdit.print(printer)
            self.statusBar().showMessage('打印成功',1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = usePrintSupport()
    window.show()
    app.exec_()
