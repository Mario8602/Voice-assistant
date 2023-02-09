import os
import random

# библиотека для распознавания речи
import speech_recognition as sr
from PySide6.QtCore import QThread, Signal

# библиотека машинного обучения
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

import words
from sweatweather import five_days, one_days, finding_definitions


class VoiceThreadHandler(QThread):
    pause_threshold = 0.5
    signals = Signal(list)
    handler_status = True

    def run(self):

        # инициализация метода CountVectorizer
        vectorizer = CountVectorizer()
        vector = vectorizer.fit_transform(list(words.data_set.keys()))

        clf = LogisticRegression()
        clf.fit(vector, list(words.data_set.values()))

        # del words.data_set

        while True:
            try:
                if self.handler_status:
                    self.rec = sr.Recognizer()
                    self.rec.pause_threshold = 0.5

                    with sr.Microphone() as micro:
                        print('Слушаю')
                        self.rec.adjust_for_ambient_noise(source=micro, duration=0.5)
                        voice = self.rec.listen(source=micro)

                        try:
                            get_voice = self.rec.recognize_google(audio_data=voice, language="ru-RU").lower()
                            say_some = f'YOU: {get_voice}'
                            self.signals.emit(['say_some', say_some])
                            self.main_fun(get_voice, vectorizer, clf)

                        except Exception as error:
                            print(error)
                else:
                    break
            except Exception as error:
                print(error)
                self.signals.emit(['stop_bot'])
                break

    def main_fun(self, get_voice, vectorizer, clf):
        name = words.NAME_ROBOT.intersection(get_voice.split())
        print(name)
        if name:
            get_voice.replace(list(name)[0], '')
            vector_text = vectorizer.transform([get_voice]).toarray()[0]
            bot_answer = clf.predict([vector_text])[0]
            name_of_func = bot_answer.split()[0]
            if name_of_func == "wiki_definitions":
                definition = get_voice.split()[-1]
                func_on = f'self.{name_of_func}("{definition}")'
            else:
                func_on = f'self.{name_of_func}()'
            exec(func_on)
        else:
            return 'Error'

    def qualia(self):
        path_file = fr"C:\Users\Marat\Desktop\music"
        name_file = os.listdir(path_file)
        os.system(fr"{path_file}\{random.choice(name_file)}")
        return "Файл открыт"

    def weather_day(self):
        d = one_days()
        self.signals.emit(['say_some', d])

    def weather_five(self):
        d = five_days()
        return d

    # функция поиска определений
    def wiki_definitions(self, word):
        result = finding_definitions(word)
        self.signals.emit(['say_some', result])
        # print(result)
