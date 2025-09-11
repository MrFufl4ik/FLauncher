# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 100)
        Form.setMinimumSize(QSize(300, 100))
        Form.setMaximumSize(QSize(300, 100))
        icon = QIcon()
        icon.addFile(u"../assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.installLineEdit = QLineEdit(Form)
        self.installLineEdit.setObjectName(u"installLineEdit")
        self.installLineEdit.setGeometry(QRect(10, 10, 281, 31))
        font = QFont()
        font.setBold(True)
        self.installLineEdit.setFont(font)
        self.installLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"    border: 1px solid #444;\n"
"}")
        self.installPushButton = QPushButton(Form)
        self.installPushButton.setObjectName(u"installPushButton")
        self.installPushButton.setGeometry(QRect(10, 50, 281, 41))
        self.installPushButton.setFont(font)
        self.installPushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #222;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.installLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID \u043c\u043e\u0434\u043f\u0430\u043a\u0430...", None))
        self.installPushButton.setText(QCoreApplication.translate("Form", u"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

