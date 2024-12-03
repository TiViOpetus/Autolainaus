# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'administrative.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 655)
        self.actionMuokkaa = QAction(MainWindow)
        self.actionMuokkaa.setObjectName(u"actionMuokkaa")
        self.actionTietoja_ohjelmasta = QAction(MainWindow)
        self.actionTietoja_ohjelmasta.setObjectName(u"actionTietoja_ohjelmasta")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 791, 601))
        font = QFont()
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabWidget.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.studentTab = QWidget()
        self.studentTab.setObjectName(u"studentTab")
        self.studentTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.registerdPersonCatalogTableWidget = QTableWidget(self.studentTab)
        if (self.registerdPersonCatalogTableWidget.columnCount() < 5):
            self.registerdPersonCatalogTableWidget.setColumnCount(5)
        if (self.registerdPersonCatalogTableWidget.rowCount() < 10):
            self.registerdPersonCatalogTableWidget.setRowCount(10)
        self.registerdPersonCatalogTableWidget.setObjectName(u"registerdPersonCatalogTableWidget")
        self.registerdPersonCatalogTableWidget.setGeometry(QRect(10, 240, 531, 331))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.registerdPersonCatalogTableWidget.setFont(font1)
        self.registerdPersonCatalogTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.registerdPersonCatalogTableWidget.setRowCount(10)
        self.registerdPersonCatalogTableWidget.setColumnCount(5)
        self.registerdPersonsLabel = QLabel(self.studentTab)
        self.registerdPersonsLabel.setObjectName(u"registerdPersonsLabel")
        self.registerdPersonsLabel.setGeometry(QRect(10, 210, 141, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.registerdPersonsLabel.setFont(font2)
        self.savePrersonPushButton = QPushButton(self.studentTab)
        self.savePrersonPushButton.setObjectName(u"savePrersonPushButton")
        self.savePrersonPushButton.setGeometry(QRect(300, 140, 71, 23))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.savePrersonPushButton.setFont(font3)
        self.savePrersonPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePrersonPushButton.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.studentTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 10, 181, 151))
        self.studentInputsLayout = QVBoxLayout(self.layoutWidget)
        self.studentInputsLayout.setObjectName(u"studentInputsLayout")
        self.studentInputsLayout.setContentsMargins(0, 0, 0, 0)
        self.ssnLineEdit = QLineEdit(self.layoutWidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setFont(font1)

        self.studentInputsLayout.addWidget(self.ssnLineEdit)

        self.firstNameLineEdit = QLineEdit(self.layoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setFont(font1)

        self.studentInputsLayout.addWidget(self.firstNameLineEdit)

        self.lastNameLineEdit = QLineEdit(self.layoutWidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setFont(font1)

        self.studentInputsLayout.addWidget(self.lastNameLineEdit)

        self.groupComboBox = QComboBox(self.layoutWidget)
        self.groupComboBox.setObjectName(u"groupComboBox")
        self.groupComboBox.setFont(font1)

        self.studentInputsLayout.addWidget(self.groupComboBox)

        self.veachelClassLineEdit = QLineEdit(self.layoutWidget)
        self.veachelClassLineEdit.setObjectName(u"veachelClassLineEdit")
        self.veachelClassLineEdit.setFont(font1)

        self.studentInputsLayout.addWidget(self.veachelClassLineEdit)

        self.layoutWidget1 = QWidget(self.studentTab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 105, 151))
        self.studetsLabelVerticalLayout = QVBoxLayout(self.layoutWidget1)
        self.studetsLabelVerticalLayout.setObjectName(u"studetsLabelVerticalLayout")
        self.studetsLabelVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ssnLabel = QLabel(self.layoutWidget1)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setFont(font2)

        self.studetsLabelVerticalLayout.addWidget(self.ssnLabel)

        self.firstNameLabel = QLabel(self.layoutWidget1)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setFont(font2)

        self.studetsLabelVerticalLayout.addWidget(self.firstNameLabel)

        self.lastNameLabel = QLabel(self.layoutWidget1)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font2)

        self.studetsLabelVerticalLayout.addWidget(self.lastNameLabel)

        self.groupLabel = QLabel(self.layoutWidget1)
        self.groupLabel.setObjectName(u"groupLabel")
        self.groupLabel.setFont(font2)

        self.studetsLabelVerticalLayout.addWidget(self.groupLabel)

        self.veachelClassLabel = QLabel(self.layoutWidget1)
        self.veachelClassLabel.setObjectName(u"veachelClassLabel")
        self.veachelClassLabel.setFont(font2)

        self.studetsLabelVerticalLayout.addWidget(self.veachelClassLabel)

        self.tabWidget.addTab(self.studentTab, "")
        self.vehicleTab = QWidget()
        self.vehicleTab.setObjectName(u"vehicleTab")
        self.vehicleTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.vehicleListLabel = QLabel(self.vehicleTab)
        self.vehicleListLabel.setObjectName(u"vehicleListLabel")
        self.vehicleListLabel.setGeometry(QRect(20, 220, 71, 16))
        self.vehicleListLabel.setFont(font2)
        self.vehicleCatalogTableWidget = QTableWidget(self.vehicleTab)
        if (self.vehicleCatalogTableWidget.columnCount() < 5):
            self.vehicleCatalogTableWidget.setColumnCount(5)
        if (self.vehicleCatalogTableWidget.rowCount() < 10):
            self.vehicleCatalogTableWidget.setRowCount(10)
        self.vehicleCatalogTableWidget.setObjectName(u"vehicleCatalogTableWidget")
        self.vehicleCatalogTableWidget.setGeometry(QRect(20, 240, 531, 331))
        self.vehicleCatalogTableWidget.setFont(font1)
        self.vehicleCatalogTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.vehicleCatalogTableWidget.setRowCount(10)
        self.vehicleCatalogTableWidget.setColumnCount(5)
        self.savePrersonPushButton_2 = QPushButton(self.vehicleTab)
        self.savePrersonPushButton_2.setObjectName(u"savePrersonPushButton_2")
        self.savePrersonPushButton_2.setGeometry(QRect(320, 130, 81, 23))
        self.savePrersonPushButton_2.setFont(font3)
        self.savePrersonPushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePrersonPushButton_2.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")
        self.savePrersonPushButton_3 = QPushButton(self.vehicleTab)
        self.savePrersonPushButton_3.setObjectName(u"savePrersonPushButton_3")
        self.savePrersonPushButton_3.setGeometry(QRect(320, 100, 81, 23))
        self.savePrersonPushButton_3.setFont(font3)
        self.savePrersonPushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePrersonPushButton_3.setStyleSheet(u"background-color: rgb(217, 145, 0);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget2 = QWidget(self.vehicleTab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(140, 10, 169, 146))
        self.veachelInputsVerticalLayout = QVBoxLayout(self.layoutWidget2)
        self.veachelInputsVerticalLayout.setObjectName(u"veachelInputsVerticalLayout")
        self.veachelInputsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.numberPlateLineEdit = QLineEdit(self.layoutWidget2)
        self.numberPlateLineEdit.setObjectName(u"numberPlateLineEdit")
        self.numberPlateLineEdit.setFont(font1)

        self.veachelInputsVerticalLayout.addWidget(self.numberPlateLineEdit)

        self.manifacturetLineEdit = QLineEdit(self.layoutWidget2)
        self.manifacturetLineEdit.setObjectName(u"manifacturetLineEdit")
        self.manifacturetLineEdit.setFont(font1)

        self.veachelInputsVerticalLayout.addWidget(self.manifacturetLineEdit)

        self.modelLineEdit = QLineEdit(self.layoutWidget2)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setFont(font1)

        self.veachelInputsVerticalLayout.addWidget(self.modelLineEdit)

        self.modelYearLineEdit = QLineEdit(self.layoutWidget2)
        self.modelYearLineEdit.setObjectName(u"modelYearLineEdit")
        self.modelYearLineEdit.setFont(font1)

        self.veachelInputsVerticalLayout.addWidget(self.modelYearLineEdit)

        self.capiacityLineEdit = QLineEdit(self.layoutWidget2)
        self.capiacityLineEdit.setObjectName(u"capiacityLineEdit")
        self.capiacityLineEdit.setFont(font1)

        self.veachelInputsVerticalLayout.addWidget(self.capiacityLineEdit)

        self.layoutWidget3 = QWidget(self.vehicleTab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 10, 108, 151))
        self.veachleLabelVerticalLayout = QVBoxLayout(self.layoutWidget3)
        self.veachleLabelVerticalLayout.setObjectName(u"veachleLabelVerticalLayout")
        self.veachleLabelVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.numberPlateLabel = QLabel(self.layoutWidget3)
        self.numberPlateLabel.setObjectName(u"numberPlateLabel")
        self.numberPlateLabel.setFont(font2)

        self.veachleLabelVerticalLayout.addWidget(self.numberPlateLabel)

        self.manifacturetLabel = QLabel(self.layoutWidget3)
        self.manifacturetLabel.setObjectName(u"manifacturetLabel")
        self.manifacturetLabel.setFont(font2)

        self.veachleLabelVerticalLayout.addWidget(self.manifacturetLabel)

        self.modelLabel = QLabel(self.layoutWidget3)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setFont(font2)

        self.veachleLabelVerticalLayout.addWidget(self.modelLabel)

        self.modelYearLabel = QLabel(self.layoutWidget3)
        self.modelYearLabel.setObjectName(u"modelYearLabel")
        self.modelYearLabel.setFont(font2)

        self.veachleLabelVerticalLayout.addWidget(self.modelYearLabel)

        self.capiacityLabel = QLabel(self.layoutWidget3)
        self.capiacityLabel.setObjectName(u"capiacityLabel")
        self.capiacityLabel.setFont(font2)

        self.veachleLabelVerticalLayout.addWidget(self.capiacityLabel)

        self.tabWidget.addTab(self.vehicleTab, "")
        self.groupTab = QWidget()
        self.groupTab.setObjectName(u"groupTab")
        self.groupTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.saveGroupPushButton = QPushButton(self.groupTab)
        self.saveGroupPushButton.setObjectName(u"saveGroupPushButton")
        self.saveGroupPushButton.setGeometry(QRect(290, 40, 75, 23))
        self.saveGroupPushButton.setFont(font3)
        self.saveGroupPushButton.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")
        self.groupsTableWidget = QTableWidget(self.groupTab)
        if (self.groupsTableWidget.columnCount() < 2):
            self.groupsTableWidget.setColumnCount(2)
        if (self.groupsTableWidget.rowCount() < 10):
            self.groupsTableWidget.setRowCount(10)
        self.groupsTableWidget.setObjectName(u"groupsTableWidget")
        self.groupsTableWidget.setGeometry(QRect(20, 120, 241, 331))
        self.groupsTableWidget.setFont(font1)
        self.groupsTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.groupsTableWidget.setRowCount(10)
        self.groupsTableWidget.setColumnCount(2)
        self.storedGroupsLabel = QLabel(self.groupTab)
        self.storedGroupsLabel.setObjectName(u"storedGroupsLabel")
        self.storedGroupsLabel.setGeometry(QRect(20, 100, 121, 16))
        self.storedGroupsLabel.setFont(font2)
        self.widget = QWidget(self.groupTab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 10, 169, 56))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupNameLineEdit = QLineEdit(self.widget)
        self.groupNameLineEdit.setObjectName(u"groupNameLineEdit")
        self.groupNameLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.groupNameLineEdit)

        self.responsiblePersonLineEdit = QLineEdit(self.widget)
        self.responsiblePersonLineEdit.setObjectName(u"responsiblePersonLineEdit")
        self.responsiblePersonLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.responsiblePersonLineEdit)

        self.widget1 = QWidget(self.groupTab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 10, 81, 61))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupNameLabel = QLabel(self.widget1)
        self.groupNameLabel.setObjectName(u"groupNameLabel")
        self.groupNameLabel.setFont(font2)

        self.verticalLayout_2.addWidget(self.groupNameLabel)

        self.responsiblePersonLabel = QLabel(self.widget1)
        self.responsiblePersonLabel.setObjectName(u"responsiblePersonLabel")
        self.responsiblePersonLabel.setFont(font2)

        self.verticalLayout_2.addWidget(self.responsiblePersonLabel)

        self.tabWidget.addTab(self.groupTab, "")
        self.raportsTab = QWidget()
        self.raportsTab.setObjectName(u"raportsTab")
        self.raportsTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.reportTypeComboBox = QComboBox(self.raportsTab)
        self.reportTypeComboBox.setObjectName(u"reportTypeComboBox")
        self.reportTypeComboBox.setGeometry(QRect(10, 50, 231, 22))
        self.reportTypeComboBox.setFont(font1)
        self.reportTypeLabel = QLabel(self.raportsTab)
        self.reportTypeLabel.setObjectName(u"reportTypeLabel")
        self.reportTypeLabel.setGeometry(QRect(10, 20, 61, 21))
        self.reportTypeLabel.setFont(font2)
        self.beginigDateEdit = QDateEdit(self.raportsTab)
        self.beginigDateEdit.setObjectName(u"beginigDateEdit")
        self.beginigDateEdit.setGeometry(QRect(10, 110, 110, 22))
        self.beginigDateEdit.setFont(font1)
        self.beginigDateEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.beginigDateEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.beginigDateEdit.setCalendarPopup(True)
        self.beginigDateEdit.setDate(QDate(2025, 1, 1))
        self.beginigLabel = QLabel(self.raportsTab)
        self.beginigLabel.setObjectName(u"beginigLabel")
        self.beginigLabel.setGeometry(QRect(10, 90, 47, 13))
        self.beginigLabel.setFont(font2)
        self.endingLabel = QLabel(self.raportsTab)
        self.endingLabel.setObjectName(u"endingLabel")
        self.endingLabel.setGeometry(QRect(130, 90, 47, 13))
        self.endingLabel.setFont(font2)
        self.endingDateEdit = QDateEdit(self.raportsTab)
        self.endingDateEdit.setObjectName(u"endingDateEdit")
        self.endingDateEdit.setGeometry(QRect(130, 110, 110, 22))
        self.endingDateEdit.setFont(font1)
        self.endingDateEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.endingDateEdit.setCalendarPopup(True)
        self.endingDateEdit.setDate(QDate(2025, 1, 1))
        self.reportTableWidget = QTableWidget(self.raportsTab)
        if (self.reportTableWidget.columnCount() < 6):
            self.reportTableWidget.setColumnCount(6)
        if (self.reportTableWidget.rowCount() < 22):
            self.reportTableWidget.setRowCount(22)
        self.reportTableWidget.setObjectName(u"reportTableWidget")
        self.reportTableWidget.setGeometry(QRect(10, 190, 641, 351))
        self.reportTableWidget.setFont(font1)
        self.reportTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.reportTableWidget.setRowCount(22)
        self.reportTableWidget.setColumnCount(6)
        self.reportLabel = QLabel(self.raportsTab)
        self.reportLabel.setObjectName(u"reportLabel")
        self.reportLabel.setGeometry(QRect(10, 170, 71, 16))
        self.reportLabel.setFont(font2)
        self.savePrersonPushButton_4 = QPushButton(self.raportsTab)
        self.savePrersonPushButton_4.setObjectName(u"savePrersonPushButton_4")
        self.savePrersonPushButton_4.setGeometry(QRect(250, 110, 81, 23))
        self.savePrersonPushButton_4.setFont(font3)
        self.savePrersonPushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePrersonPushButton_4.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.raportsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuAsetukset = QMenu(self.menubar)
        self.menuAsetukset.setObjectName(u"menuAsetukset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAsetukset.menuAction())
        self.menuAsetukset.addAction(self.actionMuokkaa)
        self.menuAsetukset.addAction(self.actionTietoja_ohjelmasta)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMuokkaa.setText(QCoreApplication.translate("MainWindow", u"Muokkaa...", None))
#if QT_CONFIG(shortcut)
        self.actionMuokkaa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setText(QCoreApplication.translate("MainWindow", u"Tietoja ohjelmasta...", None))
#if QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.registerdPersonsLabel.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6idyt lainaajat", None))
        self.savePrersonPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.groupLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4", None))
        self.veachelClassLabel.setText(QCoreApplication.translate("MainWindow", u"Ajoneuvoluokka", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.studentTab), QCoreApplication.translate("MainWindow", u"Lainaajat", None))
        self.vehicleListLabel.setText(QCoreApplication.translate("MainWindow", u"Autoluettelo", None))
        self.savePrersonPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.savePrersonPushButton_3.setText(QCoreApplication.translate("MainWindow", u"Viivakoodi", None))
        self.numberPlateLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.manifacturetLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"Malli", None))
        self.modelYearLabel.setText(QCoreApplication.translate("MainWindow", u"Vuosimalli", None))
        self.capiacityLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6m\u00e4\u00e4r\u00e4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vehicleTab), QCoreApplication.translate("MainWindow", u"Autot", None))
        self.saveGroupPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.storedGroupsLabel.setText(QCoreApplication.translate("MainWindow", u"Tallenetut ryhm\u00e4t", None))
        self.groupNameLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4n nimi", None))
        self.responsiblePersonLabel.setText(QCoreApplication.translate("MainWindow", u"Vastuuhenkil\u00f6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupTab), QCoreApplication.translate("MainWindow", u"Ryhm\u00e4t", None))
        self.reportTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Raportti", None))
        self.beginigLabel.setText(QCoreApplication.translate("MainWindow", u"Alkaa", None))
        self.endingLabel.setText(QCoreApplication.translate("MainWindow", u"P\u00e4\u00e4ttyy", None))
        self.reportLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.savePrersonPushButton_4.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.raportsTab), QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.menuAsetukset.setTitle(QCoreApplication.translate("MainWindow", u"Asetukset", None))
    # retranslateUi

