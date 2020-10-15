from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPalette,QColor
from PyQt5.QtCore import Qt
import sys

# 改变字体综合案例，运用到了QLabel,QSlider,QSpinbox,QCombobox,QFontDialog,QColorDialog
# 可以设置字体大小，样式，颜色
class setFontsize(QWidget):
    def __init__(self):
        super(setFontsize, self).__init__()
        self.initUI()
    def initUI(self):
        # 窗口布局
        self.setWindowTitle('改变字体样式')
        self.resize(380,460)
        screen_size = QDesktopWidget().geometry()
        win_size = self.geometry()
        self.move(int(screen_size.width() / 2 - win_size.width() / 2),
                  int(screen_size.height() / 2 - win_size.height() / 2))

        # 添加组件
        # 标签的字体变量(字体，字号，颜色)
        self.font_text = '宋体'
        self.size = 14
        self.color = '#000000'
        self.label = QLabel('你看我有啥变化')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(self.font_text,self.size))
        # 改变字体大小-计数器
        self.spinbox = QSpinBox()
        self.spinbox.setToolTip('计数器设置字体大小')
        self.spinbox.setRange(8,30)
        self.spinbox.setValue(self.size)
        # 改变字体大小-滑块
        self.slider = QSlider()
        # 设置滑块水平放置
        self.slider.setValue(self.size)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setToolTip('滑动条设置字体大小')
        # 设置滑块取值范围
        self.slider.setMinimum(8)
        self.slider.setMaximum(30)
        self.fontbox = QFontComboBox()
        self.fontbox.setCurrentText(self.font_text)
        self.fontbox.setToolTip('下拉框设置字体样式')
        self.fontbox.currentIndexChanged.connect(self.changefont)
        # 对话框按钮
        self.button = QPushButton('点我设置字体')
        self.button.setToolTip('字体对话框设置字体')
        self.button.clicked.connect(self.setFont)
        self.button1 = QPushButton('点我设置字体颜色')
        self.button1.setToolTip('颜色对话框设置字体颜色')
        self.button1.clicked.connect(self.setFontColor)
        # 连接槽
        self.spinbox.valueChanged.connect(lambda :self.changefontsize(widget=self.spinbox))
        self.slider.valueChanged.connect(lambda :self.changefontsize(widget=self.slider))
        # 信息标签显示信息
        self.label1 = QLabel()
        self.label1.setFont(QFont('方正喵呜体', 14))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setText('字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(self.font_text,self.size,self.color))
        Glayout = QGridLayout()
        Glayout.addWidget(self.label,0,0,1,4)
        Glayout.addWidget(self.spinbox,1,3,2,1)
        Glayout.addWidget(self.slider,1,0,2,3)
        Glayout.addWidget(self.fontbox,2,0,2,4)
        Glayout.addWidget(self.button,3,0,2,2)
        Glayout.addWidget(self.button1,3,2,2,2)
        Glayout.addWidget(self.label1,4,0,1,4)
        self.setLayout(Glayout)
    # 改变字体大小
    def changefontsize(self,widget):
        self.size = widget.value()
        self.label1.setText(
            '字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(
                self.font_text, self.size, self.color))
        if widget == self.spinbox:
            self.label.setFont(QFont('{}'.format(self.font_text),self.size))
            self.slider.setValue(self.size)
            self.label1.setText('字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(self.font_text, self.size, self.color))
        else:
            self.label.setFont(QFont('{}'.format(self.font_text),self.size))
            self.spinbox.setValue(self.size)
            self.label1.setText(
                '字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(
                    self.font_text, self.size, self.color))
    # 下拉框设置字体
    def changefont(self):
        self.label.setFont(QFont('{}'.format(self.fontbox.currentText()),self.size))
        self.font_text = self.fontbox.currentText()
        self.label1.setText(
            '字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(
                self.font_text, self.size, self.color))
    # 字体对话框设置字体
    def setFont(self):
        font,ok = QFontDialog.getFont()
        if font and ok:
            self.label.setFont(font)
            self.fontbox.setCurrentText(str(self.label.fontInfo().family()))
            self.spinbox.setValue(int(self.label.fontInfo().pointSize()))
            self.slider.setValue(int(self.label.fontInfo().pointSize()))
            self.label1.setText(
                '字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(
                    self.font_text, self.size, self.color))
    # 颜色对话框设置字体颜色
    def setFontColor(self):
        color = QColorDialog.getColor()
        palette = QPalette()
        palette.setColor(QPalette.WindowText,color)
        self.label.setPalette(palette)
        self.color = color.name()
        self.label1.setText(
            '字体：<font color=blue>{}</font> 字号：<font color=green>{}</font> 颜色：<font color=red>{}</font>'.format(
                self.font_text, self.size, self.color))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('.\image\ios.ico'))
    window = setFontsize()
    window.show()
    app.exec_()