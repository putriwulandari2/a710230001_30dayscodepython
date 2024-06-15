import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class FormApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.name_label = QLabel('Nama:')
        self.name_input = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.onSubmit)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)
        self.setWindowTitle('Form Input')

    def onSubmit(self):
        name = self.name_input.text()
        print('Nama:', name)

app = QApplication(sys.argv)
formApp = FormApp()
formApp.show()
sys.exit(app.exec_())
