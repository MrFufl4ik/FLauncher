# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(305, 210)
        Form.setMinimumSize(QSize(305, 210))
        Form.setMaximumSize(QSize(305, 210))
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255,255,255)\n"
"}")
        self.comboBoxLoader = QComboBox(Form)
        self.comboBoxLoader.setObjectName(u"comboBoxLoader")
        self.comboBoxLoader.setGeometry(QRect(10, 130, 281, 31))
        font = QFont()
        font.setBold(True)
        self.comboBoxLoader.setFont(font)
        self.comboBoxLoader.setStyleSheet(u"QComboBox {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0441\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"   "
                        " subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #333;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 6px solid white;\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    border-top-color: #999;\n"
"}")
        self.comboBoxVersion = QComboBox(Form)
        self.comboBoxVersion.setObjectName(u"comboBoxVersion")
        self.comboBoxVersion.setGeometry(QRect(10, 170, 151, 31))
        self.comboBoxVersion.setFont(font)
        self.comboBoxVersion.setStyleSheet(u"QComboBox {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0441\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"   "
                        " subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #333;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 6px solid white;\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    border-top-color: #999;\n"
"}")
        self.comboBoxVersion.setEditable(False)
        self.lineEditPlayerName = QLineEdit(Form)
        self.lineEditPlayerName.setObjectName(u"lineEditPlayerName")
        self.lineEditPlayerName.setGeometry(QRect(10, 50, 281, 31))
        self.lineEditPlayerName.setFont(font)
        self.lineEditPlayerName.setStyleSheet(u"QLineEdit {\n"
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
        self.pushButtonDone = QPushButton(Form)
        self.pushButtonDone.setObjectName(u"pushButtonDone")
        self.pushButtonDone.setGeometry(QRect(170, 170, 120, 31))
        self.pushButtonDone.setFont(font)
        self.pushButtonDone.setStyleSheet(u"QPushButton {\n"
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
        self.lineEditVisualName = QLineEdit(Form)
        self.lineEditVisualName.setObjectName(u"lineEditVisualName")
        self.lineEditVisualName.setGeometry(QRect(10, 10, 281, 31))
        self.lineEditVisualName.setFont(font)
        self.lineEditVisualName.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEditJavaArgs = QLineEdit(Form)
        self.lineEditJavaArgs.setObjectName(u"lineEditJavaArgs")
        self.lineEditJavaArgs.setGeometry(QRect(10, 90, 281, 31))
        self.lineEditJavaArgs.setFont(font)
        self.lineEditJavaArgs.setStyleSheet(u"QLineEdit {\n"
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
        self.comboBoxLoader.setPlaceholderText("")
        self.comboBoxVersion.setCurrentText("")
        self.comboBoxVersion.setPlaceholderText("")
        self.lineEditPlayerName.setPlaceholderText(QCoreApplication.translate("Form", u"\u0438\u043c\u044f \u0438\u0433\u0440\u043e\u043a\u0430", None))
        self.pushButtonDone.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEditVisualName.setPlaceholderText(QCoreApplication.translate("Form", u"\u0432\u0438\u0437\u0443\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0431\u043e\u0440\u043a\u0438", None))
        self.lineEditJavaArgs.setPlaceholderText(QCoreApplication.translate("Form", u"\u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u044b java", None))
    # retranslateUi

