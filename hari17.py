import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi List Nama")
        self.setGeometry(100, 100, 400, 300)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.label = QLabel("Daftar Nama", self)
        self.layout.addWidget(self.label)

        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)

        self.input_layout = QHBoxLayout()

        self.input_text = QLineEdit(self)
        self.input_layout.addWidget(self.input_text)

        self.add_button = QPushButton("Tambah Nama", self)
        self.add_button.clicked.connect(self.add_name)
        self.input_layout.addWidget(self.add_button)

        self.layout.addLayout(self.input_layout)

    def add_name(self):
        new_name = self.input_text.text()
        if new_name:
            self.list_widget.addItem(new_name)
            self.input_text.clear()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
