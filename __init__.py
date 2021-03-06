# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LeastCostPath
                                 A QGIS plugin
 Find the least cost path with given cost raster and points
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-12-12
        copyright            : (C) 2018 by FlowMap Group@SESS.PKU
        email                : xurigong@gmail.com
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

__author__ = 'FlowMap Group@SESS.PKU'
__date__ = '2018-12-12'
__copyright__ = '(C) 2018 by FlowMap Group@SESS.PKU'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LeastCostPath class from file LeastCostPath.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .least_cost_path import LeastCostPathPlugin
    return LeastCostPathPlugin()
