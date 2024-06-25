import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QCalendarWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QLabel, QMessageBox)
from PyQt5.QtCore import QDate

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.showDate)

        self.date_label = QLabel(self.calendar.selectedDate().toString())
        self.note_edit = QTextEdit()
        self.save_button = QPushButton('Simpan Catatan')
        self.save_button.clicked.connect(self.saveNote)
        self.notes = {} 

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.date_label)
        layout.addWidget(QLabel("Catatan:"))
        layout.addWidget(self.note_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setWindowTitle('Kalender dengan Catatan')

    def showDate(self, date):
        self.date_label.setText(date.toString())
        note = self.notes.get(date.toString(), "")
        self.note_edit.setText(note)

    def saveNote(self):
        date = self.calendar.selectedDate().toString()
        note = self.note_edit.toPlainText()
        self.notes[date] = note

        with open('notes.txt', 'w') as file:
            for date, note in self.notes.items():
                file.write(f'{date}\n{note}\n---\n')

        QMessageBox.information(self, 'Catatan Disimpan', 'Catatan berhasil disimpan!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar_app = CalendarApp()
    calendar_app.show()
    sys.exit(app.exec_())
