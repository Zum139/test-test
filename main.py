#cd .git/Projects/Lessons/1/5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
import PyQt5
import time
import sip


#Class the window my program
class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.w = QWidget()
        self.setGeometry(300, 300, 250, 150)
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

        qbtn1 = QPushButton('Back', self)
        qbtn1.resize(qbtn1.sizeHint())
        qbtn1.clicked.connect(self.initUI)
        qbtn1.move(50, 100)
        qbtn1.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
