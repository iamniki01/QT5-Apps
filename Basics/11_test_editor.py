from mailbox import mbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500) #set window size and location.
        self.setWindowTitle("Using text editor ")
        self.UI()
    
    def UI(self):
        self.editor=QTextEdit(self)
        self.editor.move(150,80)
        button= QPushButton("Send",self)
        button.move(330,280)
        button.clicked.connect(self.getValue)
        self.show()
    
    def getValue(self,value):
        text=self.editor.toPlainText()
        print(text)



def main():
    App= QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


