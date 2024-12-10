# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(312, 201)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(16, 10, 86, 141))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.serverLabel = QLabel(self.layoutWidget)
        self.serverLabel.setObjectName(u"serverLabel")
        font = QFont()
        font.setPointSize(10)
        self.serverLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.serverLabel)

        self.portLabel = QLabel(self.layoutWidget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.portLabel)

        self.userLabel = QLabel(self.layoutWidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.userLabel)

        self.databaseLabel = QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.databaseLabel)

        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(120, 10, 181, 146))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.serverLineEdit = QLineEdit(self.layoutWidget_2)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.serverLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.serverLineEdit)

        self.portLineEdit = QLineEdit(self.layoutWidget_2)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.portLineEdit)

        self.databaseLineEdit = QLineEdit(self.layoutWidget_2)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.databaseLineEdit)

        self.userLineEdit = QLineEdit(self.layoutWidget_2)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.userLineEdit)

        self.saveSettingsPushButton = QPushButton(Dialog)
        self.saveSettingsPushButton.setObjectName(u"saveSettingsPushButton")
        self.saveSettingsPushButton.setEnabled(True)
        self.saveSettingsPushButton.setGeometry(QRect(220, 160, 81, 23))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.saveSettingsPushButton.setFont(font2)
        self.saveSettingsPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveSettingsPushButton.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.serverLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.userLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.databaseLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
#if QT_CONFIG(tooltip)
        self.serverLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen nimi tai IP-osoite</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.portLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen porttinumero</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.databaseLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen k\u00e4ytt\u00e4j\u00e4tunnus</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.userLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sovelluksen k\u00e4ytt\u00e4j\u00e4 tunnus</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.saveSettingsPushButton.setToolTip(QCoreApplication.translate("Dialog", u"Tallenna asetukset tiedostoon", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingsPushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
    # retranslateUi

