#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: zengjf
Date: 2024-10-01 11:14:47
License: MIT License
"""

import datetime

from PluginsPy.VisualLogPlot import VisualLogPlot

import VisualLog.LogParser as LogParser
import VisualLog.MatplotlibZoom as MatplotlibZoom

import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.axes import Axes

class KernelKeyLoop:

    """
    @first(input/kernel_1.txt): None
    @second(input/kernel_2.txt): None
    """

    def __init__(self, kwargs):

        print("KernelKeyLoop args:")
        print(kwargs)

        first = kwargs["first"]
        second = kwargs["second"]

        parseFilenames = [first, second]
        regex = [
            '(\d*\.\d*)\s+:.*(Kernel_init_done)',
            '(\d*\.\d*)\s+:.*(INIT:late-init)',
            '(\d*\.\d*)\s+:.*(vold:fbeEnable:START)',
            '(\d*\.\d*)\s+:.*(INIT:post-fs-data)'
            ]
        kwargs["lineInfosFiles"], filenames = LogParser.logFileParser(
            parseFilenames,
            regex,
            )

        plotType             = "keyLoop"
        kwargs["xAxis"]      = [1]
        kwargs["dataIndex"]  = [0]

        if plotType == "normal":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "key":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "keyLoop":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyLoopShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "keyDiff":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyDiffShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "3D":
            MatplotlibZoom.Show(callback=VisualLogPlot.default3DShowCallback, rows = 1, cols = 1, d3=True, args=kwargs)
        else:
            print("unsupport plot type")
