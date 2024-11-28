# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.saveSettingspushButton = QPushButton(self.centralwidget)
        self.saveSettingspushButton.setObjectName(u"saveSettingspushButton")
        self.saveSettingspushButton.setGeometry(QRect(210, 160, 101, 31))
        font = QFont()
        font.setPointSize(11)
        self.saveSettingspushButton.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 20, 181, 136))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.serverLineEdit = QLineEdit(self.widget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.serverLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.serverLineEdit)

        self.portLineEdit = QLineEdit(self.widget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.portLineEdit)

        self.databaseLineEdit = QLineEdit(self.widget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.databaseLineEdit)

        self.userLineEdit = QLineEdit(self.widget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.userLineEdit)

        self.paswordLineEdit = QLineEdit(self.widget)
        self.paswordLineEdit.setObjectName(u"paswordLineEdit")
        self.paswordLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.paswordLineEdit)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 20, 86, 131))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ServerLabel = QLabel(self.widget1)
        self.ServerLabel.setObjectName(u"ServerLabel")
        self.ServerLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.ServerLabel)

        self.portLabel = QLabel(self.widget1)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.portLabel)

        self.databaseLabel = QLabel(self.widget1)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.databaseLabel)

        self.userLabel = QLabel(self.widget1)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.userLabel)

        self.passwordLabel = QLabel(self.widget1)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.passwordLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.saveSettingspushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tallentaa asetukset tiedostoon</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingspushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
#if QT_CONFIG(tooltip)
        self.serverLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen nimi tai IP-osoite</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.portLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen porttinumero</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.databaseLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tietokannan nimi</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.userLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sovelluksen k\u00e4ytt\u00e4j\u00e4tunnus</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paswordLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ServerLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
    # retranslateUi

