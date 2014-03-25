# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterPixelCountStatDialog
                                 A QGIS plugin
 Statistics Raster Pixel Count By ClassBreak
                             -------------------
        begin                : 2014-03-07
        copyright            : (C) 2014 by Kiwoong Kim/MangoSystem Inc.
        email                : socoooooool@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_rasterpixelcountstat import Ui_RasterPixelCountStat
# create the dialog for zoom to point


class RasterPixelCountStatDialog(QtGui.QDialog, Ui_RasterPixelCountStat):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
		
    def clearResult(self):
        self.txtResult.clear() 

    def setResult(self,value):
        self.txtResult.setText(value)

    def getBreakValues(self):
        return self.txtBreak.text()
