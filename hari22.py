import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont

class MoodTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mood_label = QLabel('bagaimana mood mu saat ini:')
        self.mood_label.setFont(QFont('handwritten', 12))

        self.happy_button = QPushButton('😊 Senang')
        self.happy_button.clicked.connect(lambda: self.setMood('Senang'))

        self.sad_button = QPushButton('😢 Sedih')
        self.sad_button.clicked.connect(lambda: self.setMood('Sedih'))

        self.angry_button = QPushButton('😠 Marah')
        self.angry_button.clicked.connect(lambda: self.setMood('Marah'))

        self.mood_display = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.mood_label)
        layout.addWidget(self.happy_button)
        layout.addWidget(self.sad_button)
        layout.addWidget(self.angry_button)
        layout.addWidget(self.mood_display)

        self.setLayout(layout)
        self.setWindowTitle('Mood saat ini')

    def setMood(self, mood):
        self.mood_display.setText(f'Mood sayaa saat ini: {mood}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mood_tracker = MoodTracker()
    mood_tracker.show()
    sys.exit(app.exec_())
