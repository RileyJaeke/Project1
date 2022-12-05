from PyQt5.QtWidgets import *
import re
from Conversion import *
from converter import *
from calculate import *
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
        self.shape = 'rectangle'
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendinch.hide()
        self.radendmile.hide()
        self.btnConvert.hide()
        self.lblConversion.hide()
        self.lblOriginal.hide()
        self.lblconvert.hide()
        self.lblcalc.hide()
        self.area = 0.0
        self.conversion = 0.0

    def Calculate(self):
        self.lereq1.text().strip()
        self.lereq2.text().strip()
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
        if  re.search('[a-zA-Z]', self.lereq1.text()) or re.search('[a-zA-Z]',self.lereq2.text()) or self.lereq1.text() == '' or self.lereq2.text() == '':
            self.lereq1.setText("")
            self.lereq2.setText("")
            self.lblcalc.setStyleSheet("Color: rgb(255, 0, 0);")
            self.lblcalc.setText("Measurements need to be numeric")
            self.lblcalc.show()
        elif self.preConvert == '':
            self.lblcalc.setStyleSheet("Color: rgb(255, 0, 0);")
            self.lblcalc.setText("Press a measurement")
            self.lblcalc.show()
        else:
            self.lblcalc.setStyleSheet("Color: rgb(0, 0, 0);")
            req1 = float(self.lereq1.text())
            req2 = float(self.lereq2.text())
            if self.shape == 'rectangle':
                self.area = a_rectangle(req1, req2)
                self.lblcalc.setText(f'{self.area} {self.preConvert}')
                self.lblcalc.show()
            elif self.shape == 'square':
                self.area = a_square(req1)
                self.lblcalc.setText(f'{self.area} {self.preConvert}')
                self.lblcalc.show()
            elif self.shape == 'triangle':
                self.area = a_triangle(req1, req2)
                self.lblcalc.setText(f'{self.area} {self.preConvert}')
                self.lblcalc.show()
            elif self.shape == 'circle':
                self.area = a_circle(req1)
                self.lblcalc.setText(f'{self.area} {self.preConvert}')
                self.lblcalc.show()
            self.btnCalc.hide()
            self.lblreq1.hide()
            self.lblreq2.hide()
            self.lereq1.hide()
            self.lereq2.hide()
            self.radbeginch.hide()
            self.radbegyrd.hide()
            self.radbegft.hide()
            self.radbegmile.hide()
            self.radendinch.show()
            self.radendft.show()
            self.radendmile.show()
            self.radendyrd.show()
            self.lblOriginal.show()
            self.lblcalc.show()
            self.btnConvert.show()
    def Square(self):
        self.lblcalc.setStyleSheet("Color: rgb(0, 0, 0);")
        self.shape = 'square'
        self.lblArea.setText("Area of Square")
        self.lereq1.show()
        self.lblreq1.setText('Enter side length:')
        self.lblreq2.hide()
        self.lereq2.hide()
        self.lereq2.setText("")
        self.lereq1.setText("")
        self.radbeginch.show()
        self.radbegft.show()
        self.radbegmile.show()
        self.radbegyrd.show()
        self.btnConvert.hide()
        self.radendinch.hide()
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendmile.hide()
        self.lblOriginal.hide()
        self.lblConversion.hide()
        self.lblconvert.hide()
        self.btnCalc.show()
        self.lblcalc.hide()
        self.lblreq1.show()

    def Rectangle(self):
        self.lblcalc.setStyleSheet("Color: rgb(0, 0, 0);")
        self.shape = 'rectangle'
        self.lblArea.setText("Area of Rectangle")
        self.lereq1.show()
        self.lblreq2.show()
        self.lereq2.show()
        self.lblreq2.setText("Enter Height:")
        self.lblreq1.setText("Enter Base:")
        self.lereq2.setText("")
        self.lereq1.setText("")
        self.radbeginch.show()
        self.radbegft.show()
        self.radbegmile.show()
        self.radbegyrd.show()
        self.btnConvert.hide()
        self.radendinch.hide()
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendmile.hide()
        self.lblOriginal.hide()
        self.lblConversion.hide()
        self.lblconvert.hide()
        self.btnCalc.show()
        self.lblreq1.show()
        self.lblcalc.hide()
    def Triangle(self):
        self.lblcalc.setStyleSheet("Color: rgb(0, 0, 0);")
        self.shape = "triangle"
        self.lblArea.setText("Area of Triangle")
        self.lereq1.show()
        self.lblreq2.show()
        self.lereq2.show()
        self.lblreq2.setText("Enter Height:")
        self.lblreq1.setText("Enter Base:")
        self.lereq2.setText("")
        self.lereq1.setText("")
        self.radbeginch.show()
        self.radbegft.show()
        self.radbegmile.show()
        self.radbegyrd.show()
        self.btnConvert.hide()
        self.radendinch.hide()
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendmile.hide()
        self.lblOriginal.hide()
        self.lblConversion.hide()
        self.lblconvert.hide()
        self.btnCalc.show()
        self.lblreq1.show()
        self.lblcalc.hide()
    def Circle(self):
        self.lblcalc.setStyleSheet("Color: rgb(0, 0, 0);")
        self.shape = "circle"
        self.lblArea.setText("Area of Circle")
        self.lereq1.show()
        self.lblreq2.hide()
        self.lereq2.hide()
        self.lblreq1.setText("Enter Radius:")
        self.lereq2.setText("")
        self.lereq1.setText("")
        self.radbeginch.show()
        self.radbegft.show()
        self.radbegmile.show()
        self.radbegyrd.show()
        self.btnConvert.hide()
        self.radendinch.hide()
        self.radendft.hide()
        self.radendyrd.hide()
        self.radendmile.hide()
        self.lblOriginal.hide()
        self.lblConversion.hide()
        self.lblconvert.hide()
        self.btnCalc.show()
        self.lblreq1.show()
        self.lblcalc.hide()

    def Convert(self):
        if self.radendinch.isChecked():
            self.lblconvert.setStyleSheet("Color: rgb(0, 0, 0);")
            if self.preConvert == 'in^2':
                self.lblconvert.setText('No Change')
            elif self.preConvert == 'ft^2':
                self.conversion = feet_to_inches(self.area)
                self.lblconvert.setText(f'{self.conversion} in^2')
            elif self.preConvert == 'yd^2':
                self.conversion = yards_to_inches(self.area)
                self.lblconvert.setText(f'{self.conversion} in^2')
            elif self.preConvert == 'mi^2':
                self.conversion = miles_to_inches(self.area)
                self.lblconvert.setText(f'{self.conversion} in^2')
            self.lblConversion.show()
            self.lblconvert.show()
            self.btnConvert.hide()
            self.radendinch.hide()
            self.radendft.hide()
            self.radendyrd.hide()
            self.radendmile.hide()
        elif self.radendft.isChecked():
            if self.preConvert == 'in^2':
                self.lblconvert.setStyleSheet("Color: rgb(0, 0, 0);")
                self.conversion = inches_to_feet(self.area)
                self.lblconvert.setText(f'{self.conversion} ft^2')
            elif self.preConvert == 'ft^2':
                self.lblconvert.setText(f'No Change')
            elif self.preConvert == 'yd^2':
                self.conversion = yards_to_feet(self.area)
                self.lblconvert.setText(f'{self.conversion} ft^2')
            elif self.preConvert == 'mi^2':
                self.conversion = miles_to_feet(self.area)
                self.lblconvert.setText(f'{self.conversion} ft^2')
            self.lblConversion.show()
            self.lblconvert.show()
            self.btnConvert.hide()
            self.radendinch.hide()
            self.radendft.hide()
            self.radendyrd.hide()
            self.radendmile.hide()
        elif self.radendyrd.isChecked():
            self.lblconvert.setStyleSheet("Color: rgb(0, 0, 0);")
            if self.preConvert == 'in^2':
                self.conversion = inches_to_yards(self.area)
                self.lblconvert.setText(f'{self.conversion} yd^2')
            elif self.preConvert == 'ft^2':
                self.conversion = feet_to_yards(self.area)
                self.lblconvert.setText(f'{self.conversion} yd^2')
            elif self.preConvert == 'yd^2':
                self.lblconvert.setText(f'No Change')
            elif self.preConvert == 'mi^2':
                self.conversion = miles_to_yards(self.area)
                self.lblconvert.setText(f'{self.conversion} yd^2')
            self.lblConversion.show()
            self.lblconvert.show()
            self.btnConvert.hide()
            self.radendinch.hide()
            self.radendft.hide()
            self.radendyrd.hide()
            self.radendmile.hide()
        elif self.radendmile.isChecked():
            self.lblconvert.setStyleSheet("Color: rgb(0, 0, 0);")
            if self.preConvert == 'in^2':
                self.conversion = inches_to_miles(self.area)
                self.lblconvert.setText(f'{self.conversion} mi^2')
            elif self.preConvert == 'ft^2':
                self.conversion = feet_to_miles(self.area)
                self.lblconvert.setText(f'{self.conversion} mi^2')
            elif self.preConvert == 'yd^2':
                self.conversion = yards_to_miles(self.area)
                self.lblconvert.setText(f'{self.conversion} mi^2')
            elif self.preConvert == 'mi^2':
                self.lblconvert.setText(f'No Change')
            self.lblConversion.show()
            self.lblconvert.show()
            self.btnConvert.hide()
            self.radendinch.hide()
            self.radendft.hide()
            self.radendyrd.hide()
            self.radendmile.hide()
        else:
            self.lblconvert.setStyleSheet("Color: rgb(255, 0, 0);")
            self.lblconvert.setText("Choose a measurement")
            self.lblconvert.show()







