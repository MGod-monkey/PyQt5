from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

# 菜单栏设置案例

class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.setWindowTitle('工具栏使用案例')
        self.resize(300, 300)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 添加一个工具栏
        self.tb1 = self.addToolBar('File')
        play_action = QAction(QIcon('./image/播放.ico'),'播放',self)
        # 工具栏默认会将QAction的图标设为主显示，而将文本设为提示文本
        # 通过设置QToolBar.setToolButtonStytle()来控制工具栏显示方式
        # 显示方式: Qt.ToolButtonStyle
        # ToolButtonIconOnly = ...  # 只显示图标
        # ToolButtonTextOnly = ...  # 只显示文本
        # ToolButtonTextBesideIcon = ...  # 文本在图标旁边
        # ToolButtonTextUnderIcon = ...  # 文本在图标下边
        # ToolButtonFollowStyle = ...  # 默认显示
        self.tb1.addAction(play_action)
        play_action.triggered.connect(self.clicked)
        stop_action = QAction(QIcon('./image/文本.ico'),'文本',self)
        self.tb1.addAction(stop_action)
        button1 = QPushButton('默认形式')
        button1.clicked.connect(lambda:self.settoolbuttonStyle(Qt.ToolButtonIconOnly))
        button2 = QPushButton('只显文本')
        button2.clicked.connect(lambda: self.settoolbuttonStyle(Qt.ToolButtonTextOnly))
        button3 = QPushButton('文本右显')
        button3.clicked.connect(lambda: self.settoolbuttonStyle(Qt.ToolButtonTextBesideIcon))
        button4 = QPushButton('文本下显')
        button4.clicked.connect(lambda: self.settoolbuttonStyle(Qt.ToolButtonTextUnderIcon))
        widget = QWidget()
        Flayout = QFormLayout()
        Flayout.addRow(button1,button2)
        Flayout.addRow(button3,button4)
        widget.setLayout(Flayout)
        self.setCentralWidget(widget)

    def settoolbuttonStyle(self,style):
        self.tb1.setToolButtonStyle(style)



    def clicked(self):
        self.statusBar().showMessage('播放按钮被点击了',1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ToolBar()
    mainWindow.show()
    app.exec_()
