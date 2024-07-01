import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox)

class ContactApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contacts')

        self.layout = QVBoxLayout()

        self.input_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Nama kontak')
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText('Nomor telepon')
        self.add_button = QPushButton('Tambah Kontak')
        self.add_button.clicked.connect(self.addContact)
        self.input_layout.addWidget(self.name_input)
        self.input_layout.addWidget(self.phone_input)
        self.input_layout.addWidget(self.add_button)

        self.contact_list = QListWidget()
        self.contact_list.itemDoubleClicked.connect(self.deleteContact)

        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.contact_list)

        self.setLayout(self.layout)

    def addContact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        if name and phone:
            contact_item = QListWidgetItem(f"{name} - {phone}")
            self.contact_list.addItem(contact_item)
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Nama dan nomor telepon tidak boleh kosong!')

    def deleteContact(self, item):
        reply = QMessageBox.question(self, 'Hapus Kontak',
                                     f"Apakah Anda yakin ingin menghapus kontak {item.text()}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.contact_list.takeItem(self.contact_list.row(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    contact_app = ContactApp()
    contact_app.show()
    sys.exit(app.exec_())
