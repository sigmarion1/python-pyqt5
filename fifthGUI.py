import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class SecWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setStyleSheet('background-image: url(./logobig.png)')

        bt1 = QPushButton("push")

        vbox = QVBoxLayout()
        vbox.addWidget(bt1)

        self.setLayout(vbox)
        # self.setGeometry(500,500,500,500)
        # self.show()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 500, 300)

        lb1 = QLabel("test1")
        lb2 = QLabel("test2")
        sw1 = SecWindow()



        # leftInnerLayOut = QVBoxLayout()

        # lb1.setLayout(leftInnerLayOut)


        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(sw1)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(lb2)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)


        self.setLayout(layout)


        # self.setStyleSheet("""
        #
        #     background-image: url(./logobig.png);
        #
        # """)

        # self.setStyleSheet("""
        # QLabel{
        #     color: red;
        #     font: bold italic 20px;
        #     }
        # """)


        # lb1.setStyleSheet('color: yellow')
        self.setStyleSheet('background-image: url(./logobig.png)')




if __name__ == "__main__":
    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()
    app.exec_()