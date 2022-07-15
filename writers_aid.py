import sys
import googletrans
import textblob
import pyttsx3

import os
import uuid


from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton, QComboBox, QTextEdit, QMessageBox, QFontComboBox, QFileDialog, QLabel


class ApplicationScreen(QDialog):
    def __init__(self):
        super(ApplicationScreen, self).__init__()
        loadUi("applicationscreen.ui", self)
        self.getstarted.clicked.connect(self.gotomenuscreen)

    def gotomenuscreen(self):
        menuscreen = MenuScreen()
        widget.addWidget(menuscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MenuScreen(QDialog):
    def __init__(self):
        super(MenuScreen, self).__init__()
        loadUi("menuscreen.ui", self)
        self.applicationscreen.clicked.connect(self.gotoapplicationscreen)
        self.detailsscreen.clicked.connect(self.gotodetailsscreen)
        self.translatescreen.clicked.connect(self.gototranslatescreen)
        self.writerscreen.clicked.connect(self.gotowriterscreen)

    def gotoapplicationscreen(self):
        applicationscreen = ApplicationScreen()
        widget.addWidget(applicationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodetailsscreen(self):
        detailsscreen = DetailsScreen()
        widget.addWidget(detailsscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gototranslatescreen(self):
        translatescreen = TranslateScreen()
        widget.addWidget(translatescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotowriterscreen(self):
        writerscreen = WriterScreen()
        widget.addWidget(writerscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DetailsScreen(QDialog):
    def __init__(self):
        super(DetailsScreen, self).__init__()
        loadUi("detailsscreen.ui", self)
        self.translatescreen.clicked.connect(self.gototranslatescreen)
        self.writerscreen.clicked.connect(self.gotowriterscreen)
        self.applicationscreen.clicked.connect(self.gotoapplicationscreen)
        self.backscreen.clicked.connect(self.gotomenuscreen)

    def gotoapplicationscreen(self):
        applicationscreen = ApplicationScreen()
        widget.addWidget(applicationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gototranslatescreen(self):
        translatescreen = TranslateScreen()
        widget.addWidget(translatescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotowriterscreen(self):
        writerscreen = WriterScreen()
        widget.addWidget(writerscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomenuscreen(self):
        menuscreen = MenuScreen()
        widget.addWidget(menuscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
       


class TranslateScreen(QDialog):
    def __init__(self):
        super(TranslateScreen, self).__init__()
        uic.loadUi("translatescreen.ui", self)
        self.applicationscreen.clicked.connect(self.gotoapplicationscreen)
        self.detailsscreen.clicked.connect(self.gotodetailsscreen)
        self.writerscreen.clicked.connect(self.gotowriterscreen)

        self.backscreen.clicked.connect(self.gotomenuscreen)

        self.t_button = self.findChild(QPushButton, "translateButton")
        self.c_button = self.findChild(QPushButton, "clearButton")

        self.combo_1 = self.findChild(QComboBox, "comboBox_1")
        self.combo_2 = self.findChild(QComboBox, "comboBox_2")

        self.text_1 = self.findChild(QTextEdit, "textEdit_1")
        self.text_2 = self.findChild(QTextEdit, "textEdit_2")

        self.m_button = self.findChild(QPushButton, "malevoice")
        self.f_button = self.findChild(QPushButton, "femalevoice")

        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)

        self.m_button.clicked.connect(self.speakbutton_m)
        self.f_button.clicked.connect(self.speakbutton_f)

        self.languages = googletrans.LANGUAGES
        #print(self.languages)

        self.language_list = list(self.languages.values())

        self.combo_1.addItems(self.language_list)
        self.combo_2.addItems(self.language_list)

        self.combo_1.setCurrentText("english")
        self.combo_2.setCurrentText("german")


    def clear(self):
        self.textEdit_1.setText("")
        self.textEdit_2.setText("")

        self.combo_1.setCurrentText("english")
        self.combo_2.setCurrentText("german")

    def translate(self):
        try:
            for key,value in self.languages.items():
                if (value == self.combo_1.currentText()):
                    from_language_key = key

            for key,value in self.languages.items():
                if (value == self.combo_2.currentText()):
                    to_language_key = key


            #self.text_1.setText(from_language_key)
            #self.text_2.setText(to_language_key)


            words = textblob.TextBlob(self.text_1.toPlainText())
            words = words.translate(from_lang=from_language_key, to=to_language_key)

            self.text_2.setText(str(words))
            speechengine = pyttsx3.init()            
            speechengine.say(words)
            speechengine.runAndWait()


        except Exception as e:
            QMessageBox.about(self, "Notice", str(e))

    def speakbutton_m(self):
        words = self.text_1.toPlainText()

        self.languages.items()
        self.combo_1.currentText()

        self.text_1.setText(str(words))
        speechengine = pyttsx3.init()            
        speechengine.say(words)
        speechengine.runAndWait()

    def speakbutton_f(self):
        words = self.text_2.toPlainText()

        self.languages.items()
        self.combo_1.currentText()

        self.text_2.setText(str(words))
        speechengine = pyttsx3.init()            
        speechengine.say(words)
        speechengine.runAndWait()

    def gotomenuscreen(self):
        menuscreen = MenuScreen()
        widget.addWidget(menuscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoapplicationscreen(self):
        applicationscreen = ApplicationScreen()
        widget.addWidget(applicationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodetailsscreen(self):
        detailsscreen = DetailsScreen()
        widget.addWidget(detailsscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotowriterscreen(self):
        writerscreen = WriterScreen()
        widget.addWidget(writerscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)



# main
app = QApplication(sys.argv)
welcome=ApplicationScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
app.setApplicationName("Writers Aid")
widget.setFixedHeight(550)
widget.setFixedWidth(700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
