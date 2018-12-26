import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtGui import QIcon
from

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 window'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.statusBar().showMessage('Message in statusbar.')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())