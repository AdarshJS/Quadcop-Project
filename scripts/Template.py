# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Template.ui'
#
# Created: Fri Jan  8 12:59:59 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1310, 740)
        self.Attitude_Name = QtGui.QLabel(Form)
        self.Attitude_Name.setGeometry(QtCore.QRect(850, 230, 211, 20))
        self.Attitude_Name.setAcceptDrops(False)
        self.Attitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Attitude_Name.setObjectName(_fromUtf8("Attitude_Name"))
        self.Heading_Name = QtGui.QLabel(Form)
        self.Heading_Name.setGeometry(QtCore.QRect(1080, 230, 211, 20))
        self.Heading_Name.setAcceptDrops(False)
        self.Heading_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Heading_Name.setObjectName(_fromUtf8("Heading_Name"))
        self.Turn_Name = QtGui.QLabel(Form)
        self.Turn_Name.setGeometry(QtCore.QRect(850, 360, 211, 20))
        self.Turn_Name.setAcceptDrops(False)
        self.Turn_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Turn_Name.setObjectName(_fromUtf8("Turn_Name"))
        self.Throttle_Name = QtGui.QLabel(Form)
        self.Throttle_Name.setGeometry(QtCore.QRect(1080, 360, 211, 20))
        self.Throttle_Name.setAcceptDrops(False)
        self.Throttle_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Throttle_Name.setObjectName(_fromUtf8("Throttle_Name"))
        self.Battery = QtGui.QProgressBar(Form)
        self.Battery.setGeometry(QtCore.QRect(1210, 422, 61, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Battery.setFont(font)
        self.Battery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Battery.setProperty("value", 50)
        self.Battery.setTextVisible(True)
        self.Battery.setOrientation(QtCore.Qt.Vertical)
        self.Battery.setInvertedAppearance(False)
        self.Battery.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.Battery.setObjectName(_fromUtf8("Battery"))
        self.Battery_Name = QtGui.QLabel(Form)
        self.Battery_Name.setGeometry(QtCore.QRect(1200, 640, 91, 20))
        self.Battery_Name.setAcceptDrops(False)
        self.Battery_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Battery_Name.setObjectName(_fromUtf8("Battery_Name"))
        self.Throttle = QtGui.QProgressBar(Form)
        self.Throttle.setGeometry(QtCore.QRect(1080, 290, 211, 51))
        self.Throttle.setProperty("value", 24)
        self.Throttle.setObjectName(_fromUtf8("Throttle"))
        self.EXIT = QtGui.QPushButton(Form)
        self.EXIT.setGeometry(QtCore.QRect(1190, 690, 99, 27))
        self.EXIT.setObjectName(_fromUtf8("EXIT"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 650, 209, 60))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.DATA_1 = QtGui.QVBoxLayout(self.layoutWidget)
        self.DATA_1.setMargin(0)
        self.DATA_1.setObjectName(_fromUtf8("DATA_1"))
        self.Altitude = QtGui.QHBoxLayout()
        self.Altitude.setObjectName(_fromUtf8("Altitude"))
        self.Altitude_Name = QtGui.QLabel(self.layoutWidget)
        self.Altitude_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Altitude_Name.setFont(font)
        self.Altitude_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Altitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitude_Name.setObjectName(_fromUtf8("Altitude_Name"))
        self.Altitude.addWidget(self.Altitude_Name)
        self.Altitude_LCD = QtGui.QLCDNumber(self.layoutWidget)
        self.Altitude_LCD.setEnabled(True)
        self.Altitude_LCD.setAutoFillBackground(True)
        self.Altitude_LCD.setSmallDecimalPoint(False)
        self.Altitude_LCD.setDigitCount(5)
        self.Altitude_LCD.setMode(QtGui.QLCDNumber.Dec)
        self.Altitude_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Altitude_LCD.setObjectName(_fromUtf8("Altitude_LCD"))
        self.Altitude.addWidget(self.Altitude_LCD)
        self.Altitude_Units = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Altitude_Units.setFont(font)
        self.Altitude_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitude_Units.setObjectName(_fromUtf8("Altitude_Units"))
        self.Altitude.addWidget(self.Altitude_Units)
        self.DATA_1.addLayout(self.Altitude)
        self.Pressure = QtGui.QHBoxLayout()
        self.Pressure.setObjectName(_fromUtf8("Pressure"))
        self.Pressure_Name = QtGui.QLabel(self.layoutWidget)
        self.Pressure_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Pressure_Name.setFont(font)
        self.Pressure_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Pressure_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure_Name.setObjectName(_fromUtf8("Pressure_Name"))
        self.Pressure.addWidget(self.Pressure_Name)
        self.Pressure_LCD = QtGui.QLCDNumber(self.layoutWidget)
        self.Pressure_LCD.setEnabled(True)
        self.Pressure_LCD.setAutoFillBackground(True)
        self.Pressure_LCD.setSmallDecimalPoint(False)
        self.Pressure_LCD.setDigitCount(5)
        self.Pressure_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Pressure_LCD.setObjectName(_fromUtf8("Pressure_LCD"))
        self.Pressure.addWidget(self.Pressure_LCD)
        self.Pressure_Units = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Pressure_Units.setFont(font)
        self.Pressure_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure_Units.setObjectName(_fromUtf8("Pressure_Units"))
        self.Pressure.addWidget(self.Pressure_Units)
        self.DATA_1.addLayout(self.Pressure)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(880, 687, 258, 34))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.MODE_DISPLAY = QtGui.QHBoxLayout(self.layoutWidget1)
        self.MODE_DISPLAY.setMargin(0)
        self.MODE_DISPLAY.setObjectName(_fromUtf8("MODE_DISPLAY"))
        self.Mode_Name = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mode_Name.setFont(font)
        self.Mode_Name.setObjectName(_fromUtf8("Mode_Name"))
        self.MODE_DISPLAY.addWidget(self.Mode_Name)
        self.Display = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Display.setFont(font)
        self.Display.setObjectName(_fromUtf8("Display"))
        self.MODE_DISPLAY.addWidget(self.Display)
        self.Test = QtGui.QSlider(Form)
        self.Test.setGeometry(QtCore.QRect(1170, 440, 41, 191))
        self.Test.setOrientation(QtCore.Qt.Vertical)
        self.Test.setObjectName(_fromUtf8("Test"))
        self.Frame = QtGui.QLabel(Form)
        self.Frame.setGeometry(QtCore.QRect(10, 10, 832, 624))
        self.Frame.setText(_fromUtf8(""))
        self.Frame.setObjectName(_fromUtf8("Frame"))
        self.Attitude_Image = QtGui.QLabel(Form)
        self.Attitude_Image.setGeometry(QtCore.QRect(850, 10, 210, 210))
        self.Attitude_Image.setText(_fromUtf8(""))
        self.Attitude_Image.setObjectName(_fromUtf8("Attitude_Image"))
        self.Heading_Image = QtGui.QLabel(Form)
        self.Heading_Image.setGeometry(QtCore.QRect(1080, 10, 210, 210))
        self.Heading_Image.setText(_fromUtf8(""))
        self.Heading_Image.setObjectName(_fromUtf8("Heading_Image"))
        self.Turn_Image = QtGui.QLabel(Form)
        self.Turn_Image.setGeometry(QtCore.QRect(850, 290, 210, 53))
        self.Turn_Image.setText(_fromUtf8(""))
        self.Turn_Image.setObjectName(_fromUtf8("Turn_Image"))
        self.Frame_Zoom = QtGui.QLabel(Form)
        self.Frame_Zoom.setGeometry(QtCore.QRect(850, 420, 320, 240))
        self.Frame_Zoom.setText(_fromUtf8(""))
        self.Frame_Zoom.setObjectName(_fromUtf8("Frame_Zoom"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(41, 643, 174, 88))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.GPS_Name = QtGui.QLabel(self.widget)
        self.GPS_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.GPS_Name.setFont(font)
        self.GPS_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPS_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.GPS_Name.setObjectName(_fromUtf8("GPS_Name"))
        self.verticalLayout.addWidget(self.GPS_Name)
        self.Latitude = QtGui.QHBoxLayout()
        self.Latitude.setObjectName(_fromUtf8("Latitude"))
        self.Latitude_Name = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Latitude_Name.setFont(font)
        self.Latitude_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Latitude_Name.setObjectName(_fromUtf8("Latitude_Name"))
        self.Latitude.addWidget(self.Latitude_Name)
        self.Latitude_LCD = QtGui.QLCDNumber(self.widget)
        self.Latitude_LCD.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Latitude_LCD.setFont(font)
        self.Latitude_LCD.setAutoFillBackground(True)
        self.Latitude_LCD.setSmallDecimalPoint(False)
        self.Latitude_LCD.setDigitCount(11)
        self.Latitude_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Latitude_LCD.setProperty("intValue", 0)
        self.Latitude_LCD.setObjectName(_fromUtf8("Latitude_LCD"))
        self.Latitude.addWidget(self.Latitude_LCD)
        self.verticalLayout.addLayout(self.Latitude)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Longitude_Name = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Longitude_Name.setFont(font)
        self.Longitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Longitude_Name.setObjectName(_fromUtf8("Longitude_Name"))
        self.horizontalLayout.addWidget(self.Longitude_Name)
        self.Lonigitude_LCD = QtGui.QLCDNumber(self.widget)
        self.Lonigitude_LCD.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Lonigitude_LCD.setFont(font)
        self.Lonigitude_LCD.setAutoFillBackground(True)
        self.Lonigitude_LCD.setFrameShadow(QtGui.QFrame.Raised)
        self.Lonigitude_LCD.setSmallDecimalPoint(False)
        self.Lonigitude_LCD.setDigitCount(11)
        self.Lonigitude_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Lonigitude_LCD.setProperty("value", 0.0)
        self.Lonigitude_LCD.setProperty("intValue", 0)
        self.Lonigitude_LCD.setObjectName(_fromUtf8("Lonigitude_LCD"))
        self.horizontalLayout.addWidget(self.Lonigitude_LCD)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(740, 650, 65, 66))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.Zoom = QtGui.QVBoxLayout(self.widget1)
        self.Zoom.setMargin(0)
        self.Zoom.setObjectName(_fromUtf8("Zoom"))
        self.Altitude_Name_2 = QtGui.QLabel(self.widget1)
        self.Altitude_Name_2.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Altitude_Name_2.setFont(font)
        self.Altitude_Name_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Altitude_Name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitude_Name_2.setObjectName(_fromUtf8("Altitude_Name_2"))
        self.Zoom.addWidget(self.Altitude_Name_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Pressure_LCD_2 = QtGui.QLCDNumber(self.widget1)
        self.Pressure_LCD_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Pressure_LCD_2.setFont(font)
        self.Pressure_LCD_2.setAutoFillBackground(True)
        self.Pressure_LCD_2.setSmallDecimalPoint(False)
        self.Pressure_LCD_2.setDigitCount(2)
        self.Pressure_LCD_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Pressure_LCD_2.setObjectName(_fromUtf8("Pressure_LCD_2"))
        self.horizontalLayout_2.addWidget(self.Pressure_LCD_2)
        self.X = QtGui.QLabel(self.widget1)
        self.X.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.X.setFont(font)
        self.X.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X.setAlignment(QtCore.Qt.AlignCenter)
        self.X.setObjectName(_fromUtf8("X"))
        self.horizontalLayout_2.addWidget(self.X)
        self.Zoom.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Test, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Battery.setValue)
        QtCore.QObject.connect(self.Test, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Altitude_LCD.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Attitude_Name.setText(_translate("Form", "Attitude Indicator", None))
        self.Heading_Name.setText(_translate("Form", "Heading Indicator", None))
        self.Turn_Name.setText(_translate("Form", "Turn Indicator", None))
        self.Throttle_Name.setText(_translate("Form", "Throttle Level", None))
        self.Battery_Name.setText(_translate("Form", "Battery", None))
        self.EXIT.setText(_translate("Form", "EXIT", None))
        self.Altitude_Name.setText(_translate("Form", "Altitude :", None))
        self.Altitude_Units.setText(_translate("Form", "ft", None))
        self.Pressure_Name.setText(_translate("Form", "Pressure :", None))
        self.Pressure_Units.setText(_translate("Form", "bar", None))
        self.Mode_Name.setText(_translate("Form", "MODE : ", None))
        self.Display.setText(_translate("Form", "AUTOMATIC", None))
        self.GPS_Name.setText(_translate("Form", "GPS", None))
        self.Latitude_Name.setText(_translate("Form", "Lat :", None))
        self.Longitude_Name.setText(_translate("Form", "Long :", None))
        self.Altitude_Name_2.setText(_translate("Form", "Zoom", None))
        self.X.setText(_translate("Form", "X", None))
