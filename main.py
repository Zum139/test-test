from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets  import (QWidget, QMessageBox, QApplication, QToolTip,
    QPushButton)
import PyQt5
import time
import sys


#Class the window my program
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My program')

        qbtn = QPushButton('Remind', self)
        qbtn.clicked.connect(self.RemindsWin)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.show()
        #time.sleep(20)
        #exit(0)

    #window for remind
    def RemindsWin(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Second Window')


class RemindsWin(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    #window for remind
    def remindsWin(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Second Window')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
