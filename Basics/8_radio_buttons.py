import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using Radio Buttons ")
        self.UI()
    
    def UI(self):
        self.name=QLineEdit(self)
        self.name.setPlaceholderText("Please Enter your name")
        self.name.move(150, 50)
        self.surname=QLineEdit(self)
        self.surname.setPlaceholderText("Please Enter your surname")
        self.surname.move(150,80)
        self.male=QRadioButton("Male",self) #you can make oonly one choice
        self.male.move(150,110)
        self.male.setChecked(True)
        self.female=QRadioButton("Female",self)
        self.female.move(200,110)
        button= QPushButton("Submit",self)
        button.move(150,130)
        button.clicked.connect(self.getValues)
        self.show()


    
    def getValues(self):
        name=self.name.text()
        surname=self.surname.text()
        if self.male.isChecked():
            print("Name: "+name+" Surname: "+surname+"\n You are a Male")
        else:
            print("Name: "+name+" Surname: "+surname+"\n You are a Female")

def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


