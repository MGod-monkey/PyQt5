from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

# 菜单栏设置案例

class MenuBar(QMainWindow):
    def __init__(self):
        super(MenuBar, self).__init__()
        self.setWindowTitle('菜单使用案例')
        self.resize(300, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 获取菜单栏
        menu = self.menuBar()
        # 添加菜单栏有两种方式
        # 添加菜单
        file = menu.addMenu('文件(&File)')
        #   直接添加
        file.addAction('新建(&New)')
        # 创建QAction后再添加
        action_save = QAction('保存(&Save)',self)
        # 添加快捷键
        action_save.setShortcut('Ctrl + S')
        # 添加分割符
        file.addSeparator()
        file.addAction(action_save)

        # 多级菜单
        about = menu.addMenu('关于(&About)')
        about.addAction('关于软件')
        about.addSeparator()
        about_author = about.addMenu('关于作者')
        name = QAction('作者名字', self)
        # 单击事件
        name.triggered.connect(self.print_name)
        about_author.addAction(name)
        age = QAction('作者年龄',self)
        # 单击事件
        age.triggered.connect(self.print_age)
        about_author.addAction(age)
    def print_name(self):
        self.statusBar().showMessage('作者：@MGod_monkey',1000)
    def print_age(self):
        self.statusBar().showMessage('年龄：男生的年龄是能随便问的吗',1000)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MenuBar()
    mainWindow.show()
    app.exec_()
