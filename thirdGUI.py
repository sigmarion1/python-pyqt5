import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QComboBox)
# from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 window'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):


        self.lb1 = QLabel('Option1', self)


        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb1, 0, 0)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())