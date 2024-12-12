# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 148)
        Form.setMinimumSize(QSize(300, 148))
        Form.setMaximumSize(QSize(300, 148))
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.comboBoxLoader = QComboBox(Form)
        self.comboBoxLoader.setObjectName(u"comboBoxLoader")
        self.comboBoxLoader.setGeometry(QRect(60, 40, 231, 22))
        self.comboBoxVersion = QComboBox(Form)
        self.comboBoxVersion.setObjectName(u"comboBoxVersion")
        self.comboBoxVersion.setGeometry(QRect(60, 60, 231, 22))
        self.comboBoxVersion.setEditable(False)
        self.lineEditPlayerName = QLineEdit(Form)
        self.lineEditPlayerName.setObjectName(u"lineEditPlayerName")
        self.lineEditPlayerName.setGeometry(QRect(10, 91, 161, 21))
        self.pushButtonDone = QPushButton(Form)
        self.pushButtonDone.setObjectName(u"pushButtonDone")
        self.pushButtonDone.setGeometry(QRect(175, 90, 120, 50))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 61, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 61, 20))
        self.lineEditVisualName = QLineEdit(Form)
        self.lineEditVisualName.setObjectName(u"lineEditVisualName")
        self.lineEditVisualName.setGeometry(QRect(10, 10, 281, 21))
        self.lineEditJavaArgs = QLineEdit(Form)
        self.lineEditJavaArgs.setObjectName(u"lineEditJavaArgs")
        self.lineEditJavaArgs.setGeometry(QRect(10, 120, 161, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBoxLoader.setPlaceholderText("")
        self.comboBoxVersion.setCurrentText("")
        self.comboBoxVersion.setPlaceholderText("")
        self.lineEditPlayerName.setPlaceholderText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0438\u0433\u0440\u043e\u043a\u0430", None))
        self.pushButtonDone.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0430\u0434\u0435\u0440:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.lineEditVisualName.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0438\u0437\u0443\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0431\u043e\u0440\u043a\u0438", None))
        self.lineEditJavaArgs.setPlaceholderText(QCoreApplication.translate("Form", u"\u0410\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u044b Java", None))
    # retranslateUi

