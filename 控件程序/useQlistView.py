from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys

"""
显示类数据
数据源
Model
需要创建一个数据源（Model）和QTableView实例，然后将二者关联
MVC：Model   Viewer  Controller
MVC的目的就是将后端的数据和前端页面的耦合度降低
"""

class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('QListView案例')
        self.resize(360, 360)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 创建listWidget控件->该控件是ListView的子类，不需要创建Model而且多了很多个方法
        self.listwidget = QListWidget(self)
        self.listwidget.setGeometry(0,0,360,200)
        # 添加项目
        # QListWidgetItem(QIcon, str, parent: QListWidget = None, type: int = QListWidgetItem.Type)
        item1 = QListWidgetItem(QIcon('../image/360.ico'),'360极速',self.listwidget,200)
        item2 = QListWidgetItem(QIcon('../image/2345.ico'),'2345浏览器',self.listwidget,200)

        self.listwidget.itemClicked.connect(self.clicked)

    def clicked(self,index):
        QMessageBox.information(self,'提示框','你点击了'+index.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = ListView()
    window.show()
    app.exec_()