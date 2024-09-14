#!/usr/bin/env python3

import os

from PluginsPy.TemplateUI import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Template:

    def __init__(self):
        self.templateDiag = QDialog()
        self.templateUI = Ui_TemplatUI()
        self.templateUI.setupUi(self.templateDiag)

        size = self.templateDiag.geometry()
        self.templateDiag.setFixedSize(size.width(), size.height())

        self.templateDiag.setWindowIcon(QIcon(os.path.dirname(__file__) + "/assets/images/icon.png"))

        self.templateUI.TLVisualLogPushButton.clicked.connect(self.TLVisualLogClick)

        self.templateDiag.show()

    def TLVisualLogClick(self):
        print("TLVisualLogClick")
