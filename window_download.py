# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(195, 105)
        Form.setMinimumSize(QSize(195, 105))
        Form.setMaximumSize(QSize(195, 105))
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.installLineEdit = QLineEdit(Form)
        self.installLineEdit.setObjectName(u"installLineEdit")
        self.installLineEdit.setGeometry(QRect(10, 10, 171, 21))
        self.installPushButton = QPushButton(Form)
        self.installPushButton.setObjectName(u"installPushButton")
        self.installPushButton.setGeometry(QRect(10, 40, 171, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.installLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u0430\u043a\u043e\u0439 \u043c\u043e\u0434\u043f\u0430\u043a \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c?", None))
        self.installPushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

