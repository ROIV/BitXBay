# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Bitco\bitmessageqt\sell.ui'
#
# Created: Sat Jun 28 18:13:59 2014
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

class Ui_Sell(object):
    def setupUi(self, Sell):
        Sell.setObjectName(_fromUtf8("Sell"))
        Sell.resize(860, 571)
        Sell.setMinimumSize(QtCore.QSize(0, 0))
        Sell.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.verticalLayout = QtGui.QVBoxLayout(Sell)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainToolBar = QtGui.QToolBar(Sell)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.verticalLayout.addWidget(self.mainToolBar)
        self.centralWidget = QtGui.QWidget(Sell)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.productdetails = QtGui.QTextEdit(self.centralWidget)
        self.productdetails.setGeometry(QtCore.QRect(10, 250, 831, 191))
        self.productdetails.setObjectName(_fromUtf8("productdetails"))
        self.payandpost = QtGui.QPushButton(self.centralWidget)
        self.payandpost.setGeometry(QtCore.QRect(664, 450, 151, 31))
        self.payandpost.setObjectName(_fromUtf8("payandpost"))
        self.labelsc = QtGui.QLabel(self.centralWidget)
        self.labelsc.setGeometry(QtCore.QRect(20, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelsc.setFont(font)
        self.labelsc.setObjectName(_fromUtf8("labelsc"))
        self.lblscore = QtGui.QLabel(self.centralWidget)
        self.lblscore.setGeometry(QtCore.QRect(120, 15, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblscore.setFont(font)
        self.lblscore.setObjectName(_fromUtf8("lblscore"))
        self.listaddresssell = QtGui.QComboBox(self.centralWidget)
        self.listaddresssell.setGeometry(QtCore.QRect(10, 50, 331, 22))
        self.listaddresssell.setObjectName(_fromUtf8("listaddresssell"))
        self.categorytext = QtGui.QTextEdit(self.centralWidget)
        self.categorytext.setGeometry(QtCore.QRect(10, 180, 831, 31))
        self.categorytext.setObjectName(_fromUtf8("categorytext"))
        self.lab3el_3 = QtGui.QLabel(self.centralWidget)
        self.lab3el_3.setGeometry(QtCore.QRect(10, 160, 831, 21))
        self.lab3el_3.setObjectName(_fromUtf8("lab3el_3"))
        self.la3bel_4 = QtGui.QLabel(self.centralWidget)
        self.la3bel_4.setGeometry(QtCore.QRect(10, 220, 831, 21))
        self.la3bel_4.setObjectName(_fromUtf8("la3bel_4"))
        self.labelprice = QtGui.QLabel(self.centralWidget)
        self.labelprice.setGeometry(QtCore.QRect(20, 442, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelprice.setFont(font)
        self.labelprice.setObjectName(_fromUtf8("labelprice"))
        self.sellprice = QtGui.QDoubleSpinBox(self.centralWidget)
        self.sellprice.setGeometry(QtCore.QRect(80, 459, 71, 21))
        self.sellprice.setDecimals(4)
        self.sellprice.setMinimum(0.0001)
        self.sellprice.setMaximum(9999999.0)
        self.sellprice.setSingleStep(0.01)
        self.sellprice.setObjectName(_fromUtf8("sellprice"))
        self.onlyreted = QtGui.QCheckBox(self.centralWidget)
        self.onlyreted.setGeometry(QtCore.QRect(360, 50, 181, 21))
        self.onlyreted.setObjectName(_fromUtf8("onlyreted"))
        self.xcategory = QtGui.QComboBox(self.centralWidget)
        self.xcategory.setGeometry(QtCore.QRect(500, 100, 281, 22))
        self.xcategory.setObjectName(_fromUtf8("xcategory"))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(570, 70, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.smthwrong = QtGui.QLabel(self.centralWidget)
        self.smthwrong.setGeometry(QtCore.QRect(280, 480, 411, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.smthwrong.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smthwrong.setFont(font)
        self.smthwrong.setText(_fromUtf8(""))
        self.smthwrong.setWordWrap(True)
        self.smthwrong.setObjectName(_fromUtf8("smthwrong"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 450, 121, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 500, 441, 31))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ratinlbl = QtGui.QLabel(self.centralWidget)
        self.ratinlbl.setGeometry(QtCore.QRect(170, 442, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ratinlbl.setFont(font)
        self.ratinlbl.setObjectName(_fromUtf8("ratinlbl"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(300, 459, 62, 21))
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(0.0001)
        self.doubleSpinBox.setMaximum(99999999.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.contactsell = QtGui.QComboBox(self.centralWidget)
        self.contactsell.setGeometry(QtCore.QRect(10, 100, 331, 22))
        self.contactsell.setObjectName(_fromUtf8("contactsell"))
        self.contactsell.addItem(_fromUtf8(""))
        self.label213 = QtGui.QLabel(self.centralWidget)
        self.label213.setGeometry(QtCore.QRect(10, 125, 331, 31))
        self.label213.setObjectName(_fromUtf8("label213"))
        self.newsellcont = QtGui.QPushButton(self.centralWidget)
        self.newsellcont.setGeometry(QtCore.QRect(350, 100, 91, 22))
        self.newsellcont.setObjectName(_fromUtf8("newsellcont"))
        self.label_4231 = QtGui.QLabel(self.centralWidget)
        self.label_4231.setGeometry(QtCore.QRect(10, 75, 421, 21))
        self.label_4231.setObjectName(_fromUtf8("label_4231"))
        self.resend = QtGui.QPushButton(self.centralWidget)
        self.resend.setGeometry(QtCore.QRect(610, 0, 191, 41))
        self.resend.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.resend.setObjectName(_fromUtf8("resend"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(570, 123, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.location = QtGui.QComboBox(self.centralWidget)
        self.location.setGeometry(QtCore.QRect(500, 150, 281, 22))
        self.location.setObjectName(_fromUtf8("location"))
        self.verticalLayout.addWidget(self.centralWidget)

        self.retranslateUi(Sell)
        QtCore.QMetaObject.connectSlotsByName(Sell)

    def retranslateUi(self, Sell):
        Sell.setWindowTitle(_translate("Sell", "Dialog", None))
        self.payandpost.setText(_translate("Sell", "Pay and post", None))
        self.labelsc.setText(_translate("Sell", "Address score:", None))
        self.lblscore.setText(_translate("Sell", "0", None))
        self.lab3el_3.setText(_translate("Sell", "Category. Everyone can create a category. But it is better to use an existing one.", None))
        self.la3bel_4.setText(_translate("Sell", "Product or service details", None))
        self.labelprice.setText(_translate("Sell", "Price:", None))
        self.onlyreted.setText(_translate("Sell", "Show only rated addresses", None))
        self.xcategory.setItemText(0, _translate("Sell", "Goods", None))
        self.xcategory.setItemText(1, _translate("Sell", "Services", None))
        self.xcategory.setItemText(2, _translate("Sell", "Currencies", None))
        self.label.setText(_translate("Sell", "Type of offer", None))
        self.pushButton.setText(_translate("Sell", "Cancel", None))
        self.label_2.setText(_translate("Sell", "For better position pay more.", None))
        self.ratinlbl.setText(_translate("Sell", "Rating payment:", None))
        self.contactsell.setItemText(0, _translate("Sell", "Contact address", None))
        self.label213.setText(_translate("Sell", "Contact address", None))
        self.newsellcont.setText(_translate("Sell", "New contact", None))
        self.label_4231.setText(_translate("Sell", "Bitcoin address for sign message and rating payment.", None))
        self.resend.setText(_translate("Sell", "Resend last offer", None))
        self.label_3.setText(_translate("Sell", "Location", None))
