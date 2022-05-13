import sys
from PyQt5.QtWidgets import *

class WindowLabels(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using Labels ")
        self.UI()
    
    def UI(self):
        text1=QLabel("Hello Python", self)
        text2=QLabel("Hello World!", self)
        text1.move(50,50)
        text1.move(200,150)
        self.show()
    

def main():
    App= QApplication(sys.argv)
    window = WindowLabels()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


