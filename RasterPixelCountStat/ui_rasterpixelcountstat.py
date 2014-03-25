# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rasterpixelcountstat.ui'
#
# Created: Mon Mar 10 12:11:12 2014
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_RasterPixelCountStat(object):
    def setupUi(self, RasterPixelCountStat):
        RasterPixelCountStat.setObjectName(_fromUtf8("RasterPixelCountStat"))
        RasterPixelCountStat.resize(416, 603)
        self.gridLayout = QtGui.QGridLayout(RasterPixelCountStat)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(RasterPixelCountStat)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_4 = QtGui.QLabel(RasterPixelCountStat)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 3)
        self.txtBreak = QtGui.QLineEdit(RasterPixelCountStat)
        self.txtBreak.setObjectName(_fromUtf8("txtBreak"))
        self.gridLayout.addWidget(self.txtBreak, 3, 0, 1, 3)
        self.btnCal = QtGui.QPushButton(RasterPixelCountStat)
        self.btnCal.setObjectName(_fromUtf8("btnCal"))
        self.gridLayout.addWidget(self.btnCal, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(RasterPixelCountStat)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 2)
        self.txtResult = QtGui.QTextBrowser(RasterPixelCountStat)
        self.txtResult.setObjectName(_fromUtf8("txtResult"))
        self.gridLayout.addWidget(self.txtResult, 6, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(RasterPixelCountStat)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 3)
        self.label = QtGui.QLabel(RasterPixelCountStat)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cboLayer = QtGui.QComboBox(RasterPixelCountStat)
        self.cboLayer.setObjectName(_fromUtf8("cboLayer"))
        self.gridLayout.addWidget(self.cboLayer, 0, 1, 1, 2)

        self.retranslateUi(RasterPixelCountStat)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RasterPixelCountStat.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RasterPixelCountStat.reject)
        QtCore.QObject.connect(self.btnCal, QtCore.SIGNAL(_fromUtf8("clicked()")), RasterPixelCountStat.accept)
        QtCore.QMetaObject.connectSlotsByName(RasterPixelCountStat)

    def retranslateUi(self, RasterPixelCountStat):
        RasterPixelCountStat.setWindowTitle(_translate("RasterPixelCountStat", "RasterPixelCountStat", None))
        self.label_2.setText(_translate("RasterPixelCountStat", "- Input Break Values.. Seperate By Comma(,)", None))
        self.label_4.setText(_translate("RasterPixelCountStat", "ex> input 10, 20, 30, 40 then MIN~10, 10 ~ 20, ... , 40 ~ MAX", None))
        self.btnCal.setText(_translate("RasterPixelCountStat", "Calculate", None))
        self.label_3.setText(_translate("RasterPixelCountStat", "** Statistics Result... **", None))
        self.label.setText(_translate("RasterPixelCountStat", "- Select Raster Layer", None))

