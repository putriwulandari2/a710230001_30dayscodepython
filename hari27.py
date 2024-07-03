import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Pemilihan Warna")
        self.setGeometry(100, 100, 400, 200)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.color_button = QPushButton("Pilih Warna", self)
        self.color_button.clicked.connect(self.choose_color)
        self.layout.addWidget(self.color_button)

        self.exit_button = QPushButton("Keluar", self)
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.main_widget.setStyleSheet(f"background-color: {color.name()};")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
