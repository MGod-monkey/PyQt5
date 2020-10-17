from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys

"""
显示二维表数据
数据源
Model
需要创建一个数据源（Model）和QTableView实例，然后将二者关联
MVC：Model   Viewer  Controller
MVC的目的就是将后端的数据和前端页面的耦合度降低
"""

class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('TableView案例')
        self.resize(360, 360)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 创建模型(4x4)
        self.model = QStandardItemModel(4,4)
        # 设置表格水平标题
        self.model.setHorizontalHeaderLabels(['姓名','年龄','性别','喜好'])
        # 创建表格控件和Model
        self.tableView = QTableView(self)
        self.tableView.setGeometry(0,0,300,360)
        self.tableView.setModel(self.model)
        # 往表格内添加数据（每个表格单元格都是一个QStandardItem()）
        item11 = QStandardItem('肥逼1号')
        item12 = QStandardItem('19')
        item13 = QStandardItem('男')
        item14 = QStandardItem('电竞')

        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)
        self.model.setItem(0,3,item14)
    def change(self):
        print('数据改变了')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = TableView()
    window.show()
    app.exec_()
