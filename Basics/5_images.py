from os import remove
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class WindowLabels(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using Images ")
        self.UI()
    
    def UI(self):
        self.image= QLabel(self)
        self.image.setPixmap(QPixmap('images/Python-logo-notext.svg'))
        self.image.move(150,50)
        removeButton =QPushButton("Remove", self)
        removeButton.move(150,220)
        removeButton.clicked.connect(self.removeImg)
        showButton =QPushButton("Show", self)
        showButton.move(260,220)
        removeButton.clicked.connect(self.showImg)
        self.show()
    
    def removeImg(self):
        self.image.close()
    
    def showImg(self):
        self.image.show()

    

def main():
    App= QApplication(sys.argv)
    window = WindowLabels()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


