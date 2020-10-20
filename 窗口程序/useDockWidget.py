from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel
from PyQt5.QtCore import Qt,QDate,QDateTime,QTime
import sys

# 停靠控件实例
class DockWidget(QMainWindow):
    def __init__(self):
        super(DockWidget, self).__init__()
        self.setWindowTitle('停靠窗口案例')
        self.resize(360, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        self.dock = QDockWidget('工具栏',self)
        self.listWidget = QListWidget()
        self.listWidget.addItems(['复制','粘贴'])
        self.dock.setWidget(self.listWidget)

        self.addDockWidget(Qt.TopDockWidgetArea,self.dock)
        # if self.dock.close()==True:
        #     self.addDockWidget(Qt.TopDockWidgetArea, self.dock)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../image/ios.ico'))
    window = DockWidget()
    window.show()
    app.exec_()