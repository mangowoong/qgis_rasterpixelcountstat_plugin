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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load RasterPixelCountStat class from file RasterPixelCountStat
    from rasterpixelcountstat import RasterPixelCountStat
    return RasterPixelCountStat(iface)
