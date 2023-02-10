import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6 import QtGui, QtCore
import speech_recognition as sr

from design1 import Ui_MainWindow
from myhandler import VoiceThreadHandler

import pyttsx3


class MyVoiceHandler(QMainWindow):
    def __init__(self):
        super(MyVoiceHandler, self).__init__()
        self.pressing = None
        self.oldPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # убираем windows рамки
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # действия с web - окном
        self.ui.btn_4.clicked.connect(lambda: self.close())
        self.ui.btn_3.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_2.clicked.connect(self.check_voice)
        self.ui.btn_1.clicked.connect(self.first_but)

        # основные действия бота
        self.ui.btn_mic.clicked.connect(self.check_micro)
        self.ui.btn_go.clicked.connect(self.start_app)
        self.ui.btn_what.clicked.connect(self.about_me)

        # инициализация класса в отдельный поток
        self.thread_func = VoiceThreadHandler()
        self.thread_func.signals.connect(self.signal_handler)

    @staticmethod
    def hello_world():
        print("hi ;)")

    # функция для кнопки "?"
    def first_but(self):
        self.ui.plain_text.clear()
        self.ui.plain_text.appendPlainText('?')

    # нажатие на клавишу мышки
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.oldPos = event.globalPosition()
        self.pressing = True

    # передвижение окна
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.pressing:
            delta = QtCore.QPointF.toPoint(event.globalPosition() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        self.pressing = False

    def closeEvent(self, event):
        event.accept()

    def check_voice(self):
        # self.ui.btn_2.setIcon()
        icon = QIcon()
        icon.addFile("icons/volume2.png", state=QIcon.On)
        icon.addFile("icons/volumg", state=QIcon.Off)

        self.ui.btn_2.setCheckable(True)
        self.ui.btn_2.setIcon(icon)

        if self.ui.btn_2.isChecked():
            self.ui.plain_text.clear()
            self.ui.plain_text.appendPlainText('Звук отключен')

        else:
            self.ui.plain_text.clear()
            self.ui.plain_text.appendPlainText('Звук включен')
            voice_start = pyttsx3.init()
            voice_start.say('Звук включен')
            voice_start.runAndWait()
            voice_start.stop()

    # проверка включенных микрофонов
    def check_micro(self):
        mic_list = sr.Microphone.list_microphone_names()
        if len(mic_list) == 0:
            mic_list = "Нет подключенных микрофонов"
        QMessageBox.about(self, "Подключенные микрофоны: ", str(mic_list).encode("cp1251").decode('utf-8'))

    # функции обрабатываемые ботом
    def about_me(self):
        helper = " " \
                 "\n  You can user next commands: " \
                 "\n " \
                 "\n1) Погода на один или пять дней. " \
                 "\n2) Включить музыку. " \
                 "\n3) Записать заметку"
        self.ui.plain_text.clear()
        self.ui.plain_text.appendPlainText(helper)

    # начать общение с ботом
    def start_app(self):
        if self.ui.btn_go.text().lower() == "let's go":
            self.signal_handler(["start_bot"])
            self.thread_func.handler_status = True
            self.thread_func.start()
        elif self.ui.btn_go.text().lower() == "stop it":
            self.signal_handler(["stop_bot"])
            self.thread_func.handler_status = False
            self.thread_func.terminate()

    # обработка запроса полученных с потока QThread VoiceThreadHandler
    def signal_handler(self, value: list) -> None:
        if value[0] == "start_bot":
            self.ui.plain_text.clear()
            self.ui.plain_text.appendPlainText("\n  Say something..."
                                               "\n")
            self.ui.btn_go.setText("Stop it")

        elif value[0] == "say_some":
            self.ui.plain_text.appendPlainText(value[1])

        elif value[0] == "stop_bot":
            print("Я ЕГО СТОПАНУЛ")
            self.ui.btn_go.setText("Let's go")
            self.ui.plain_text.clear()
            self.ui.plain_text.appendPlainText("\n"
                                               "  To get started, click on \"Let's go\"")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyVoiceHandler()
    window.show()

    sys.exit(app.exec())
