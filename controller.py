from PyQt5.QtWidgets import *
import re
from Conversion import *
import math


class Controller(QMainWindow, Ui_mainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnCalc.clicked.connect(lambda: self.Calculate())
        self.btnConvert.clicked.connect(lambda: self.Convert())
        self.actionSquare.triggered.connect(lambda: self.Square())
        self.actionRectangle.triggered.connect(lambda: self.Rectangle)
        self.actionTriangle.triggered.connect(lambda: self.Triangle)
        self.actionCircle.triggered.connect(lambda: self.Circle)

        self.label = ""
        self.lblcalc.hide()
        self.lblresult.hide()

    def Calculate(self):
        self.lblcalc.setText("bruh")
    def Square(self):
        self.lblArea.setText("Area of Square")
        self.lblreq2.hide()
        self.lereq2.hide()
        self.lblreq1.setText("Enter Side Length:")

