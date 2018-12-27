import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFrame


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 200, 500, 300)


        self.frame = QFrame()
        self.frame.resize(300,300)
        self.frame.setObjectName("nf")
        self.frame.setStyleSheet("""
            QFrame#nf{
            background-image: url(./logobig.png);
            }
        """)

        self.lb1 = QLabel("11")
        self.lb2 = QLabel("22")
        self.lb3 = QLabel("33")

        self.layout = QHBoxLayout()
        self.leftLay = QVBoxLayout()
        self.rightLay = QVBoxLayout()


        self.leftLay.addWidget(self.lb1)
        self.leftLay.addWidget(self.lb2)
        # self.leftLay.addWidget(self.frame)
        self.rightLay.addWidget(self.lb3)
        # self.setCentralWidget(self.frame)

        self.frame.setLayout(self.leftLay)


        self.lb1 = QLabel("11")
        self.lb2 = QLabel("22")
        self.lb3 = QLabel("33")



        self.layout.addLayout(self.leftLay)
        self.layout.addLayout(self.rightLay)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()