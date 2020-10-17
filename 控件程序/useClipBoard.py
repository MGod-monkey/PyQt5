from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap,QDrag
from PyQt5.QtCore import Qt
import sys

# 剪切板使用案例

class ClipBoard(QMainWindow):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.setWindowTitle('使用剪切板')
        self.resize(300, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.textCopyButton = QPushButton('复制')
        self.textCopyButton.setToolTip('点击复制文本')
        self.textPasteButton = QPushButton('粘贴')
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText('你看我几分像从前！')
        self.imageCopyButton = QPushButton('复制')
        self.imagePasteButton = QPushButton('粘贴')
        self.imagelabel = QLabel()
        self.imagelabel.setPixmap(QPixmap('../image/游戏.ico'))
        self.imagelabel.setAlignment(Qt.AlignCenter)
        self.textCopyButton.clicked.connect(self.copyText)
        self.textPasteButton.clicked.connect(self.pasteText)
        self.imageCopyButton.clicked.connect(self.copyimage)
        self.imagePasteButton.clicked.connect(self.pasteimage)
        widget = QWidget()
        Glayout = QGridLayout()
        Glayout.addWidget(self.lineEdit,0,0,1,3)
        Glayout.addWidget(self.textCopyButton,0,3,1,1)
        Glayout.addWidget(self.textPasteButton,0,4,1,1)
        Glayout.addWidget(self.imagelabel,1,0,2,3)
        Glayout.addWidget(self.imageCopyButton,1,3,1,2)
        Glayout.addWidget(self.imagePasteButton,2,3,1,2)
        widget.setLayout(Glayout)
        self.setCentralWidget(widget)

    def copyText(self):
        # 剪切板
        clipboard = QApplication.clipboard()
        # 将编辑框的文字复制到剪切板中
        clipboard.setText(self.lineEdit.text())
        # ok = QMessageBox.information(self,'消息框','复制成功',QMessageBox.Ok)
        status = self.statusBar()
        status.showMessage('复制成功',1000)
    def pasteText(self):
        clipboard = QApplication.clipboard()
        # 将裁剪版的内容粘贴到编辑框中
        self.lineEdit.setText(clipboard.text())
        status = self.statusBar()
        status.showMessage('粘贴成功', 1000)
        # ok = QMessageBox.information(self,'消息框','粘贴成功',QMessageBox.Ok)
    def copyimage(self):
        clipboard = QApplication.clipboard()
        # 将图片内容复制到裁剪版
        clipboard.setPixmap(self.imagelabel.pixmap())
        clipboard.setText(self.lineEdit.text())
        status = self.statusBar()
        status.showMessage('复制成功', 1000)
    def pasteimage(self):
        clipboard = QApplication.clipboard()
        # 将裁剪版的图片复制到图片标签
        self.imagelabel.setPixmap(clipboard.pixmap())
        status = self.statusBar()
        status.showMessage('粘贴成功', 1000)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = ClipBoard()
    window.show()
    app.exec_()