# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_modpack_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 205)
        Form.setMinimumSize(QSize(400, 205))
        Form.setMaximumSize(QSize(400, 205))
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.pushButton_create = QPushButton(Form)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(270, 80, 111, 111))
        self.lineEdit_id = QLineEdit(Form)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(10, 10, 371, 22))
        self.lineEdit_title_name = QLineEdit(Form)
        self.lineEdit_title_name.setObjectName(u"lineEdit_title_name")
        self.lineEdit_title_name.setGeometry(QRect(10, 40, 371, 22))
        self.information = QLabel(Form)
        self.information.setObjectName(u"information")
        self.information.setGeometry(QRect(10, 80, 241, 121))
        self.information.setTextFormat(Qt.TextFormat.RichText)
        self.information.setScaledContents(True)
        self.information.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.information.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_create.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u043e\u0434\u043f\u0430\u043a", None))
        self.lineEdit_id.setInputMask("")
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("Form", u"ID \u043c\u043e\u0434\u043f\u0430\u043a\u0430, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 -> exampleModPack \u0438\u043b\u0438 beautfiulPack", None))
        self.lineEdit_title_name.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u043f\u0430\u043a\u0430 (\u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
        self.information.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u044f! \u041f\u0440\u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u043f\u0430\u043a\u0430 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0439\u0442\u0435 \u0447\u0442\u043e: \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u0434\u0436\u0430\u0432\u0430 \u0438 \u0432\u0435\u0440\u0441\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u043c\u043e\u0434\u043f\u0430\u043a\u0430! \u0418 \u0437\u0430\u0434\u0430\u044e\u0442\u0441\u044f \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0445 \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u043c \u043c\u0435\u043d\u044e \u043b\u0430\u0443\u043d\u0447\u0435\u0440\u0430.</p><p>\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u044f :)</p></body></html>", None))
    # retranslateUi

