# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_importRiverFromIsokp.ui'
#
# Created: Tue Sep 15 08:46:52 2015
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

class Ui_DlgImportRiverFromIsokp(object):
    def setupUi(self, DlgImportRiverFromIsokp):
        DlgImportRiverFromIsokp.setObjectName(_fromUtf8("DlgImportRiverFromIsokp"))
        DlgImportRiverFromIsokp.resize(374, 310)
        self.gridLayout = QtGui.QGridLayout(DlgImportRiverFromIsokp)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DlgImportRiverFromIsokp)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.lineEdConnection = QtGui.QLineEdit(self.groupBox)
        self.lineEdConnection.setReadOnly(True)
        self.lineEdConnection.setObjectName(_fromUtf8("lineEdConnection"))
        self.verticalLayout_5.addWidget(self.lineEdConnection)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_6.addWidget(self.label_6)
        self.lineEdSchema = QtGui.QLineEdit(self.groupBox)
        self.lineEdSchema.setObjectName(_fromUtf8("lineEdSchema"))
        self.verticalLayout_6.addWidget(self.lineEdSchema)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdSrid = QtGui.QLineEdit(self.groupBox)
        self.lineEdSrid.setObjectName(_fromUtf8("lineEdSrid"))
        self.horizontalLayout_4.addWidget(self.lineEdSrid)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.helpButton = QtGui.QPushButton(DlgImportRiverFromIsokp)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout.addWidget(self.helpButton)
        self.buttonBox = QtGui.QDialogButtonBox(DlgImportRiverFromIsokp)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(DlgImportRiverFromIsokp)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdHostname = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdHostname.setObjectName(_fromUtf8("lineEdHostname"))
        self.verticalLayout_3.addWidget(self.lineEdHostname)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdUsername = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdUsername.setObjectName(_fromUtf8("lineEdUsername"))
        self.verticalLayout_3.addWidget(self.lineEdUsername)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.lineEdDatabase = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdDatabase.setObjectName(_fromUtf8("lineEdDatabase"))
        self.verticalLayout_4.addWidget(self.lineEdDatabase)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.lineEdPassword = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdPassword.setObjectName(_fromUtf8("lineEdPassword"))
        self.verticalLayout_4.addWidget(self.lineEdPassword)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.btnConnect = QtGui.QPushButton(self.groupBox_2)
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.verticalLayout_7.addWidget(self.btnConnect)
        self.AreaNameAttributeLabel = QtGui.QLabel(self.groupBox_2)
        self.AreaNameAttributeLabel.setObjectName(_fromUtf8("AreaNameAttributeLabel"))
        self.verticalLayout_7.addWidget(self.AreaNameAttributeLabel)
        self.cboRivers = QtGui.QComboBox(self.groupBox_2)
        self.cboRivers.setObjectName(_fromUtf8("cboRivers"))
        self.verticalLayout_7.addWidget(self.cboRivers)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.AreaNameAttributeLabel.setBuddy(self.cboRivers)

        self.retranslateUi(DlgImportRiverFromIsokp)
        QtCore.QMetaObject.connectSlotsByName(DlgImportRiverFromIsokp)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdHostname, self.lineEdDatabase)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdDatabase, self.lineEdUsername)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdUsername, self.lineEdPassword)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdPassword, self.btnConnect)
        DlgImportRiverFromIsokp.setTabOrder(self.btnConnect, self.cboRivers)
        DlgImportRiverFromIsokp.setTabOrder(self.cboRivers, self.lineEdConnection)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdConnection, self.lineEdSchema)
        DlgImportRiverFromIsokp.setTabOrder(self.lineEdSchema, self.helpButton)
        DlgImportRiverFromIsokp.setTabOrder(self.helpButton, self.buttonBox)

    def retranslateUi(self, DlgImportRiverFromIsokp):
        DlgImportRiverFromIsokp.setWindowTitle(_translate("DlgImportRiverFromIsokp", "Import River Data From ISOKP", None))
        self.groupBox.setTitle(_translate("DlgImportRiverFromIsokp", "PostGIS", None))
        self.label_5.setText(_translate("DlgImportRiverFromIsokp", "Connection", None))
        self.label_6.setText(_translate("DlgImportRiverFromIsokp", "Target schema", None))
        self.label_7.setText(_translate("DlgImportRiverFromIsokp", "SRID", None))
        self.lineEdSrid.setText(_translate("DlgImportRiverFromIsokp", "2180", None))
        self.helpButton.setText(_translate("DlgImportRiverFromIsokp", "Help", None))
        self.groupBox_2.setTitle(_translate("DlgImportRiverFromIsokp", "ISOKP", None))
        self.label.setText(_translate("DlgImportRiverFromIsokp", "Host name", None))
        self.lineEdHostname.setText(_translate("DlgImportRiverFromIsokp", "cmp20", None))
        self.label_3.setText(_translate("DlgImportRiverFromIsokp", "Username", None))
        self.lineEdUsername.setText(_translate("DlgImportRiverFromIsokp", "csduser", None))
        self.label_2.setText(_translate("DlgImportRiverFromIsokp", "Database", None))
        self.lineEdDatabase.setText(_translate("DlgImportRiverFromIsokp", "cross_section_db_pzrp", None))
        self.label_4.setText(_translate("DlgImportRiverFromIsokp", "Password", None))
        self.lineEdPassword.setText(_translate("DlgImportRiverFromIsokp", "csdpass", None))
        self.btnConnect.setText(_translate("DlgImportRiverFromIsokp", "Connect to ISOKP", None))
        self.AreaNameAttributeLabel.setText(_translate("DlgImportRiverFromIsokp", "Select River", None))

