# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os
import time

from PyQt6 import QtCore, QtGui, QtWidgets

from vsensebox.gui.uitools import CUR_DIR, UI_TMP
from vsensebox.config.configurator import IN_ROOT_DIR, IN_CONFIG_DIR
from vsensebox.config.confighelper import getCFGDict, dumpDocDict
from vsensebox.utils.about import getVersionString
from vsensebox.utils.commontools import joinFPathFull, normalizePathFDS, isExist, getAncestorDir
from vsensebox.utils.logtools import add_warning_log


class Ui_CFGLoader(object):

    def setupUi(self, CFGLoader):
        CFGLoader.setObjectName("CFGLoader")
        CFGLoader.resize(560, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CFGLoader.sizePolicy().hasHeightForWidth())
        CFGLoader.setSizePolicy(sizePolicy)
        CFGLoader.setMinimumSize(QtCore.QSize(560, 600))
        CFGLoader.setMaximumSize(QtCore.QSize(560, 600))
        self.line2 = QtWidgets.QFrame(parent=CFGLoader)
        self.line2.setGeometry(QtCore.QRect(10, 540, 541, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QFrame(parent=CFGLoader)
        self.line1.setGeometry(QtCore.QRect(10, 55, 541, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        self.line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line1.setObjectName("line1")
        self.save_pushButton = QtWidgets.QPushButton(parent=CFGLoader)
        self.save_pushButton.setGeometry(QtCore.QRect(475, 561, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_pushButton.sizePolicy().hasHeightForWidth())
        self.save_pushButton.setSizePolicy(sizePolicy)
        self.save_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.save_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(parent=CFGLoader)
        self.cancel_pushButton.setGeometry(QtCore.QRect(395, 561, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.cancel_pushButton.setSizePolicy(sizePolicy)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.cancel_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.par_label = QtWidgets.QLabel(parent=CFGLoader)
        self.par_label.setGeometry(QtCore.QRect(10, 68, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.par_label.setFont(font)
        self.par_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.par_label.setObjectName("par_label")
        self.value_label = QtWidgets.QLabel(parent=CFGLoader)
        self.value_label.setGeometry(QtCore.QRect(130, 68, 341, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.value_label.setFont(font)
        self.value_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.value_label.setObjectName("value_label")
        self.file_label = QtWidgets.QLabel(parent=CFGLoader)
        self.file_label.setGeometry(QtCore.QRect(470, 68, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.file_label.setFont(font)
        self.file_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.file_label.setObjectName("file_label")
        self.saveas_pushButton = QtWidgets.QPushButton(parent=CFGLoader)
        self.saveas_pushButton.setGeometry(QtCore.QRect(90, 560, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveas_pushButton.sizePolicy().hasHeightForWidth())
        self.saveas_pushButton.setSizePolicy(sizePolicy)
        self.saveas_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.saveas_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.saveas_pushButton.setObjectName("saveas_pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=CFGLoader)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 541, 446))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.par01_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par01_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par01_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par01_value_lineEdit.setObjectName("par01_value_lineEdit")
        self.gridLayout.addWidget(self.par01_value_lineEdit, 0, 1, 1, 1)
        self.par01_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par01_pushButton.sizePolicy().hasHeightForWidth())
        self.par01_pushButton.setSizePolicy(sizePolicy)
        self.par01_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par01_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par01_pushButton.setObjectName("par01_pushButton")
        self.gridLayout.addWidget(self.par01_pushButton, 0, 2, 1, 1)
        self.par02_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par02_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par02_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par02_value_lineEdit.setObjectName("par02_value_lineEdit")
        self.gridLayout.addWidget(self.par02_value_lineEdit, 1, 1, 1, 1)
        self.par02_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par02_pushButton.sizePolicy().hasHeightForWidth())
        self.par02_pushButton.setSizePolicy(sizePolicy)
        self.par02_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par02_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par02_pushButton.setObjectName("par02_pushButton")
        self.gridLayout.addWidget(self.par02_pushButton, 1, 2, 1, 1)
        self.par03_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par03_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par03_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par03_value_lineEdit.setObjectName("par03_value_lineEdit")
        self.gridLayout.addWidget(self.par03_value_lineEdit, 2, 1, 1, 1)
        self.par03_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par03_pushButton.sizePolicy().hasHeightForWidth())
        self.par03_pushButton.setSizePolicy(sizePolicy)
        self.par03_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par03_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par03_pushButton.setObjectName("par03_pushButton")
        self.gridLayout.addWidget(self.par03_pushButton, 2, 2, 1, 1)
        self.par04_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par04_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par04_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par04_value_lineEdit.setObjectName("par04_value_lineEdit")
        self.gridLayout.addWidget(self.par04_value_lineEdit, 3, 1, 1, 1)
        self.par04_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par04_pushButton.sizePolicy().hasHeightForWidth())
        self.par04_pushButton.setSizePolicy(sizePolicy)
        self.par04_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par04_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par04_pushButton.setObjectName("par04_pushButton")
        self.gridLayout.addWidget(self.par04_pushButton, 3, 2, 1, 1)
        self.par05_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par05_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par05_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par05_value_lineEdit.setObjectName("par05_value_lineEdit")
        self.gridLayout.addWidget(self.par05_value_lineEdit, 4, 1, 1, 1)
        self.par05_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par05_pushButton.sizePolicy().hasHeightForWidth())
        self.par05_pushButton.setSizePolicy(sizePolicy)
        self.par05_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par05_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par05_pushButton.setObjectName("par05_pushButton")
        self.gridLayout.addWidget(self.par05_pushButton, 4, 2, 1, 1)
        self.par06_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par06_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par06_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par06_value_lineEdit.setObjectName("par06_value_lineEdit")
        self.gridLayout.addWidget(self.par06_value_lineEdit, 5, 1, 1, 1)
        self.par06_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par06_pushButton.sizePolicy().hasHeightForWidth())
        self.par06_pushButton.setSizePolicy(sizePolicy)
        self.par06_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par06_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par06_pushButton.setObjectName("par06_pushButton")
        self.gridLayout.addWidget(self.par06_pushButton, 5, 2, 1, 1)
        self.par07_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par07_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par07_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par07_value_lineEdit.setObjectName("par07_value_lineEdit")
        self.gridLayout.addWidget(self.par07_value_lineEdit, 6, 1, 1, 1)
        self.par07_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par07_pushButton.sizePolicy().hasHeightForWidth())
        self.par07_pushButton.setSizePolicy(sizePolicy)
        self.par07_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par07_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par07_pushButton.setObjectName("par07_pushButton")
        self.gridLayout.addWidget(self.par07_pushButton, 6, 2, 1, 1)
        self.par08_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par08_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par08_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par08_value_lineEdit.setObjectName("par08_value_lineEdit")
        self.gridLayout.addWidget(self.par08_value_lineEdit, 7, 1, 1, 1)
        self.par08_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par08_pushButton.sizePolicy().hasHeightForWidth())
        self.par08_pushButton.setSizePolicy(sizePolicy)
        self.par08_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par08_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par08_pushButton.setObjectName("par08_pushButton")
        self.gridLayout.addWidget(self.par08_pushButton, 7, 2, 1, 1)
        self.par09_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par09_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par09_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par09_value_lineEdit.setObjectName("par09_value_lineEdit")
        self.gridLayout.addWidget(self.par09_value_lineEdit, 8, 1, 1, 1)
        self.par09_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par09_pushButton.sizePolicy().hasHeightForWidth())
        self.par09_pushButton.setSizePolicy(sizePolicy)
        self.par09_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par09_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par09_pushButton.setObjectName("par09_pushButton")
        self.gridLayout.addWidget(self.par09_pushButton, 8, 2, 1, 1)
        self.par10_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par10_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par10_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par10_value_lineEdit.setObjectName("par10_value_lineEdit")
        self.gridLayout.addWidget(self.par10_value_lineEdit, 9, 1, 1, 1)
        self.par10_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par10_pushButton.sizePolicy().hasHeightForWidth())
        self.par10_pushButton.setSizePolicy(sizePolicy)
        self.par10_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par10_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par10_pushButton.setObjectName("par10_pushButton")
        self.gridLayout.addWidget(self.par10_pushButton, 9, 2, 1, 1)
        self.par11_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par11_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par11_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par11_value_lineEdit.setObjectName("par11_value_lineEdit")
        self.gridLayout.addWidget(self.par11_value_lineEdit, 10, 1, 1, 1)
        self.par11_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par11_pushButton.sizePolicy().hasHeightForWidth())
        self.par11_pushButton.setSizePolicy(sizePolicy)
        self.par11_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par11_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par11_pushButton.setObjectName("par11_pushButton")
        self.gridLayout.addWidget(self.par11_pushButton, 10, 2, 1, 1)
        self.par12_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par12_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par12_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par12_value_lineEdit.setObjectName("par12_value_lineEdit")
        self.gridLayout.addWidget(self.par12_value_lineEdit, 11, 1, 1, 1)
        self.par12_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par12_pushButton.sizePolicy().hasHeightForWidth())
        self.par12_pushButton.setSizePolicy(sizePolicy)
        self.par12_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par12_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par12_pushButton.setObjectName("par12_pushButton")
        self.gridLayout.addWidget(self.par12_pushButton, 11, 2, 1, 1)
        self.par13_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par13_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par13_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par13_value_lineEdit.setObjectName("par13_value_lineEdit")
        self.gridLayout.addWidget(self.par13_value_lineEdit, 12, 1, 1, 1)
        self.par13_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par13_pushButton.sizePolicy().hasHeightForWidth())
        self.par13_pushButton.setSizePolicy(sizePolicy)
        self.par13_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par13_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par13_pushButton.setObjectName("par13_pushButton")
        self.gridLayout.addWidget(self.par13_pushButton, 12, 2, 1, 1)
        self.par14_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par14_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par14_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par14_value_lineEdit.setObjectName("par14_value_lineEdit")
        self.gridLayout.addWidget(self.par14_value_lineEdit, 13, 1, 1, 1)
        self.par14_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par14_pushButton.sizePolicy().hasHeightForWidth())
        self.par14_pushButton.setSizePolicy(sizePolicy)
        self.par14_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par14_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par14_pushButton.setObjectName("par14_pushButton")
        self.gridLayout.addWidget(self.par14_pushButton, 13, 2, 1, 1)
        self.par15_value_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par15_value_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par15_value_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.par15_value_lineEdit.setObjectName("par15_value_lineEdit")
        self.gridLayout.addWidget(self.par15_value_lineEdit, 14, 1, 1, 1)
        self.par15_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.par15_pushButton.sizePolicy().hasHeightForWidth())
        self.par15_pushButton.setSizePolicy(sizePolicy)
        self.par15_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.par15_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.par15_pushButton.setObjectName("par15_pushButton")
        self.gridLayout.addWidget(self.par15_pushButton, 14, 2, 1, 1)
        self.par01_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par01_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par01_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par01_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par01_lineEdit.setObjectName("par01_lineEdit")
        self.gridLayout.addWidget(self.par01_lineEdit, 0, 0, 1, 1)
        self.par02_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par02_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par02_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par02_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par02_lineEdit.setObjectName("par02_lineEdit")
        self.gridLayout.addWidget(self.par02_lineEdit, 1, 0, 1, 1)
        self.par03_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par03_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par03_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par03_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par03_lineEdit.setObjectName("par03_lineEdit")
        self.gridLayout.addWidget(self.par03_lineEdit, 2, 0, 1, 1)
        self.par04_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par04_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par04_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par04_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par04_lineEdit.setObjectName("par04_lineEdit")
        self.gridLayout.addWidget(self.par04_lineEdit, 3, 0, 1, 1)
        self.par05_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par05_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par05_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par05_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par05_lineEdit.setObjectName("par05_lineEdit")
        self.gridLayout.addWidget(self.par05_lineEdit, 4, 0, 1, 1)
        self.par06_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par06_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par06_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par06_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par06_lineEdit.setObjectName("par06_lineEdit")
        self.gridLayout.addWidget(self.par06_lineEdit, 5, 0, 1, 1)
        self.par07_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par07_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par07_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par07_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par07_lineEdit.setObjectName("par07_lineEdit")
        self.gridLayout.addWidget(self.par07_lineEdit, 6, 0, 1, 1)
        self.par08_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par08_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par08_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par08_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par08_lineEdit.setObjectName("par08_lineEdit")
        self.gridLayout.addWidget(self.par08_lineEdit, 7, 0, 1, 1)
        self.par09_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par09_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par09_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par09_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par09_lineEdit.setObjectName("par09_lineEdit")
        self.gridLayout.addWidget(self.par09_lineEdit, 8, 0, 1, 1)
        self.par10_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par10_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par10_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par10_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par10_lineEdit.setObjectName("par10_lineEdit")
        self.gridLayout.addWidget(self.par10_lineEdit, 9, 0, 1, 1)
        self.par11_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par11_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par11_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par11_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par11_lineEdit.setObjectName("par11_lineEdit")
        self.gridLayout.addWidget(self.par11_lineEdit, 10, 0, 1, 1)
        self.par12_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par12_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par12_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par12_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par12_lineEdit.setObjectName("par12_lineEdit")
        self.gridLayout.addWidget(self.par12_lineEdit, 11, 0, 1, 1)
        self.par13_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par13_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par13_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par13_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par13_lineEdit.setObjectName("par13_lineEdit")
        self.gridLayout.addWidget(self.par13_lineEdit, 12, 0, 1, 1)
        self.par14_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par14_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par14_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par14_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par14_lineEdit.setObjectName("par14_lineEdit")
        self.gridLayout.addWidget(self.par14_lineEdit, 13, 0, 1, 1)
        self.par15_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.par15_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.par15_lineEdit.setMaximumSize(QtCore.QSize(114, 24))
        self.par15_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                         QtCore.Qt.AlignmentFlag.AlignTrailing|
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.par15_lineEdit.setObjectName("par15_lineEdit")
        self.gridLayout.addWidget(self.par15_lineEdit, 14, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(parent=CFGLoader)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 541, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yaml_file_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaml_file_label.sizePolicy().hasHeightForWidth())
        self.yaml_file_label.setSizePolicy(sizePolicy)
        self.yaml_file_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|
                                          QtCore.Qt.AlignmentFlag.AlignTrailing|
                                          QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.yaml_file_label.setObjectName("yaml_file_label")
        self.horizontalLayout.addWidget(self.yaml_file_label)
        self.yaml_file_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.yaml_file_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.yaml_file_lineEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.yaml_file_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.yaml_file_lineEdit.setReadOnly(True)
        self.yaml_file_lineEdit.setObjectName("yaml_file_lineEdit")
        self.horizontalLayout.addWidget(self.yaml_file_lineEdit)
        self.yaml_file_pushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaml_file_pushButton.sizePolicy().hasHeightForWidth())
        self.yaml_file_pushButton.setSizePolicy(sizePolicy)
        self.yaml_file_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.yaml_file_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.yaml_file_pushButton.setObjectName("yaml_file_pushButton")
        self.horizontalLayout.addWidget(self.yaml_file_pushButton)
        self.status_lineEdit = QtWidgets.QLineEdit(parent=CFGLoader)
        self.status_lineEdit.setGeometry(QtCore.QRect(170, 560, 221, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_lineEdit.sizePolicy().hasHeightForWidth())
        self.status_lineEdit.setSizePolicy(sizePolicy)
        self.status_lineEdit.setMinimumSize(QtCore.QSize(221, 24))
        self.status_lineEdit.setMaximumSize(QtCore.QSize(221, 24))
        self.status_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_lineEdit.setReadOnly(True)
        self.status_lineEdit.setObjectName("status_lineEdit")
        self.reload_pushButton = QtWidgets.QPushButton(parent=CFGLoader)
        self.reload_pushButton.setGeometry(QtCore.QRect(10, 560, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_pushButton.sizePolicy().hasHeightForWidth())
        self.reload_pushButton.setSizePolicy(sizePolicy)
        self.reload_pushButton.setMinimumSize(QtCore.QSize(75, 24))
        self.reload_pushButton.setMaximumSize(QtCore.QSize(75, 24))
        self.reload_pushButton.setObjectName("reload_pushButton")

        # custom
        self.yaml_file_pushButton.setDefault(True)
        self.yaml_file_pushButton.clicked.connect(self.browseYAMLFile)
        self.cancel_pushButton.clicked.connect(lambda: self.cancel(CFGLoader))
        self.save_pushButton.setDisabled(True)
        self.save_pushButton.clicked.connect(self.saveYAML)
        self.saveas_pushButton.clicked.connect(self.saveas)
        self.reload_pushButton.clicked.connect(self.reload)
        self.reload_pushButton.setDisabled(True)
        self.par01_pushButton.clicked.connect(lambda: self.browseFile(1))
        self.par02_pushButton.clicked.connect(lambda: self.browseFile(2))
        self.par03_pushButton.clicked.connect(lambda: self.browseFile(3))
        self.par04_pushButton.clicked.connect(lambda: self.browseFile(4))
        self.par05_pushButton.clicked.connect(lambda: self.browseFile(5))
        self.par06_pushButton.clicked.connect(lambda: self.browseFile(6))
        self.par07_pushButton.clicked.connect(lambda: self.browseFile(7))
        self.par08_pushButton.clicked.connect(lambda: self.browseFile(8))
        self.par09_pushButton.clicked.connect(lambda: self.browseFile(9))
        self.par10_pushButton.clicked.connect(lambda: self.browseFile(10))
        self.par11_pushButton.clicked.connect(lambda: self.browseFile(11))
        self.par12_pushButton.clicked.connect(lambda: self.browseFile(12))
        self.par13_pushButton.clicked.connect(lambda: self.browseFile(13))
        self.par14_pushButton.clicked.connect(lambda: self.browseFile(14))
        self.par15_pushButton.clicked.connect(lambda: self.browseFile(15))

        # task
        self.checkUITMP()

        self.retranslateUi(CFGLoader)
        QtCore.QMetaObject.connectSlotsByName(CFGLoader)

    def retranslateUi(self, CFGLoader):
        _translate = QtCore.QCoreApplication.translate
        title = "Configurator | VSenseBox v" + getVersionString() + " (GPLV3+)"
        CFGLoader.setWindowTitle(_translate("CFGLoader", title))
        self.save_pushButton.setText(_translate("CFGLoader", "Save"))
        self.cancel_pushButton.setText(_translate("CFGLoader", "Cancel"))
        self.par_label.setText(_translate("CFGLoader", "Edit parameter"))
        self.value_label.setText(_translate("CFGLoader", "Edit value"))
        self.file_label.setText(_translate("CFGLoader", "File?"))
        self.saveas_pushButton.setText(_translate("CFGLoader", "Save as"))
        par_value_placeholder = "Bool/Int/Float/List/String/Path"
        self.par01_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par01_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par02_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par02_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par03_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par03_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par04_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par04_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par05_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par05_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par06_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par06_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par07_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par07_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par08_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par08_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par09_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par09_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par10_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par10_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par11_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par11_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par12_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par12_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par13_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par13_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par14_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par14_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par15_value_lineEdit.setPlaceholderText(_translate("CFGLoader", par_value_placeholder))
        self.par15_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.par01_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 01"))
        self.par02_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 02"))
        self.par03_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 03"))
        self.par04_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 04"))
        self.par05_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 05"))
        self.par06_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 06"))
        self.par07_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 07"))
        self.par08_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 08"))
        self.par09_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 09"))
        self.par10_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 10"))
        self.par11_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 11"))
        self.par12_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 12"))
        self.par13_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 13"))
        self.par14_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 14"))
        self.par15_lineEdit.setPlaceholderText(_translate("CFGLoader", "Parameter 15"))
        self.yaml_file_label.setText(_translate("CFGLoader", "You are configing file:"))
        self.yaml_file_lineEdit.setPlaceholderText(_translate("CFGLoader", "For example: yolo_ultralytics_v11s.yaml"))
        self.yaml_file_pushButton.setText(_translate("CFGLoader", "Browse"))
        self.status_lineEdit.setPlaceholderText(_translate("CFGLoader", "Status"))
        self.reload_pushButton.setText(_translate("CFGLoader", "Reload"))

    def resetStatus(self):
        self.status_lineEdit.setText("")
        self.status_lineEdit.setStyleSheet("color: rgb(0, 0, 0)")

    def browseYAMLFile(self):
        self.resetStatus()
        file_filter = "Config file (*.yaml *.json)"
        input_file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse config file", 
                                                              IN_CONFIG_DIR, file_filter)
        if input_file:
            self.yaml_file_lineEdit.setText(input_file)
            self.readYAML(input_file)
            self.save_pushButton.setDisabled(False)
            self.reload_pushButton.setDisabled(False)

    def browseFile(self, par_num):
        file_filter = "File (*.*)"
        input_file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse file", 
                                                              IN_ROOT_DIR, file_filter)
        if input_file:
            input_file = normalizePathFDS(IN_ROOT_DIR, input_file)
            if par_num == 1:
                self.par01_value_lineEdit.setText(input_file)
            elif par_num == 2:
                self.par02_value_lineEdit.setText(input_file)
            elif par_num == 3:
                self.par03_value_lineEdit.setText(input_file)
            elif par_num == 4:
                self.par04_value_lineEdit.setText(input_file)
            elif par_num == 5:
                self.par05_value_lineEdit.setText(input_file)
            elif par_num == 6:
                self.par06_value_lineEdit.setText(input_file)
            elif par_num == 7:
                self.par07_value_lineEdit.setText(input_file)
            elif par_num == 8:
                self.par08_value_lineEdit.setText(input_file)
            elif par_num == 9:
                self.par09_value_lineEdit.setText(input_file)
            elif par_num == 10:
                self.par10_value_lineEdit.setText(input_file)
            elif par_num == 11:
                self.par11_value_lineEdit.setText(input_file)
            elif par_num == 12:
                self.par12_value_lineEdit.setText(input_file)
            elif par_num == 13:
                self.par13_value_lineEdit.setText(input_file)
            elif par_num == 14:
                self.par14_value_lineEdit.setText(input_file)
            elif par_num == 15:
                self.par15_value_lineEdit.setText(input_file)

    def clearPar(self):
        self.resetStatus()
        self.par01_lineEdit.setText("")
        self.par01_value_lineEdit.setText("")
        self.par02_lineEdit.setText("")
        self.par02_value_lineEdit.setText("")
        self.par03_lineEdit.setText("")
        self.par03_value_lineEdit.setText("")
        self.par04_lineEdit.setText("")
        self.par04_value_lineEdit.setText("")
        self.par05_lineEdit.setText("")
        self.par05_value_lineEdit.setText("")
        self.par06_lineEdit.setText("")
        self.par06_value_lineEdit.setText("")
        self.par07_lineEdit.setText("")
        self.par07_value_lineEdit.setText("")
        self.par08_lineEdit.setText("")
        self.par08_value_lineEdit.setText("")
        self.par09_lineEdit.setText("")
        self.par09_value_lineEdit.setText("")
        self.par10_lineEdit.setText("")
        self.par10_value_lineEdit.setText("")
        self.par11_lineEdit.setText("")
        self.par11_value_lineEdit.setText("")
        self.par12_lineEdit.setText("")
        self.par12_value_lineEdit.setText("")
        self.par13_lineEdit.setText("")
        self.par13_value_lineEdit.setText("")
        self.par14_lineEdit.setText("")
        self.par14_value_lineEdit.setText("")
        self.par15_lineEdit.setText("")
        self.par15_value_lineEdit.setText("")

    def readYAML(self, yaml_file):
        config_yaml = getCFGDict(yaml_file)
        self.clearPar()
        if len(config_yaml) > 15:
            add_warning_log("The length of YAML configuration is greater than 15. " +
                            "Its original content will be lost if you click save.")
            self.status_lineEdit.setText("CONTENT WILL BE LOST!!!")
            self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")
        par_num = 1
        for key, value in config_yaml.items():
            if par_num == 1:
                self.par01_lineEdit.setText(key)
                self.par01_value_lineEdit.setText(str(value))
            elif par_num == 2:
                self.par02_lineEdit.setText(key)
                self.par02_value_lineEdit.setText(str(value))
            elif par_num == 3:
                self.par03_lineEdit.setText(key)
                self.par03_value_lineEdit.setText(str(value))
            elif par_num == 4:
                self.par04_lineEdit.setText(key)
                self.par04_value_lineEdit.setText(str(value))
            elif par_num == 5:
                self.par05_lineEdit.setText(key)
                self.par05_value_lineEdit.setText(str(value))
            elif par_num == 6:
                self.par06_lineEdit.setText(key)
                self.par06_value_lineEdit.setText(str(value))
            elif par_num == 7:
                self.par07_lineEdit.setText(key)
                self.par07_value_lineEdit.setText(str(value))
            elif par_num == 8:
                self.par08_lineEdit.setText(key)
                self.par08_value_lineEdit.setText(str(value))
            elif par_num == 9:
                self.par09_lineEdit.setText(key)
                self.par09_value_lineEdit.setText(str(value))
            elif par_num == 10:
                self.par10_lineEdit.setText(key)
                self.par10_value_lineEdit.setText(str(value))
            elif par_num == 11:
                self.par11_lineEdit.setText(key)
                self.par11_value_lineEdit.setText(str(value))
            elif par_num == 12:
                self.par12_lineEdit.setText(key)
                self.par12_value_lineEdit.setText(str(value))
            elif par_num == 13:
                self.par13_lineEdit.setText(key)
                self.par13_value_lineEdit.setText(str(value))
            elif par_num == 14:
                self.par14_lineEdit.setText(key)
                self.par14_value_lineEdit.setText(str(value))
            elif par_num == 15:
                self.par15_lineEdit.setText(key)
                self.par15_value_lineEdit.setText(str(value))
            par_num += 1

    def getConfig(self):
        _config_yaml = {
            self.par01_lineEdit.text(): self.par01_value_lineEdit.text(),
            self.par02_lineEdit.text(): self.par02_value_lineEdit.text(),
            self.par03_lineEdit.text(): self.par03_value_lineEdit.text(),
            self.par04_lineEdit.text(): self.par04_value_lineEdit.text(),
            self.par05_lineEdit.text(): self.par05_value_lineEdit.text(),
            self.par06_lineEdit.text(): self.par06_value_lineEdit.text(),
            self.par07_lineEdit.text(): self.par07_value_lineEdit.text(),
            self.par08_lineEdit.text(): self.par08_value_lineEdit.text(),
            self.par09_lineEdit.text(): self.par09_value_lineEdit.text(),
            self.par10_lineEdit.text(): self.par10_value_lineEdit.text(),
            self.par11_lineEdit.text(): self.par11_value_lineEdit.text(),
            self.par12_lineEdit.text(): self.par12_value_lineEdit.text(),
            self.par13_lineEdit.text(): self.par13_value_lineEdit.text(),
            self.par14_lineEdit.text(): self.par14_value_lineEdit.text(),
            self.par15_lineEdit.text(): self.par15_value_lineEdit.text()
        }
        config_yaml = {k.strip(): v.strip() for k, v in _config_yaml.items() if k.strip() != ''}
        return config_yaml

    def saveYAML(self):
        self.resetStatus()
        yaml_file = self.yaml_file_lineEdit.text()
        yaml_path = getAncestorDir(yaml_file)
        if isExist(getAncestorDir(yaml_file)) and yaml_path != '':
            date_time = str(time.strftime("%Y-%m-%d %Hh%Mm%Ss"))
            try:
                header = "# Modified " + date_time + "\n"
                config_yaml = self.getConfig()
                dumpDocDict(yaml_file, config_yaml, header)
                self.status_lineEdit.setText("Saved " + date_time)
                self.status_lineEdit.setStyleSheet("color: rgb(50, 255, 50)")
            except Exception as e:
                print(e)
                self.status_lineEdit.setText("Failed to save!")
                self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")
        else:
            self.status_lineEdit.setText("YAML path is not valid!")
            self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")
    
    def saveas(self):
        self.resetStatus()
        config_yaml = self.getConfig()
        file_filter = "File (*.yaml)"
        yaml_file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save configuration", 
                                                             IN_CONFIG_DIR, file_filter)
        if isExist(getAncestorDir(yaml_file)) and yaml_file != '':
            date_time = str(time.strftime("%Y-%m-%d %Hh%Mm%Ss"))
            try:
                header = "# Modified " + date_time + "\n"
                config_yaml = self.getConfig()
                dumpDocDict(yaml_file, config_yaml, header)
                self.status_lineEdit.setText("Saved " + date_time)
                self.status_lineEdit.setStyleSheet("color: rgb(50, 255, 50)")
            except Exception as e:
                print(e)
                self.status_lineEdit.setText("Failed to save!")
                self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")

    def checkUITMP(self):
        if isExist(UI_TMP):
            with open(UI_TMP) as _ui_tmp_file:
                lines = _ui_tmp_file.read().splitlines()
                if len(lines) > 0:
                    if isinstance(lines[0], str):
                        self.yaml_file_lineEdit.setText(lines[0])
                        self.readYAML(lines[0])
                        self.save_pushButton.setDisabled(False)
                        self.reload_pushButton.setDisabled(False)
            os.remove(UI_TMP)

    def reload(self):
        self.resetStatus()
        yaml_file = self.yaml_file_lineEdit.text()
        if isExist(yaml_file):
            try:
                self.clearPar()
                self.readYAML(yaml_file)
                self.status_lineEdit.setText("Reloaded!")
                self.status_lineEdit.setStyleSheet("color: rgb(50, 255, 50)")
            except Exception as e:
                print(e)
                self.status_lineEdit.setText("Failed to reload!")
                self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")
        else:
            self.status_lineEdit.setText("File no longer exists!")
            self.status_lineEdit.setStyleSheet("color: rgb(255, 50, 50)")

    def cancel(self, CFGLoader):
        CFGLoader.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CFGLoader = QtWidgets.QWidget()
    CFGLoader.setWindowIcon(QtGui.QIcon(joinFPathFull(CUR_DIR, "assets/settings.ico")))
    ui = Ui_CFGLoader()
    ui.setupUi(CFGLoader)
    CFGLoader.show()
    sys.exit(app.exec())
