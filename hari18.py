import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
import random

class CekKhodamApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
       
        self.setWindowTitle('Cek Khodam')
        self.setGeometry(100, 100, 400, 300)
     
        layout = QVBoxLayout()
       
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Masukkan nama Anda')
        layout.addWidget(self.name_input)
     
        self.label = QLabel('Klik tombol untuk cek khodam', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
       
        self.button = QPushButton('Cek Khodam', self)
        self.button.clicked.connect(self.cekKhodam)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def cekKhodam(self):
      
        khodams = [
            "Khodam Harimau Salto",
            "Khodam Tuyul Mulletttt",
            "Khodam Macan Putih",
            "Khodam Pocong Rayud",
            "Khodam Singa Pedelpop",
            "Khodam Singa Introvet",
        ]
      
        khodam = random.choice(khodams)
      
        name = self.name_input.text()
        
        if name:
            self.label.setText(f'{name}, Khodam Anda: {khodam}')
        else:
            self.label.setText('Masukkan nama Anda terlebih dahulu!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CekKhodamApp()
    ex.show()
    sys.exit(app.exec_())
