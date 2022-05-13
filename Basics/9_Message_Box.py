import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using Message Boxes ")
        self.UI()
    
    def UI(self):
        button= QPushButton("Imformation",self)
        button.setFont(font)
        button.move(200,110)
        button.clicked.connect(self.infoBox)
        button= QPushButton("Exit",self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.questionBox)
        self.show()
    
    def infoBox(self):
        mbox=QMessageBox.information(self, "Info!!", "This is the demo of Message Box and its Types")


    
    def questionBox(self):
        mbox=QMessageBox.question(self, "Warning!!", "Are Your Sure to exit?", QMessageBox.Yes | QMessageBox.NO | QMessageBox.Cancel, QMessageBox.No)
        if mbox ==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No:
            print("You clicked No")




def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


