import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication
from loguru import logger
from RandomMeovSentence import Sentence
from Forms import Ui_Form

"""
Преобразование uic -> py: pyuic5 Forms/TextForm.ui -o Forms/TextForm.py
Создание requirements файла: pip3 freeze > requirements.txt
"""

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        logger.info(f"Объектное окружение установлено: {self.ui}")

        self.sentence = Sentence()
        logger.info(f"Объект Sentence создан: {self.sentence}")

        self.ui.pushButton.clicked.connect(lambda: self.add_text())

    @logger.catch()
    @pyqtSlot()
    def add_text(self):
        logger.info(f"Метод {self.add_text} использован")

        _sentence = self.sentence.sentence()
        logger.info(f"ПРЕДЛОЖЕНИЕ ДЛЯ ВСТАВКИ ПОЛУЧЕНО: {_sentence}")

        _metric = QFontMetrics(self.ui.label_2.font())
        logger.info(f"Получен объект метрики текста: {_metric}")

        _elided = _metric.elidedText(_sentence, Qt.ElideRight, self.ui.label_2.width())
        logger.info(f"Объект _elided создан: {_elided}")

        self.ui.label_2.setText(str(_elided))


if __name__ == '__main__':
    logger.info("Программа запускается")

    _app = QApplication(sys.argv)
    _app.setStyle("Fusion")
    _window = MainWindow()
    _window.show()

    logger.info("Программа запущена")

    sys.exit(_app.exec_())
