import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap
# from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'pyqt test'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.lb1 = QLabel(self)
        self.pixmap = QPixmap('logobig.png')
        self.lb1.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(),self.pixmap.height())

        self.lb2 = QLabel("01 02 03 04 05\n06 07 08 09 10\n11 21 23 24 15", self)
        self.btn1 = QPushButton("입력", self)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb1, 0, 0)
        grid.addWidget(self.lb2, 0, 0)

        grid.addWidget(self.btn1, 0, 1)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
