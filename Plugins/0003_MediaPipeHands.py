#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: ZengjfOS
Date: 2024-09-29 09:02:56
License: MIT License
"""

import datetime

from PluginsPy.VisualLogPlot import VisualLogPlot

import VisualLog.LogParser as LogParser
import VisualLog.MatplotlibZoom as MatplotlibZoom

import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.axes import Axes

class MediaPipeHands:

    """
    @data(input/hands.txt): None
    """

    def __init__(self, kwargs):

        print("MediaPipeHands args:")
        print(kwargs)

        data = kwargs["data"]

        parseFilenames = [data]
        regex = [
            'x\s*=\s*([-]?\d.\d+),\s*y\s*=\s*([-]?\d.\d+),\s*z\s*=\s*([-]?\d.\d+)'
            ]
        kwargs["lineInfosFiles"], filenames = LogParser.logFileParser(
                parseFilenames,
                regex,
            )

        plotType             = "3D"
        kwargs["xAxis"]      = [0]
        kwargs["dataIndex"]  = [0, 1, 2]

        if plotType == "normal":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "key":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "keyLoop":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyLoopShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "3D":
            MatplotlibZoom.Show(callback=VisualLogPlot.default3DShowCallback, rows = 1, cols = 1, d3=True, args=kwargs)
        else:
            print("unsupport plot type")
