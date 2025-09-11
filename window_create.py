# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_modpack_window.ui'
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
        Form.resize(390, 130)
        Form.setMinimumSize(QSize(390, 130))
        Form.setMaximumSize(QSize(390, 130))
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.pushButton_create = QPushButton(Form)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(10, 90, 371, 31))
        font = QFont()
        font.setBold(True)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setStyleSheet(u"QPushButton {\n"
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
        self.lineEdit_id = QLineEdit(Form)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(10, 10, 371, 31))
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_title_name = QLineEdit(Form)
        self.lineEdit_title_name.setObjectName(u"lineEdit_title_name")
        self.lineEdit_title_name.setGeometry(QRect(10, 50, 371, 31))
        self.lineEdit_title_name.setFont(font)
        self.lineEdit_title_name.setStyleSheet(u"QLineEdit {\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_create.setText(QCoreApplication.translate("Form", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u043e\u0434\u043f\u0430\u043a", None))
        self.lineEdit_id.setInputMask("")
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("Form", u"id \u043c\u043e\u0434\u043f\u0430\u043a\u0430", None))
        self.lineEdit_title_name.setPlaceholderText(QCoreApplication.translate("Form", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u043f\u0430\u043a\u0430 (\u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
    # retranslateUi

