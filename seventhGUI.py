import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QFrame

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 200, 500, 300)

        self.principalLayout = QHBoxLayout(self)

        self.leftFrame = QFrame(self)
        self.leftFrame.setObjectName("lf")
        self.leftFrame.setStyleSheet("""
            QFrame#lf{
            background-image: url(./classroom.png);
            }
        """)

        self.verticalLayoutL = QVBoxLayout(self.leftFrame)
        self.gridLayout = QGridLayout()



        btn = QPushButton(self.leftFrame)
        btn.setText("11")
        self.gridLayout.addWidget(btn, 1, 1)

        btn = QPushButton(self.leftFrame)
        btn.setText("22")
        self.gridLayout.addWidget(btn, 2, 2)

        self.verticalLayoutL.addLayout(self.gridLayout)
        self.principalLayout.addWidget(self.leftFrame)

        self.verticalLayoutR = QVBoxLayout()
        self.gridLayout = QGridLayout()

        lb = QLabel()
        lb.setText("남학생 수 입력")
        self.gridLayout.addWidget(lb, 0, 0)

        le = QLineEdit()
        self.gridLayout.addWidget(le, 0, 1)

        lb = QLabel()
        lb.setText("여학생 수 입력")
        self.gridLayout.addWidget(lb, 1, 0)

        le = QLineEdit()
        self.gridLayout.addWidget(le, 1, 1)

        self.verticalLayoutR.addLayout(self.gridLayout)
        self.principalLayout.addLayout(self.verticalLayoutR)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()