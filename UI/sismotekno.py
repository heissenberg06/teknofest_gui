from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5.uic import loadUiType

ui, _ = loadUiType('sismotekno.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.updateLogo(False) 

        self.setStyleSheet("QMainWindow {background-color: #ADD8E6;}")  # Light blue background
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    

        self.pushButton_4.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    

        self.pushButton_5.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    

        self.pushButton_6.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    

        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    

        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #F88379;
                color: white; 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: #D7716A; 
                border-style: inset;
            }
        """)    


    def updateLogo(self, condition):
        red_logo_path = 'white.jpeg'
        black_logo_path = 'red.jpeg'

        if condition:
            pixmap = QPixmap(red_logo_path)
        else:
            pixmap = QPixmap(black_logo_path)

        self.warningLogo.setPixmap(pixmap)  # Replace 'logoLabel' with the actual name of your QLabel
        self.warningLogo.setScaledContents(True)  # Ensure the logo fits the label

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
