from PyQt5.QtWidgets import QToolTip,QApplication,QWidget,QLineEdit,QDesktopWidget,QDialog,QGridLayout,QPushButton,QLabel
import sys
from PyQt5.QtCore import Qt

class useLineEdit(QDialog):
    def __init__(self):
        super(useLineEdit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入框的简单使用')
        screen = QDesktopWidget().geometry()
        size = self.geometry()
        self.move(int(screen.width()/2-size.width()/2),int(screen.height()/2-size.height()/2))

        # 添加组件
        button1 = QPushButton('&Sign in')
        button2 = QPushButton('&Cancle')
        Label1 = QLabel('&Name')
        Label1.setText('登录')
        Label2 = QLabel('&Password')
        Label2.setText('密码')
        # 设置标签与输入框的伙伴关系
        Label1.setBuddy(button1)
        Label2.setBuddy(button2)
        # 添加编辑框,并设置回显模式
        Lineedit1 = QLineEdit()
        Lineedit2 = QLineEdit()
        Lineedit1.setEchoMode(QLineEdit.Normal)
        Lineedit2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # 设置编辑框默认显示消息
        Lineedit1.setPlaceholderText('请输入账号')
        Lineedit2.setPlaceholderText('请输入密码')
        # 添加网格布局(QGridLayout.addWidget(控件名,rowIndex,columnIndex,row,column)->行位置,列位置,所占的行空间,所占的列空间)
        GridLayout = QGridLayout()
        GridLayout.addWidget(Label1,0,0,1,1)
        GridLayout.addWidget(Lineedit1,0,1,1,3)
        GridLayout.addWidget(Label2,1,0,1,1)
        GridLayout.addWidget(Lineedit2,1,1,1,3)
        GridLayout.addWidget(button1,2,0,1,2)
        GridLayout.addWidget(button2,2,2,1,2)
        self.setLayout(GridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = useLineEdit()
    mainWindow.show()
    app.exec_()