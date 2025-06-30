#!/usr/bin/env python3

import os
import subprocess

from PluginsPy.MainUI import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Perf:

    def __init__(self, ui: Ui_MainWindow, MainWindow: QMainWindow):
        self.ui               = ui
        self.gridLayout       = ui.PSGridLayout
        self.MainWindow       = MainWindow

        self.ui.PerfCapturePushButton.clicked.connect(self.captureClicked)
        self.ui.PerfSystemTypeComboBox.addItems(["android"])
        self.ui.PerfTypeComboBox.addItems(["atrace", "perfetto"])
        self.ui.PerfTimeoutLineEdit.setText("30")

        detectDevice = self.Shell("adb devices".split(" ")).split("\n")
        if (len(detectDevice) > 1):
            print("device connected")

            atraceList = []
            for item in self.Shell("adb shell atrace --list_categories".split(" ")).split("\n"):
                atraceList.append(item.split("-")[0].strip())
            print(atraceList)

            self.fillPSGridLayout(self.ui.PerfTracesGridLayout, atraceList)
        else:
            print("no device connected")

    def Shell(self, cmd):
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out.wait()
        data = out.stdout.read()
        return data.decode('utf-8').strip()

    def fillPSGridLayout(self, gridLayout: QGridLayout, items: list):
        i = 0

        # clear
        item_list = list(range(gridLayout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序

        for i in item_list:
            item = gridLayout.itemAt(i)
            gridLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

        for item in items:
            checkbox = QCheckBox(item)
            gridLayout.addWidget(checkbox, i // 5, i % 5, 1, 1)

            i += 1

    def captureClicked(self):
        print("captureClicked")

        itemStates = {}
        gridLayout = self.ui.PerfTracesGridLayout
        for i in range(gridLayout.rowCount()):
            for j in range(gridLayout.columnCount()):
                item = gridLayout.itemAtPosition(i, j)
                if item != None and isinstance(item.widget(), QCheckBox):
                    if item.widget().isChecked():
                        itemStates[item.widget().text()] = item.widget().isChecked()

        print(itemStates)
