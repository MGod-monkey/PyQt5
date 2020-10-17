from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QLabel,QVBoxLayout,QDesktopWidget
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import Qt # 一些常用的变量
import sys

class label_use(QMainWindow):
    def __init__(self):
        super(label_use, self).__init__()
        self.setUI()
        self.labels()

    def setUI(self):
        self.resize(450,380)
        self.setWindowTitle('标签使用案例')
        self.setCenter()

    # 设置初始位置为中
    def setCenter(self):
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int(screen.width()/2-window_size.width()/2),int(screen.height()/2-window_size.height()/2))

    # 显示标签
    def labels(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setToolTip('这是一个普通标签')
        label1.setText('<font color=blue>这是一个带色的标签</font>')
        label1.setFont(QFont(u'宋体',14))
        # 调色板
        # palette = QPalette()
        # label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)   #设置标签的对齐方式


        label2.setToolTip('这个滑动有惊喜')
        label2.setText('<a href="">没有东西哦</a>')
        label2.linkHovered.connect(self.linkhovered)

        label3.setPixmap(QPixmap('./1.png'))
        label3.setToolTip('这是一个图片标签')
        label3.setAlignment(Qt.AlignCenter)

        label4.setAlignment(Qt.AlignLeft)
        label4.setOpenExternalLinks(True)   #当为True时,为打开超链接,当为false时,为触动事件
        label4.setText("<a href='https://www.baidu.com/'>这是百度网站</a>")
        label4.setToolTip('这是一个超级链接')
        label4.linkActivated.connect(self.linkactived)
        # # 添加一个垂直布局
        vboox = QVBoxLayout()
        vboox.addWidget(label1)
        vboox.addWidget(label2)
        vboox.addWidget(label3)
        vboox.addWidget(label4)
        mainW = QWidget()   # 创建一个临时窗口并附加到主窗口
        mainW.setLayout(vboox)
        self.setCentralWidget(mainW)

    def linkhovered(self):
        # self.statusBar().showMessage('标签2被划过了',1000)
        print('xxx')
    def linkactived(self):
        self.statusBar().showMessage('标签4被点击了',1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = label_use()
    window.show()
    sys.exit(app.exec_())