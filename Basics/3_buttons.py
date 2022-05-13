from cgitb import text
import sys
from PyQt5.QtWidgets import *

class WindowButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using Buttons ")
        self.UI()
    
    def UI(self):
        self.text=QLabel("Hello Python", self)
        enterButton= QPushButton("Enter",self)
        exitButton=QPushButton("Exit",self)
        self.text.move(150,50)
        enterButton.move(100,80)
        exitButton.move(200,80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()
    
    def enterFunc(self):
        self.text.setText("Entered. :)")
    
    def exitFunc(self):
        self.text.setText("Exited. :(")
        

def main():
    App= QApplication(sys.argv)
    window = WindowButton()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


