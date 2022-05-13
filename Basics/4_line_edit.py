import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using Line edit ")
        self.UI()
    
    def UI(self):
        self.nameTextBox=QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please Enter your username")
        self.nameTextBox.move(120, 50)
        self.passTextBox=QLineEdit(self)
        self.passTextBox.setPlaceholderText("Please Enter your Password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120,80)
        button= QPushButton("Enter",self)
        button.move(150,120)
        button.clicked.connect(self.getValues)
        self.show()
    
    def getValues(self):
        name=self.nameTextBox.text()
        password=self.passTextBox.text()
        self.setWindowTitle("Your user name is: "+name+ "Your Password: "+password)
    

def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


