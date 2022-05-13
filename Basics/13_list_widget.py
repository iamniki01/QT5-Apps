from mailbox import mbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using List Widget ")
        self.UI()
    
    def UI(self):
        self.addRecord=QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget =QListWidget(self)
        self.listWidget.move(100,80)


        proLang = ["C", "C#", "C++", "Python", "Java", "PHP"]
        self.listWidget.addItems(proLang)

        btnAdd=QPushButton("Add",self)
        btnAdd.move(360,80)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete=QPushButton("Delete",self)
        btnDelete.move(360,110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet=QPushButton("GetItem",self)
        btnGet.move(360,140)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll=QPushButton("Delete All",self)
        btnDeleteAll.move(360,170)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)
        self.show()
    
    def funcAdd(self):
        val=self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")
    
    def funcDelete(self):
        id=self.listWidget.currentRow()
        self.listWidget.takeItem(id)

    def funcGet(self):
        value=self.listWidget.currentItem().text()
        print(value)

    def funcDeleteAll(self):
        self.listWidget.clear()


def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


