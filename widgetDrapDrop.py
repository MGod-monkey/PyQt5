from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap,QDrag
from PyQt5.QtCore import Qt
import sys

"""
让控件支持拖拽功能
1，A.setDragEnabled(True)->让控件A可拖拽
2, B.setAcceptDrops(True)->让控件B可接受拖拽信息

B(信号):
1，dragEnterEvent()->将A托到B触发
2，dropEvent()->将A拖到B并放下触发
"""
class mycombobox(QComboBox):
    def __init__(self):
        super(mycombobox,self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):
        # 当拖动的控件是文本时触发
        if e.mimeData().hasText():
            self.resize(self.size().width()*2,self.size().height()*2)
            e.accept()
        else:
            e.ignore()
    def dragLeaveEvent(self, *args, **kwargs):
        self.resize(int(self.size().width()/2),int(self.size().height()/2))
    def dropEvent(self,e):
        self.addItem(e.mimeData().text())
class DragDrop(QWidget):
    def __init__(self):
        super(DragDrop, self).__init__()
        self.setWindowTitle('拖拽文本')
        self.resize(300, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        label = QLabel('将左边文本托拽到右边可在右边下拉框中添加项目')
        lineEdit = QLineEdit()
        lineEdit.setText('你倒是拖我啊')
        # 设置编辑框可拖拽
        lineEdit.setDragEnabled(True)
        combox = mycombobox()
        Vlayout = QVBoxLayout()
        Vlayout.addWidget(label)
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(lineEdit)
        Hlayout.addWidget(combox)
        Vlayout.addLayout(Hlayout)
        self.setLayout(Vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('.\image\ios.ico'))
    window = DragDrop()
    window.show()
    app.exec_()

