import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Temperature Converter')

        self.layout = QVBoxLayout()

        self.input_layout = QHBoxLayout()
        self.celsius_label = QLabel('Celsius:')
        self.celsius_input = QLineEdit()
        self.celsius_input.setPlaceholderText('Masukkan suhu Celsius')
        self.input_layout.addWidget(self.celsius_label)
        self.input_layout.addWidget(self.celsius_input)

        self.convert_button = QPushButton('Konversi')
        self.convert_button.clicked.connect(self.convertTemperature)

        self.result_layout = QVBoxLayout()
        self.fahrenheit_label = QLabel('Fahrenheit:')
        self.kelvin_label = QLabel('Kelvin:')
        self.fahrenheit_result = QLabel()
        self.kelvin_result = QLabel()
        self.result_layout.addWidget(self.fahrenheit_label)
        self.result_layout.addWidget(self.fahrenheit_result)
        self.result_layout.addWidget(self.kelvin_label)
        self.result_layout.addWidget(self.kelvin_result)

        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.convert_button)
        self.layout.addLayout(self.result_layout)

        self.setLayout(self.layout)

    def convertTemperature(self):
        celsius_text = self.celsius_input.text()
        if celsius_text:
            try:
                celsius = float(celsius_text)
                fahrenheit = celsius * 9/5 + 32
                kelvin = celsius + 273.15
                self.fahrenheit_result.setText(f'{fahrenheit:.2f} °F')
                self.kelvin_result.setText(f'{kelvin:.2f} K')
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Masukkan angka yang valid untuk suhu Celsius!')
        else:
            QMessageBox.warning(self, 'Peringatan', 'Masukkan suhu Celsius terlebih dahulu!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())
