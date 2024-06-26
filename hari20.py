import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Sederhana dengan PyQt5")
        self.setGeometry(100, 100, 300, 200)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.hello_button = QPushButton("Tampilkan Pesan", self)
        self.hello_button.clicked.connect(self.show_message)
        self.layout.addWidget(self.hello_button)

        self.exit_button = QPushButton("Keluar", self)
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def show_message(self):
        QMessageBox.information(self, "Pesan", "Hai, maniezzzzzz!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
