import sys  
from PyQt5.QtWidgets import * 
from PyQt5 import  uic  
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl
from PyQt5 import *
import webbrowser

class Panora(QMainWindow):
    def __init__(self):                                                            
        super(Panora, self).__init__()                                 
        uic.loadUi("untitled.ui", self)
        self.all_image_button.clicked.connect(self.select_all)
        self.stop_button.clicked.connect(self.stop)        
        self.start2.clicked.connect(self.start)
        self.logo.clicked.connect(self.technomind)

    def select_all(self):
        self.pushButton_1.setChecked(True)   
        self.pushButton_2.setChecked(True) 
        self.pushButton_3.setChecked(True) 
        self.pushButton_4.setChecked(True) 
        self.pushButton_5.setChecked(True) 
        self.pushButton_6.setChecked(True) 
        self.pushButton_7.setChecked(True) 
        self.pushButton_8.setChecked(True) 
        self.pushButton_9.setChecked(True) 
        self.pushButton_10.setChecked(True) 
        self.pushButton_11.setChecked(True) 
        self.pushButton_12.setChecked(True) 
        self.pushButton_13.setChecked(True) 
        self.pushButton_14.setChecked(True) 
        self.pushButton_15.setChecked(True) 
        self.pushButton_16.setChecked(True) 

    def stop(self):
        pass
          
    def technomind(self):
        webbrowser.open("http://www.technomind.com.tr")
 
    def start(self):
        pass
             
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Panora()
    widget.show()
    sys.exit(app.exec_())
  
