#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: zengjf
Date: 2024-10-01 11:14:47
License: MIT License
"""

import datetime

from PluginsPy.VisualLogPlot import VisualLogPlot

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
        kwargs["lineInfosFiles"], filenames = VisualLogPlot.parseData(
            parseFilenames,
            regex,
            )

        kwargs["plotType"]   = "keyLoop"
        kwargs["xAxis"]      = [1]
        kwargs["dataIndex"]  = [0]

        VisualLogPlot.show(kwargs)
