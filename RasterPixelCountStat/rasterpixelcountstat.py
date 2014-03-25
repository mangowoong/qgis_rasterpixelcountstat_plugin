# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterPixelCountStat
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
from osgeo import gdal
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from rasterpixelcountstatdialog import RasterPixelCountStatDialog
import os.path

class RasterPixelCountStat:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
		
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'rasterpixelcountstat_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = RasterPixelCountStatDialog()
		
		# Always on top
        self.dlg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/rasterpixelcountstat/icon.png"),
            u"RasterPixelCountStat", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Statistics Raster Pixel Count By ClassBreak", self.action)
		
        result = QObject.connect(self.canvas, SIGNAL("layersChanged ()"), self.handleLayersChanged)
        QObject.connect(self.dlg.btnCal, SIGNAL("clicked ()"), self.CalculateStart)

    def getLayerByName(self, layer_name):
	    for layer in self.canvas.layers():
		    if (layer.name() == layer_name):
			    return layer

    def handleLayersChanged(self):
	    self.dlg.cboLayer.clear()
	    for layer in self.canvas.layers():
	        self.dlg.cboLayer.addItem(layer.name())
			
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Statistics Raster Pixel Count By ClassBreak", self.action)
        self.iface.removeToolBarIcon(self.action)

    def CalculateStart(self):
        current_layer = self.getLayerByName(self.dlg.cboLayer.currentText())
			
        if current_layer is not None:
            if current_layer.type() == QgsMapLayer.VectorLayer:
                QMessageBox.information(self.iface.mainWindow(), "Information", u"Selected Layer is not Raster Layer...")
            elif current_layer.type() == QgsMapLayer.RasterLayer:
				curDataProvider = current_layer.dataProvider()
				rasterInterface = curDataProvider.clone()
				rasterbandStat = rasterInterface.bandStatistics(1, QgsRasterBandStats.All, curDataProvider.extent(), 0)
					
				gdaldata = gdal.Open(unicode(curDataProvider.dataSourceUri()))
					
				if gdaldata is not None:
					self.dlg.clearResult()
						
					# Default Stat Value
					dNoDataValue = curDataProvider.srcNoDataValue(1)
					dTotal = rasterbandStat.elementCount
					dMin = rasterbandStat.minimumValue
					dMax = rasterbandStat.maximumValue
					dSum = rasterbandStat.sum
					dMean = rasterbandStat.mean
					dStdDev = rasterbandStat.stdDev
					dPixelSizeX = current_layer.rasterUnitsPerPixelX()
					dPixelSizeY = current_layer.rasterUnitsPerPixelY()
					
					# calculate Count by breaks (Loop)
					sBreakStr = self.dlg.getBreakValues()
					sBreakStr = sBreakStr.replace(' ', '')
					lstBreak = sBreakStr.split(',')
					
					valDicCellCount = {}
						
					for i in lstBreak:
					    valDicCellCount[i] = 0
						
					# store Max..
					valDicCellCount['max'] = 0

					xSize = gdaldata.RasterXSize
					ySize = gdaldata.RasterYSize
					raster = gdaldata.ReadAsArray()
					noDataCnt = 0
					
					for col in range(xSize):
					    for row in range(ySize):
						    dCellValue = raster[row, col]
							
						    if (dCellValue == dNoDataValue):
							    noDataCnt += 1
							    continue
							
						    try:
						        bIsMax = True
									
						        for breakVal in lstBreak:
						            if (dCellValue <= float(breakVal)):
						                valDicCellCount[breakVal] += 1
						                bIsMax = False
						                break
											
						        if bIsMax == True:
						            valDicCellCount['max'] += 1
						    except:
								continue
									
					# report resultStr
					resultStr = u"Raster File : " + curDataProvider.dataSourceUri() + "\n\n"
					resultStr = resultStr + u"*** Basic Statistics ***" + "\n"
					resultStr = resultStr + (u"- Total Pixel Count = %s \n" % dTotal)
					resultStr = resultStr + (u"- Min Value = %s \n" % dMin)
					resultStr = resultStr + (u"- Max Value = %s \n" % dMax)
					resultStr = resultStr + (u"- Sum Value = %s \n" % dSum)
					resultStr = resultStr + (u"- Mean Value = %s \n" % dMean)
					resultStr = resultStr + (u"- StdDev Value = %s \n" % dStdDev)
					resultStr = resultStr + (u"- NoData Value = %s \n" % dNoDataValue)
					resultStr = resultStr + (u"- PixelSize X = %s \n" % dPixelSizeX)
					resultStr = resultStr + (u"- PixelSize Y = %s \n\n" % dPixelSizeY)
					
					resultStr = resultStr + u"*** Break Count ***\n"
					resultStr = resultStr + u"Break, Count, Area(PixelSize X * Y * Count)\n"
					
					sTempStr = u"min"
					
					for breakValStr in lstBreak:
					    dAreaVal = float(valDicCellCount[breakValStr]) * (float(dPixelSizeX) * float(dPixelSizeY))
					    resultStr = resultStr + (u"%s ~ %s, %s, %s \n" % (sTempStr, breakValStr, valDicCellCount[breakValStr], dAreaVal))
					    sTempStr = breakValStr
				    
					# Max
					dAreaVal = float(valDicCellCount['max']) * (float(dPixelSizeX) * float(dPixelSizeY))
					resultStr = resultStr + (u"%s ~ max, %s, %s \n" % (sTempStr, valDicCellCount['max'], dAreaVal))

					# Nodata
					dAreaVal = float(noDataCnt) * (float(dPixelSizeX) * float(dPixelSizeY))
					resultStr = resultStr + (u"NoData, %s, %s \n\n" % (noDataCnt, dAreaVal))
					resultStr = resultStr + u"*** End of Result ***"
					
					self.dlg.setResult(resultStr)
						
					QMessageBox.information(self.iface.mainWindow(), "Information", u"Calculate Complete...")
				    
				else:
				    QMessageBox.information(self.iface.mainWindow(), "Information", u"Raster Layer Not Open In GDAL...")
				    # self.dlg.setTextBrowser(u"Value = %s" % raster_value) 
            else:
                QMessageBox.information(self.iface.mainWindow(), "Information", u"Selected Layer is not Raster Layer...")
        else:
            QMessageBox.information(self.iface.mainWindow(), "Information", u"Targer Layer is not Selected...")
	
        self.dlg.open()
		
    # run method that performs all the real work
    def run(self):
        self.handleLayersChanged()
		
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass