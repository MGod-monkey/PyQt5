from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QFontInfo
from PyQt5.QtCore import Qt
import sys

class setFontsize(QWidget):
    def __init__(self):
        super(setFontsize, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('改变字体样式')
        self.resize(340,400)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 添加组件
        self.label = QLabel('你看我有啥变化')
        self.label.setAlignment(Qt.AlignCenter)
        self.spinbox = QSpinBox()
        self.spinbox.setToolTip('设置字体大小')
        self.spinbox.setRange(12,24)
        self.slider = QSlider()
        # 设置滑块水平放置
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setToolTip('滑动设置字体大小')
        # 设置滑块取值范围
        self.slider.setMinimum(12)
        self.slider.setMaximum(24)
        self.fontbox = QFontComboBox()
        self.fontbox.setCurrentText('黑体')
        self.fontbox.setToolTip('点我设置字体')
        self.fontbox.currentIndexChanged.connect(self.changefont)
        self.button = QPushButton('点我设置字体')
        self.button.clicked.connect(self.setFont)
        # 连接槽
        self.spinbox.valueChanged.connect(lambda :self.changefontsize(widget=self.spinbox))
        self.slider.valueChanged.connect(lambda :self.changefontsize(widget=self.slider))
        Glayout = QGridLayout()
        Glayout.addWidget(self.label,0,0,1,4)
        Glayout.addWidget(self.spinbox,1,3,1,1)
        Glayout.addWidget(self.slider,1,0,1,3)
        Glayout.addWidget(self.fontbox,2,0,2,4)
        Glayout.addWidget(self.button,3,0,1,4)
        self.setLayout(Glayout)
        self.size = 12
    def changefontsize(self,widget):
        self.size = widget.value()
        if widget == self.spinbox:
            self.label.setFont(QFont('{}'.format(self.fontbox.currentText()),self.size))
            self.slider.setValue(self.size)
        else:
            self.label.setFont(QFont('{}'.format(self.fontbox.currentText()),self.size))
            self.spinbox.setValue(self.size)
    def changefont(self):
        self.label.setFont(QFont('{}'.format(self.fontbox.currentText()),self.size))
    def setFont(self):
        font,ok = QFontDialog.getFont()
        if font and ok:
            self.label.setFont(font)
            self.fontbox.setCurrentText(str(self.label.fontInfo().family()))
            self.spinbox.setValue(int(self.label.fontInfo().pointSize()))
            self.slider.setValue(int(self.label.fontInfo().pointSize()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('M:\Project File\PyQt5\image\微信.png'))
    window = setFontsize()
    window.show()
    app.exec_()