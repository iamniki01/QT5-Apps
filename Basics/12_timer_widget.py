from mailbox import mbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using Timer widget")
        self.UI()
    
    def UI(self):
        self.colorLabel=QLabel( self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("Background-color:green")
        self.colorLabel.move(40,25)
        ###############################
        buttonStart= QPushButton("start",self)
        buttonStart.move(80,300)
        buttonStart.clicked.connect(self.start)
        buttonStop= QPushButton("stop",self)
        buttonStop.move(180,300)
        buttonStop.clicked.connect(self.stop)
        ###############################
        self.timer=QTimer()
        self.timer.setInterval(1000) #1000ms=1sec
        self.timer.timeout.connect(self.changecolor)
        self.value=0
        self.show()
    
    def changeColor(self):
        if self.value==0:
            self.colorLabel.setStyleSheet("Background-color:yellow")
            self.value=1
        else:
            self.colorLabel.setStyleSheet("Background-color:yellow")
            self.value=0

    def start(self):
        self.timer.start()
    
    def stop(self):
        self.timer.stop()


def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


