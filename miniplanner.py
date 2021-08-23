import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget, QTextEdit, QSpinBox, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('miniplanner.ui', self)
        self.events = {}
        self.dates = []
        self.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.listWidget.clear()
        event = self.lineEdit.text()
        time = self.timeEdit.dateTime().toString('HH:mm')
        date = self.calendarWidget.selectedDate()
        date = date.toString('yyyy-MM-dd')
        self.dates.append(date + ' ' + time)
        self.dates = sorted(self.dates)
        self.events[date + ' ' + time] = event
        for elem in self.dates:
            self.listWidget.addItem(f'{elem} - {self.events[elem]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Минипланировщик")
    sys.exit(app.exec())
