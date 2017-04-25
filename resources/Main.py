# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_player_coins = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_player_coins.setFont(font)
        self.txt_player_coins.setObjectName("txt_player_coins")
        self.verticalLayout.addWidget(self.txt_player_coins)
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.tab_facts = QtWidgets.QWidget()
        self.tab_facts.setObjectName("tab_facts")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_facts)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_facts = QtWidgets.QListView(self.tab_facts)
        self.list_facts.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list_facts.setObjectName("list_facts")
        self.horizontalLayout_2.addWidget(self.list_facts)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_facts)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_name = QtWidgets.QLabel(self.tab_facts)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.label_2 = QtWidgets.QLabel(self.tab_facts)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_per_sec = QtWidgets.QLabel(self.tab_facts)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_per_sec.setFont(font)
        self.txt_per_sec.setObjectName("txt_per_sec")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_per_sec)
        self.label_5 = QtWidgets.QLabel(self.tab_facts)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.list_in = QtWidgets.QListView(self.tab_facts)
        self.list_in.setObjectName("list_in")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.list_in)
        self.label_6 = QtWidgets.QLabel(self.tab_facts)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.list_out = QtWidgets.QListView(self.tab_facts)
        self.list_out.setObjectName("list_out")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.list_out)
        self.label_7 = QtWidgets.QLabel(self.tab_facts)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cbx_enable = QtWidgets.QCheckBox(self.tab_facts)
        self.cbx_enable.setObjectName("cbx_enable")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cbx_enable)
        self.label_10 = QtWidgets.QLabel(self.tab_facts)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_8 = QtWidgets.QLabel(self.tab_facts)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txt_energy = QtWidgets.QLabel(self.tab_facts)
        self.txt_energy.setObjectName("txt_energy")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txt_energy)
        self.txt_state = QtWidgets.QLabel(self.tab_facts)
        self.txt_state.setObjectName("txt_state")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_state)
        self.label_12 = QtWidgets.QLabel(self.tab_facts)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.bar_current = QtWidgets.QProgressBar(self.tab_facts)
        self.bar_current.setProperty("value", 24)
        self.bar_current.setObjectName("bar_current")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bar_current)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.tabs.addTab(self.tab_facts, "")
        self.tab_storages = QtWidgets.QWidget()
        self.tab_storages.setObjectName("tab_storages")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_storages)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list_storages = QtWidgets.QListView(self.tab_storages)
        self.list_storages.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list_storages.setObjectName("list_storages")
        self.horizontalLayout_3.addWidget(self.list_storages)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_sell_10 = QtWidgets.QPushButton(self.tab_storages)
        self.btn_sell_10.setObjectName("btn_sell_10")
        self.gridLayout.addWidget(self.btn_sell_10, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_storages)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_storages)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_storages)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.txt_storage_name = QtWidgets.QLabel(self.tab_storages)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_storage_name.setFont(font)
        self.txt_storage_name.setObjectName("txt_storage_name")
        self.gridLayout.addWidget(self.txt_storage_name, 0, 1, 1, 1)
        self.list_storage_elements = QtWidgets.QListView(self.tab_storages)
        self.list_storage_elements.setObjectName("list_storage_elements")
        self.gridLayout.addWidget(self.list_storage_elements, 3, 1, 1, 1)
        self.txt_storage_capacity = QtWidgets.QLabel(self.tab_storages)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_storage_capacity.setFont(font)
        self.txt_storage_capacity.setObjectName("txt_storage_capacity")
        self.gridLayout.addWidget(self.txt_storage_capacity, 1, 1, 1, 1)
        self.bar_storage_capacity = QtWidgets.QProgressBar(self.tab_storages)
        self.bar_storage_capacity.setProperty("value", 24)
        self.bar_storage_capacity.setObjectName("bar_storage_capacity")
        self.gridLayout.addWidget(self.bar_storage_capacity, 2, 1, 1, 1)
        self.btn_sell_1 = QtWidgets.QPushButton(self.tab_storages)
        self.btn_sell_1.setObjectName("btn_sell_1")
        self.gridLayout.addWidget(self.btn_sell_1, 4, 1, 1, 1)
        self.btn_sell_all = QtWidgets.QPushButton(self.tab_storages)
        self.btn_sell_all.setObjectName("btn_sell_all")
        self.gridLayout.addWidget(self.btn_sell_all, 6, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.tabs.addTab(self.tab_storages, "")
        self.verticalLayout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt_player_coins.setText(_translate("MainWindow", "Ресурсов игрока: 9000"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.txt_name.setText(_translate("MainWindow", "Шахта"))
        self.label_2.setText(_translate("MainWindow", "Товара в секунду"))
        self.txt_per_sec.setText(_translate("MainWindow", "2.5"))
        self.label_5.setText(_translate("MainWindow", "Что производит"))
        self.label_6.setText(_translate("MainWindow", "Что требуется"))
        self.label_7.setText(_translate("MainWindow", "Статус"))
        self.cbx_enable.setText(_translate("MainWindow", "Включено"))
        self.label_10.setText(_translate("MainWindow", "Состояние"))
        self.label_8.setText(_translate("MainWindow", "Потребение энергии"))
        self.txt_energy.setText(_translate("MainWindow", "100"))
        self.txt_state.setText(_translate("MainWindow", "Не работает-Не хватает энергии"))
        self.label_12.setText(_translate("MainWindow", "Производство"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_facts), _translate("MainWindow", "Фабрики"))
        self.btn_sell_10.setText(_translate("MainWindow", "Продать 10 шт"))
        self.label_9.setText(_translate("MainWindow", "Элементы на складе"))
        self.label_4.setText(_translate("MainWindow", "Вместимость склада"))
        self.label_3.setText(_translate("MainWindow", "Название"))
        self.txt_storage_name.setText(_translate("MainWindow", "Склад 1"))
        self.txt_storage_capacity.setText(_translate("MainWindow", "100/152"))
        self.btn_sell_1.setText(_translate("MainWindow", "Продать 1 шт"))
        self.btn_sell_all.setText(_translate("MainWindow", "Продать все"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_storages), _translate("MainWindow", "Склады"))

