# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_ras2dAreaMesh.ui'
#
# Created: Thu Oct 22 10:50:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AreaMesh(object):
    def setupUi(self, AreaMesh):
        AreaMesh.setObjectName(_fromUtf8("AreaMesh"))
        AreaMesh.resize(357, 410)
        self.gridLayout = QtGui.QGridLayout(AreaMesh)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(AreaMesh)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.cbo2dAreas = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dAreas.sizePolicy().hasHeightForWidth())
        self.cbo2dAreas.setSizePolicy(sizePolicy)
        self.cbo2dAreas.setMinimumSize(QtCore.QSize(0, 0))
        self.cbo2dAreas.setAcceptDrops(False)
        self.cbo2dAreas.setMinimumContentsLength(0)
        self.cbo2dAreas.setFrame(True)
        self.cbo2dAreas.setObjectName(_fromUtf8("cbo2dAreas"))
        self.horizontalLayout_3.addWidget(self.cbo2dAreas)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.AreaNameAttributeLabel = QtGui.QLabel(self.groupBox)
        self.AreaNameAttributeLabel.setObjectName(_fromUtf8("AreaNameAttributeLabel"))
        self.horizontalLayout_4.addWidget(self.AreaNameAttributeLabel)
        self.cbo2dAreasNameAttr = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dAreasNameAttr.sizePolicy().hasHeightForWidth())
        self.cbo2dAreasNameAttr.setSizePolicy(sizePolicy)
        self.cbo2dAreasNameAttr.setObjectName(_fromUtf8("cbo2dAreasNameAttr"))
        self.horizontalLayout_4.addWidget(self.cbo2dAreasNameAttr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.AreaNameAttributeLabel_2 = QtGui.QLabel(self.groupBox)
        self.AreaNameAttributeLabel_2.setObjectName(_fromUtf8("AreaNameAttributeLabel_2"))
        self.horizontalLayout_5.addWidget(self.AreaNameAttributeLabel_2)
        self.cbo2dAreasMeshSizeAttr = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dAreasMeshSizeAttr.sizePolicy().hasHeightForWidth())
        self.cbo2dAreasMeshSizeAttr.setSizePolicy(sizePolicy)
        self.cbo2dAreasMeshSizeAttr.setObjectName(_fromUtf8("cbo2dAreasMeshSizeAttr"))
        self.horizontalLayout_5.addWidget(self.cbo2dAreasMeshSizeAttr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(AreaMesh)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.AreaNameAttributeLabel_3 = QtGui.QLabel(self.groupBox_2)
        self.AreaNameAttributeLabel_3.setObjectName(_fromUtf8("AreaNameAttributeLabel_3"))
        self.horizontalLayout_6.addWidget(self.AreaNameAttributeLabel_3)
        self.cboStructures = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStructures.sizePolicy().hasHeightForWidth())
        self.cboStructures.setSizePolicy(sizePolicy)
        self.cboStructures.setObjectName(_fromUtf8("cboStructures"))
        self.horizontalLayout_6.addWidget(self.cboStructures)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.AreaNameAttributeLabel_4 = QtGui.QLabel(self.groupBox_2)
        self.AreaNameAttributeLabel_4.setObjectName(_fromUtf8("AreaNameAttributeLabel_4"))
        self.horizontalLayout_7.addWidget(self.AreaNameAttributeLabel_4)
        self.cboStructureMeshSizeAlongAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStructureMeshSizeAlongAttr.sizePolicy().hasHeightForWidth())
        self.cboStructureMeshSizeAlongAttr.setSizePolicy(sizePolicy)
        self.cboStructureMeshSizeAlongAttr.setObjectName(_fromUtf8("cboStructureMeshSizeAlongAttr"))
        self.horizontalLayout_7.addWidget(self.cboStructureMeshSizeAlongAttr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_9.addWidget(self.label_6)
        self.cboStructureMeshSizeAcrossAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStructureMeshSizeAcrossAttr.sizePolicy().hasHeightForWidth())
        self.cboStructureMeshSizeAcrossAttr.setSizePolicy(sizePolicy)
        self.cboStructureMeshSizeAcrossAttr.setObjectName(_fromUtf8("cboStructureMeshSizeAcrossAttr"))
        self.horizontalLayout_9.addWidget(self.cboStructureMeshSizeAcrossAttr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.cboStructureMeshRowsAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStructureMeshRowsAttr.sizePolicy().hasHeightForWidth())
        self.cboStructureMeshRowsAttr.setSizePolicy(sizePolicy)
        self.cboStructureMeshRowsAttr.setObjectName(_fromUtf8("cboStructureMeshRowsAttr"))
        self.horizontalLayout_11.addWidget(self.cboStructureMeshRowsAttr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(AreaMesh)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setMargin(3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.cboBreakPoints = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreakPoints.sizePolicy().hasHeightForWidth())
        self.cboBreakPoints.setSizePolicy(sizePolicy)
        self.cboBreakPoints.setObjectName(_fromUtf8("cboBreakPoints"))
        self.horizontalLayout_8.addWidget(self.cboBreakPoints)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.label_2 = QtGui.QLabel(AreaMesh)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditGeoFile = QtGui.QLineEdit(AreaMesh)
        self.lineEditGeoFile.setPlaceholderText(_fromUtf8(""))
        self.lineEditGeoFile.setObjectName(_fromUtf8("lineEditGeoFile"))
        self.horizontalLayout_2.addWidget(self.lineEditGeoFile)
        self.geoFileBtn = QtGui.QToolButton(AreaMesh)
        self.geoFileBtn.setObjectName(_fromUtf8("geoFileBtn"))
        self.horizontalLayout_2.addWidget(self.geoFileBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.helpButton = QtGui.QPushButton(AreaMesh)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout.addWidget(self.helpButton)
        self.buttonBox = QtGui.QDialogButtonBox(AreaMesh)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label.setBuddy(self.cbo2dAreas)
        self.AreaNameAttributeLabel.setBuddy(self.cbo2dAreasNameAttr)
        self.AreaNameAttributeLabel_2.setBuddy(self.cbo2dAreasMeshSizeAttr)
        self.AreaNameAttributeLabel_3.setBuddy(self.cboStructures)
        self.AreaNameAttributeLabel_4.setBuddy(self.cboStructureMeshSizeAlongAttr)

        self.retranslateUi(AreaMesh)
        QtCore.QMetaObject.connectSlotsByName(AreaMesh)

    def retranslateUi(self, AreaMesh):
        AreaMesh.setWindowTitle(_translate("AreaMesh", "Create 2D Flow Areas", None))
        self.groupBox.setTitle(_translate("AreaMesh", "2D Areas Layer", None))
        self.label.setText(_translate("AreaMesh", "Layer name", None))
        self.AreaNameAttributeLabel.setText(_translate("AreaMesh", "Area name attribute", None))
        self.AreaNameAttributeLabel_2.setText(_translate("AreaMesh", "Default mesh size attribute", None))
        self.groupBox_2.setTitle(_translate("AreaMesh", "Structures", None))
        self.AreaNameAttributeLabel_3.setText(_translate("AreaMesh", "Layer name", None))
        self.label_4.setText(_translate("AreaMesh", "Attributes:", None))
        self.AreaNameAttributeLabel_4.setText(_translate("AreaMesh", "Mesh size along structure", None))
        self.label_6.setText(_translate("AreaMesh", "Mesh size across structure", None))
        self.label_5.setText(_translate("AreaMesh", "Mesh rows number", None))
        self.groupBox_3.setTitle(_translate("AreaMesh", "Structure breakpoints", None))
        self.label_3.setText(_translate("AreaMesh", "Layer name", None))
        self.label_2.setText(_translate("AreaMesh", "Target HEC-RAS geometry file", None))
        self.geoFileBtn.setText(_translate("AreaMesh", "...", None))
        self.helpButton.setText(_translate("AreaMesh", "Help", None))

