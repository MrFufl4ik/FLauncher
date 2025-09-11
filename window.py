# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(80000, 49000))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"assets/frog_launcher_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setGeometry(QRect(760, 360, 231, 61))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_folder = QPushButton(self.centralwidget)
        self.pushButton_folder.setObjectName(u"pushButton_folder")
        self.pushButton_folder.setGeometry(QRect(620, 290, 61, 61))
        self.pushButton_folder.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u"assets/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_folder.setIcon(icon1)
        self.pushButton_config = QPushButton(self.centralwidget)
        self.pushButton_config.setObjectName(u"pushButton_config")
        self.pushButton_config.setGeometry(QRect(620, 80, 61, 61))
        self.pushButton_config.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u"assets/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_config.setIcon(icon2)
        self.pushButton_reload = QPushButton(self.centralwidget)
        self.pushButton_reload.setObjectName(u"pushButton_reload")
        self.pushButton_reload.setGeometry(QRect(620, 360, 61, 61))
        self.pushButton_reload.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon3 = QIcon()
        icon3.addFile(u"assets/reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_reload.setIcon(icon3)
        self.pushButton_download = QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.setGeometry(QRect(620, 150, 61, 61))
        self.pushButton_download.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon4 = QIcon()
        icon4.addFile(u"assets/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_download.setIcon(icon4)
        self.pushButton_create = QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(620, 10, 61, 61))
        self.pushButton_create.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon5 = QIcon()
        icon5.addFile(u"assets/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_create.setIcon(icon5)
        self.list_view = QListWidget(self.centralwidget)
        self.list_view.setObjectName(u"list_view")
        self.list_view.setGeometry(QRect(690, 10, 301, 341))
        font1 = QFont()
        font1.setBold(True)
        self.list_view.setFont(font1)
        self.list_view.setStyleSheet(u"QListWidget {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 4px;\n"
"    padding: 8px;\n"
"    margin: 2px;\n"
"    /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    selection-color: white;\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #1a1a1a;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #444;\n"
"    color: white;\n"
"    border: 1px solid #555;\n"
"    /* \u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0443\u0431\u0438\u0440\u0430\u0435\u043c outline \u0438 \u0440\u0430\u043c\u043a\u0443 \u0444\u043e\u043a\u0443\u0441\u0430 */\n"
"    out"
                        "line: none;\n"
"    border: 1px solid #555;\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background-color: #555;\n"
"    outline: none;\n"
"    border: 1px solid #666;\n"
"}\n"
"\n"
"QListWidget::item:selected:focus {\n"
"    outline: none;\n"
"    border: 1px solid #555;\n"
"}\n"
"\n"
"/* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e: \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 \u0434\u043b\u044f \u0441\u0430\u043c\u043e\u0433\u043e \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"QListWidget:focus {\n"
"    outline: none;\n"
"    border: 1px solid #333;\n"
"}\n"
"\n"
"QListWidget::item:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #1a1a1a;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:ver"
                        "tical {\n"
"    background: #444;\n"
"    border-radius: 6px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #555;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 0px;\n"
"}")
        self.pushButton_log = QPushButton(self.centralwidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setGeometry(QRect(620, 220, 61, 61))
        self.pushButton_log.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon6 = QIcon()
        icon6.addFile(u"assets/notepad.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_log.setIcon(icon6)
        self.pushButton_exit = QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(690, 360, 61, 61))
        self.pushButton_exit.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
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
        icon7 = QIcon()
        icon7.addFile(u"assets/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_exit.setIcon(icon7)
        self.picMain_2 = QLabel(self.centralwidget)
        self.picMain_2.setObjectName(u"picMain_2")
        self.picMain_2.setGeometry(QRect(0, 0, 1001, 441))
        self.picMain_2.setPixmap(QPixmap(u"assets/background.png"))
        self.picMain_2.setScaledContents(True)
        self.labelChangelog = QLabel(self.centralwidget)
        self.labelChangelog.setObjectName(u"labelChangelog")
        self.labelChangelog.setGeometry(QRect(10, 10, 601, 411))
        font2 = QFont()
        font2.setPointSize(12)
        self.labelChangelog.setFont(font2)
        self.labelChangelog.setAutoFillBackground(False)
        self.labelChangelog.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background: rgba(0,0,0,191);\n"
"	border: 1px solid #333;\n"
"	border-radius: 6px;\n"
"	padding: 8px 16px;\n"
"}")
        self.labelChangelog.setTextFormat(Qt.TextFormat.MarkdownText)
        self.labelChangelog.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelChangelog.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.picMain_2.raise_()
        self.pushButton_run.raise_()
        self.pushButton_folder.raise_()
        self.pushButton_config.raise_()
        self.pushButton_reload.raise_()
        self.pushButton_download.raise_()
        self.pushButton_create.raise_()
        self.list_view.raise_()
        self.pushButton_log.raise_()
        self.pushButton_exit.raise_()
        self.labelChangelog.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FLauncher Outed Edition", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_folder.setText("")
        self.pushButton_config.setText("")
        self.pushButton_reload.setText("")
        self.pushButton_download.setText("")
        self.pushButton_create.setText("")
        self.pushButton_log.setText("")
        self.pushButton_exit.setText("")
        self.picMain_2.setText("")
        self.labelChangelog.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0440\u0438\u0432\u0435\u0442 <span style=\" font-weight:700;\">\u0434\u043e\u0440\u043e\u0433\u043e\u0439 \u0438\u043c\u043f\u0435\u0440\u0435\u0446!</span> \u0432 \u0441\u0432\u044f\u0437\u0438 \u0441 \u0443\u0436\u0430\u0441\u043d\u0435\u0439\u0448\u0435\u0439 \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u043e\u0439 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 FLauncher, <span style=\" font-weight:700;\">\u044f mrfufl4ik</span>, \u043f\u0440\u0435\u043a\u0440\u0430\u0449\u0430\u044e \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0443 \u043c\u043e\u0440\u0430\u043b\u044c\u043d\u043e \u0443\u0441\u0442\u0430\u0440\u0435\u0432\u0448\u043e\u0439 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438. \u041d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442 \u0443\u0436\u0435 \u0433\u043e\u0442\u043e\u0432\u0438\u0442\u0441\u044f \u043d\u0430 \u0435\u0433\u043e \u0437\u0430\u043c\u0435\u043d\u0443 \u0438\u043c\u044f \u0435\u0433\u043e FLauncher Beta "
                        "(\u043f\u043e\u043a\u0430 \u0435\u0449\u0451 \u043d\u0435 \u0438\u043c\u0435\u0435\u0442 \u043f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u043e\u0433\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f) \u0440\u0430\u0437\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 github, \u0438 \u043b\u044e\u0431\u043e\u0439 \u0436\u0435\u043b\u0430\u044e\u0449\u0438\u0439 \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438: <a href=\"https://github.com/MrFufl4ik/FLauncherBeta\"><span style=\" text-decoration: underline; color:#2980b9;\">https://github.com/mrfufl4ik/fLauncherbeta</span></a>. <span style=\" font-weight:700;\">\u0432 \u0441\u0432\u044f\u0437\u0438 \u0441 \u0442\u0435\u043c \u0447\u0442\u043e \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u043e \u0432\u044b\u0448\u0435, \u044f \u043e\u0444\u0438\u0446\u0430\u043b\u044c\u043d"
                        "\u043e \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u044e \u043f\u0440\u043e\u0435\u043a\u0442 FLauncher</span>. \u043e\u043d \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442, \u0438 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0437\u0430\u0433\u043b\u0443\u0448\u043a\u043e\u0439, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0443\u043c\u0435\u0435\u0442 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043a\u0443\u0431\u044b, \u0434\u0430 \u0438 \u0432\u043f\u0440\u0438\u043d\u0446\u0435\u043f\u0435 \u0432\u0441\u0451. \u0441\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u043f\u043e\u043d\u0438\u043c\u0430\u043d\u0438\u0435!</p></body></html>", None))
    # retranslateUi

