import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using Comboboxes ")
        self.UI()
    
    def UI(self):
        self.combo=QComboBox(self)
        self.combo.move(150,150)
        button= QPushButton("Save",self)
        button.move(150,130)
        self.combo.addItem("Python") #only string is valid
        self.combo.addItems(["C", "C#", "C++", "Python", "Java", "PHP"])
        button.clicked.connect(self.getValues)
        additionCombos = ["perl", "go", "Javascript", "Ruby"]
        
        for name in additionCombos:
            self.combo.addItem(name)
        self.show()


    
    def getValues(self):
        # self.setWindowTitle("Your u name is: "+name+ "Your Password: "+password)
        values=self.combo.currentText()
        print(values)
    

def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


