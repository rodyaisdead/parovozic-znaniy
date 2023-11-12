#синтезатор речи SeechRecognition
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

engine.say('Добро пожаловать в виртуальный тренажёр Поезд Знаний')

engine.runAndWait()
#требуются предустановленные библиотеки! 