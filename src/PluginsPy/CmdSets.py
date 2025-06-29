#!/usr/bin/env python3

import os
import json

from PluginsPy.MainUI import *
from PluginsPy.Tools import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CmdSets:

    def __init__(self, ui: Ui_MainWindow, MainWindow: QMainWindow):
        self.ui               = ui
        self.gridLayout       = ui.PSGridLayout
        self.MainWindow       = MainWindow

        self.configPath = 'CmdSets'
        self.loadConfig()

    def loadConfig(self):
        self.cmdSets = []

        for f in getFiles(self.configPath):
            configFile = self.configPath + '/' + f
            if os.path.exists(configFile):
                with open(configFile, 'r') as f:
                    self.cmdSets.append(json.load(f))

        print(self.cmdSets)
