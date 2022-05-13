import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,350,350) #set window size and location.
        self.setWindowTitle("Using CheckBox ")
        self.UI()
    
    def UI(self):
        self.name=QLineEdit(self)
        self.name.setPlaceholderText("Please Enter your name")
        self.name.move(150, 50)
        self.surname=QLineEdit(self)
        self.surname.setPlaceholderText("Please Enter your surname")
        self.surname.move(150,80)
        self.remember=QCheckBox("Remember me",self)
        self.remember.move(150,110)
        button= QPushButton("Submit",self)
        button.move(200,140)
        button.clicked.connect(self.submit)
        self.show()
    
    def submit(self):
        # self.setWindowTitle("Your u name is: "+name+ "Your Password: "+password)
        if(self.remember.isChecked()):
            print("Your name is: "+self.name+ "\nYour Surname: "+self.surname)
        else:
            print("Your name is: "+self.name+ "\nYour Surname: "+self.surname)
    

def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


