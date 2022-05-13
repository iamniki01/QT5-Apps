from mailbox import mbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using Spin Boxes ")
        self.UI()
    
    def UI(self):
        self.spinBox=QSpinBox(self)
        self.spinBox.move(150,110)
        self.spinBox.setRange(25,110) #set minimum and maximum value respectively
        self.spinBox.setPrefix("$ ")
        self.spinBox.setSuffix(".00 Cents")
        self.spinBox.setSingleStep(5)
        # self.spinBox.valueChanged.connect(self.getValue)
        button= QPushButton("Send",self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        self.show()
    
    def getValue(self,value):
        value=self.spinBox.value()
        print(value)



def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


