# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordDialog.ui'
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
        Dialog.resize(334, 137)
        self.savePasswordPushButton = QPushButton(Dialog)
        self.savePasswordPushButton.setObjectName(u"savePasswordPushButton")
        self.savePasswordPushButton.setGeometry(QRect(210, 80, 75, 23))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.savePasswordPushButton.setFont(font)
        self.savePasswordPushButton.setStyleSheet(u"background-color: rgb(55, 154, 220);\n"
"color: rgb(255, 255, 255);")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 92, 51))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.oldPasswordLabel = QLabel(self.widget)
        self.oldPasswordLabel.setObjectName(u"oldPasswordLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.oldPasswordLabel.setFont(font1)

        self.verticalLayout.addWidget(self.oldPasswordLabel)

        self.newPasswordLabel = QLabel(self.widget)
        self.newPasswordLabel.setObjectName(u"newPasswordLabel")
        self.newPasswordLabel.setFont(font1)

        self.verticalLayout.addWidget(self.newPasswordLabel)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(120, 10, 169, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.oldPasswordLineEdit = QLineEdit(self.widget1)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        font2 = QFont()
        font2.setPointSize(11)
        self.oldPasswordLineEdit.setFont(font2)

        self.verticalLayout_2.addWidget(self.oldPasswordLineEdit)

        self.newPasswordLineEdit = QLineEdit(self.widget1)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setFont(font2)

        self.verticalLayout_2.addWidget(self.newPasswordLineEdit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.savePasswordPushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.oldPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Vanha salasana", None))
        self.newPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Uusi salasana", None))
        self.oldPasswordLineEdit.setText("")
    # retranslateUi

