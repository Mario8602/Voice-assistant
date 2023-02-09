################################################################################
## Form generated from reading UI file 'design1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
                               QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)
import file_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(352, 527)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
                                 "	background-color: green;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "background-color: #121212;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
                                         "	color: white;\n"
                                         "	background-color: #121212;\n"
                                         "	font-size: 14pt;\n"
                                         "	font-family: SimSun;\n"
                                         "	font-weight: 600;\n"
                                         "	border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "Cascadia Code\n"
                                         "Kelson Sans\n"
                                         "Mv Boli\n"
                                         "RomanD")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"QFrame {\n"
                                 "	background-color: #121212;\n"
                                 "	border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 331, 134))
        self.layout_but = QGridLayout(self.layoutWidget)
        self.layout_but.setObjectName(u"layout_but")
        self.layout_but.setHorizontalSpacing(0)
        self.layout_but.setVerticalSpacing(2)
        self.layout_but.setContentsMargins(0, 0, 0, 0)
        self.btn_what = QPushButton(self.layoutWidget)
        self.btn_what.setObjectName(u"btn_what")
        self.btn_what.setMinimumSize(QSize(0, 40))
        self.btn_what.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_what.setStyleSheet(u"QPushButton {\n"
                                    "	background-color: #121212;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: #666;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "	background-color: #888;\n"
                                    "}")

        self.layout_but.addWidget(self.btn_what, 8, 0, 1, 1)

        self.btn_go = QPushButton(self.layoutWidget)
        self.btn_go.setObjectName(u"btn_go")
        self.btn_go.setMinimumSize(QSize(0, 40))
        self.btn_go.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go.setStyleSheet(u"QPushButton {\n"
                                  "	background-color: #121212;\n"
                                  "	border: none;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: #666;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "	background-color: #888;\n"
                                  "}\n"
                                  "\n"
                                  "background-color: transparent;")

        self.layout_but.addWidget(self.btn_go, 1, 0, 1, 1)

        self.btn_mic = QPushButton(self.layoutWidget)
        self.btn_mic.setObjectName(u"btn_mic")
        self.btn_mic.setEnabled(True)
        self.btn_mic.setMinimumSize(QSize(0, 38))
        self.btn_mic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mic.setStyleSheet(u"QPushButton {\n"
                                   "	background-color: #121212;\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: #666;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "	background-color: #888;\n"
                                   "}")

        self.layout_but.addWidget(self.btn_mic, 0, 0, 1, 1)

        self.plain_text = QPlainTextEdit(self.frame)
        self.plain_text.setObjectName(u"plain_text")
        self.plain_text.setGeometry(QRect(0, 169, 331, 321))
        self.plain_text.setStyleSheet(u"QPlainTextEdit {\n"
                                      "	background-color: transparent;\n"
                                      "	font-family: SimSun;\n"
                                      "	border: none;\n"
                                      "	color: #888;\n"
                                      "	margin-left: 10px;\n"
                                      "	margin-top: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.plain_text.setReadOnly(True)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 331, 32))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(0, 30))
        self.btn_2.setMaximumSize(QSize(10000000, 300))
        self.btn_2.setStyleSheet(u"QPushButton {\n"
                                 "	background-color: #121212;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/volume2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_2.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(70, 30))
        self.btn_1.setMaximumSize(QSize(1009999, 16777215))
        self.btn_1.setStyleSheet(u"QPushButton {\n"
                                 "	background-color: #121212;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}")

        self.gridLayout_2.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(0, 30))
        self.btn_3.setMaximumSize(QSize(16777215, 16777215))
        self.btn_3.setStyleSheet(u"QPushButton {\n"
                                 "	background-color: #121212;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}")

        self.gridLayout_2.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(40, 30))
        self.btn_4.setMaximumSize(QSize(16777215, 16777215))
        self.btn_4.setStyleSheet(u"QPushButton {\n"
                                 "	background-color: #121212;\n"
                                 "	border: none;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/close3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_4.setIcon(icon1)
        self.btn_4.setIconSize(QSize(18, 18))

        self.gridLayout_2.addWidget(self.btn_4, 0, 3, 1, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VoiceHelper", None))
        self.btn_what.setText(QCoreApplication.translate("MainWindow", u"what?", None))
        self.btn_go.setText(QCoreApplication.translate("MainWindow", u"Let's go", None))
        self.btn_mic.setText(QCoreApplication.translate("MainWindow", u"Check mic", None))
        self.plain_text.setPlainText(QCoreApplication.translate("MainWindow", u"Wake up ;)", None))
        self.btn_2.setText("")
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_4.setText("")
    # retranslateUi
