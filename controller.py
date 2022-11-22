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
        self.actionRectangle.triggered.connect(lambda: self.Rectangle())
        self.actionTriangle.triggered.connect(lambda: self.Triangle())
        self.actionCircle.triggered.connect(lambda: self.Circle())

        """
        PreConvert will help us determine what measurement we're using in if statements.
        I.E. if we chose the inch button, label will equal "
        """
        self.preConvert = ""
        """
        shape will help us determine what area calculation we're using in if statements. SO when we click a shape
        shape will equal which one we press I.E. if shape = square, we use the square area calc
        """
        self.shape = ''
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendinch.hide()
        self.radendmile.hide()
        self.btnConvert.hide()
        self.lblConversion.hide()
        self.lblOriginal.hide()
        self.lblconvert.hide()
        self.lblcalc.hide()
        #This will be a method
        self.calculation = ""

    def Calculate(self):
        if self.lereq2.isHidden():
            self.lereq2.setText("0")
        self.lblcalc.setText("")
        if self.radbeginch.isChecked():
            self.preConvert = "in^2"
        elif self.radbegft.isChecked():
            self.preConvert = "ft^2"
        elif self.radbegyrd.isChecked():
            self.preConvert = "yd^2"
        elif self.radbegmile.isChecked():
            self.preConvert = "mi^2"
        else:
            self.lblcalc.setText("Press a measurement")
        if  re.search('[a-zA-Z]', self.lereq1.text()) or re.search('[a-zA-Z]',self.lereq2.text()) or self.lereq1.text() == '' or self.lereq2.text() == '':
            self.lereq1.setText("")
            self.lereq2.setText("")
            self.lblcalc.setText('Measurements need to be numeric')
        self.lblcalc.show()
    def Square(self):
        self.shape = 'square'
        self.lblArea.setText("Area of Square")
        self.lblreq2.hide()
        self.lereq2.hide()
        self.lereq2.setText("")
        self.lereq1.setText("")
    def Rectangle(self):
        self.shape = 'rectangle'
        self.lblArea.setText("Area of Rectangle")
        self.lblreq2.show()
        self.lereq2.show()
        self.lblreq2.setText("Enter Height")
        self.lblreq1.setText("Enter Base")
        self.lereq2.setText("")
        self.lereq1.setText("")
    def Triangle(self):
        self.shape = "triangle"
        self.lblArea.setText("Area of Triangle")
        self.lblreq2.show()
        self.lereq2.show()
        self.lblreq2.setText("Enter Height")
        self.lblreq1.setText("Enter Base")
        self.lereq2.setText("")
        self.lereq1.setText("")
    def Circle(self):
        self.shape = "circle"
        self.lblArea.setText("Area of Circle")
        self.lblreq2.hide()
        self.lereq2.hide()
        self.lblreq1.setText("Enter Radius:")
        self.lereq2.setText("")
        self.lereq1.setText("")

