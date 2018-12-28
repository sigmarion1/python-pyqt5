import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QFrame


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Test")

        self.setGeometry(800, 200, 500, 300)
        # self.setFixedSize(500, 300)

        self.principalLayout = QHBoxLayout(self)

        self.leftFrame = QFrame(self)
        self.leftFrame.resize(10,10)
        self.leftFrame.setObjectName("lf")
        self.leftFrame.setStyleSheet("""
            QFrame#lf{
            background-image: url(./logobig.png);
            }
        """)

        self.verticalLayoutL = QVBoxLayout(self.leftFrame)
        self.gridLayout = QGridLayout()


        # self.gridLayout.setColumnStretch(0,1)
        # self.gridLayout.setColumnStretch(6,1)
        #
        # self.gridLayout.setRowStretch(0,1)
        # self.gridLayout.setRowStretch(7,1)


        self.lbArray = list()

        for i in range(6):
            for j in range(5):
                self.lb = QLabel(self)
                self.lbArray.append(self.lb)
                self.lb.setText(str(i*5 + j))
                self.gridLayout.addWidget(self.lb, i+1, j+1)

        for i in range(6):
            for j in range(5):
                self.lbArray[i*5+j].setText('hi')
                # lbArray[i * 5 + j].setStyleSheet("""
                #     background-color: yellow;
                #     font: bold 40px;
                #     """)



        spacerItem = QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem)


        # btn = QPushButton(self.leftFrame)
        # btn.setText("11")
        # self.gridLayout.addWidget(btn, 1, 1)
        #
        # btn = QPushButton(self.leftFrame)
        # btn.setText("22")
        # self.gridLayout.addWidget(btn, 2, 2)

        self.verticalLayoutL.addLayout(self.gridLayout)
        self.principalLayout.addWidget(self.leftFrame)

        self.verticalLayoutR = QVBoxLayout()
        self.gridLayout = QGridLayout()

        self.lb1 = QLabel()
        self.lb1.setText("1번 입력")
        self.gridLayout.addWidget(self.lb1, 0, 0)

        self.le = QLineEdit()
        self.gridLayout.addWidget(self.le, 0, 1)

        self.lb2 = QLabel()
        self.lb2.setText("2번 입력")
        self.gridLayout.addWidget(self.lb2, 1, 0)

        self.le = QLineEdit()
        self.gridLayout.addWidget(self.le, 1, 1)

        self.lb3 = QLabel()
        self.lb3.setText("3번 입력")
        self.gridLayout.addWidget(self.lb3, 2, 0)

        self.le = QLineEdit()
        self.gridLayout.addWidget(self.le, 2, 1)


        self.bt1 = QPushButton()
        self.bt1.setText("변경")
        self.bt1.clicked.connect(self.button_clicked)
        self.gridLayout.addWidget(self.bt1, 3, 1)

        self.verticalLayoutR.addLayout(self.gridLayout)
        self.principalLayout.addLayout(self.verticalLayoutR)

    def button_clicked(self):

        for i in range(6):
            for j in range(5):
                self.lbArray[i * 5 + j].setStyleSheet("""
                    background-color: yellow;
                    font: bold 40px;
                    """)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()