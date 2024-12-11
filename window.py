# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 490)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(808, 490))
        MainWindow.setMaximumSize(QSize(808, 490))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setGeometry(QRect(500, 420, 301, 61))
        self.top_image = QLabel(self.centralwidget)
        self.top_image.setObjectName(u"top_image")
        self.top_image.setGeometry(QRect(10, 10, 601, 401))
        self.top_image.setPixmap(QPixmap(u"assets/emptybanner.png"))
        self.top_image.setScaledContents(True)
        self.pushButton_folder = QPushButton(self.centralwidget)
        self.pushButton_folder.setObjectName(u"pushButton_folder")
        self.pushButton_folder.setGeometry(QRect(220, 420, 61, 61))
        icon1 = QIcon()
        icon1.addFile(u"assets/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_folder.setIcon(icon1)
        self.pushButton_config = QPushButton(self.centralwidget)
        self.pushButton_config.setObjectName(u"pushButton_config")
        self.pushButton_config.setGeometry(QRect(150, 420, 61, 61))
        icon2 = QIcon()
        icon2.addFile(u"assets/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_config.setIcon(icon2)
        self.pushButton_reload = QPushButton(self.centralwidget)
        self.pushButton_reload.setObjectName(u"pushButton_reload")
        self.pushButton_reload.setGeometry(QRect(290, 420, 61, 61))
        icon3 = QIcon()
        icon3.addFile(u"assets/reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_reload.setIcon(icon3)
        self.pushButton_download = QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.setGeometry(QRect(80, 420, 61, 61))
        icon4 = QIcon()
        icon4.addFile(u"assets/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_download.setIcon(icon4)
        self.pushButton_create = QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(10, 420, 61, 61))
        icon5 = QIcon()
        icon5.addFile(u"assets/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_create.setIcon(icon5)
        self.list_view = QListWidget(self.centralwidget)
        self.list_view.setObjectName(u"list_view")
        self.list_view.setGeometry(QRect(620, 10, 181, 401))
        self.pushButton_log = QPushButton(self.centralwidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setGeometry(QRect(360, 420, 61, 61))
        icon6 = QIcon()
        icon6.addFile(u"assets/notepad.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_log.setIcon(icon6)
        self.pushButton_exit = QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(429, 420, 61, 61))
        icon7 = QIcon()
        icon7.addFile(u"assets/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_exit.setIcon(icon7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FLauncher", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.top_image.setText("")
        self.pushButton_folder.setText("")
        self.pushButton_config.setText("")
        self.pushButton_reload.setText("")
        self.pushButton_download.setText("")
        self.pushButton_create.setText("")
        self.pushButton_log.setText("")
        self.pushButton_exit.setText("")
    # retranslateUi

