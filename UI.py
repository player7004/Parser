# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleLccYhS.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 13, 781, 541))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_base_save = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_save.setObjectName(u"bt_base_save")

        self.gridLayout_2.addWidget(self.bt_base_save, 3, 6, 1, 1)

        self.line_base = QLineEdit(self.gridLayoutWidget_2)
        self.line_base.setObjectName(u"line_base")

        self.gridLayout_2.addWidget(self.line_base, 3, 5, 1, 1)

        self.bt_exit = QPushButton(self.gridLayoutWidget_2)
        self.bt_exit.setObjectName(u"bt_exit")

        self.gridLayout_2.addWidget(self.bt_exit, 6, 6, 1, 1)

        self.line_regul = QLineEdit(self.gridLayoutWidget_2)
        self.line_regul.setObjectName(u"line_regul")

        self.gridLayout_2.addWidget(self.line_regul, 1, 1, 1, 1)

        self.bt_start = QPushButton(self.gridLayoutWidget_2)
        self.bt_start.setObjectName(u"bt_start")

        self.gridLayout_2.addWidget(self.bt_start, 5, 3, 1, 1)

        self.table_sites = QTableView(self.gridLayoutWidget_2)
        self.table_sites.setObjectName(u"table_sites")

        self.gridLayout_2.addWidget(self.table_sites, 5, 0, 1, 2)

        self.line_sites = QLineEdit(self.gridLayoutWidget_2)
        self.line_sites.setObjectName(u"line_sites")

        self.gridLayout_2.addWidget(self.line_sites, 3, 1, 1, 1)

        self.bt_base_open = QPushButton(self.gridLayoutWidget_2)
        self.bt_base_open.setObjectName(u"bt_base_open")

        self.gridLayout_2.addWidget(self.bt_base_open, 1, 6, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.bt_regul = QPushButton(self.gridLayoutWidget_2)
        self.bt_regul.setObjectName(u"bt_regul")

        self.gridLayout_2.addWidget(self.bt_regul, 1, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.bt_sites = QPushButton(self.gridLayoutWidget_2)
        self.bt_sites.setObjectName(u"bt_sites")

        self.gridLayout_2.addWidget(self.bt_sites, 3, 3, 1, 1)

        self.table_base = QTableView(self.gridLayoutWidget_2)
        self.table_base.setObjectName(u"table_base")

        self.gridLayout_2.addWidget(self.table_base, 5, 4, 1, 3)

        self.horizontalSpacer = QSpacerItem(91, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_base_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.bt_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.bt_base_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0441\u0430\u0439\u0442\u043e\u0432", None))
        self.bt_regul.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b. \u0432\u044b\u0440\u0430\u0436.", None))
        self.bt_sites.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
    # retranslateUi

