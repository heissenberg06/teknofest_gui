from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5.uic import loadUiType
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

ui, _ = loadUiType('sismotekno.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.updateLogo(False) 
        self.initPlot()


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


    def initPlot(self):
        # Create the Matplotlib figure and axis
        fig = Figure()
        ax = fig.add_subplot(111)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y, label='Sine Wave')
        ax.set_title('Example Sine Wave Plot')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.legend()
        ax.grid(True)

        # Create a canvas and add it to your main window
        self.canvas = FigureCanvas(fig)
        self.plotLayout.addWidget(self.canvas)  # Ensure you have a layout called 'plotLayout' in your Qt Designer where the plot should be added

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
