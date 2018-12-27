import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 200, 500, 300)

        self.frame = QFrame()
        self.frame.resize(300,300)
        self.frame.setObjectName("nf")
        self.frame.setStyleSheet("""
            QFrame#nf{
            background-image: url(./classroom.png);
            }
        """)

        self.layout = QVBoxLayout()

        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)

        self.lb1 = QLabel("11")
        self.lb2 = QLabel("22")
        self.lb3 = QLabel("22")


        self.layout.addWidget(self.lb1)
        self.layout.addWidget(self.lb2)
        self.layout.addWidget(self.lb3)


        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()