from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys


class TreeWidget(QMainWindow):
    def __init__(self):
        super(TreeWidget, self).__init__()
        self.setWindowTitle('树控件案例')
        self.resize(360, 360)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.tree = QTreeWidget()
        self.setCentralWidget(self.tree)

        # 为控件指定列数
        self.tree.setColumnCount(2)
        self.tree.setWindowTitle('设置')
        # 指定列标签
        self.tree.setHeaderLabels(['key','value'])

        # def setColumnWidth(self, p_int, p_int_1):  # real signature unknown; restored from __doc__
        # p_int->列数，p_int_1->列距
        self.tree.setColumnWidth(0,150)
        # 为树控件添加根结点
        root = QTreeWidgetItem(self.tree)
        root.setText(0,'语言设置')
        root.setIcon(0,QIcon('../image/播放器.ico'))
        # 添加根结点下的第一个结点
        language = QTreeWidgetItem(root)
        language.setText(0,'界面语言')
        language.setIcon(0,QIcon('../image/飞机.ico'))
        # 添加第二个根结点
        root1 = QTreeWidgetItem(self.tree)
        root1.setIcon(0,QIcon('../image/记事.ico'))
        root1.setText(0,'背景设置')
        backgroud = QTreeWidgetItem(root1)
        backgroud.setText(0,'背景颜色设置')
        backgroud.setIcon(0,QIcon('../image/远程.ico'))
        # 为树控件添加单击事件
        # self.tree.clicked.connect(self.clicked)
    #
    # def clicked(self,index):
    #     item = self.tree.itemFromIndex(index)
    #     def

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = TreeWidget()
    window.show()
    app.exec_()