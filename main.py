import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer,QTime, Qt
from PyQt6.QtGui import QFont,QFontDatabase

class digitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 300, 100)
        self.time_label = QLabel("12:00:00",self)
        self.timer = QTimer()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label.setStyleSheet("font-size: 130px ; color: #22ff00 ")
        self.setStyleSheet("background-color: black")

        font_name = QFontDatabase.addApplicationFont("font.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_name)[0]
        font = QFont(font_family, 100)

        self.time_label.setFont(font)


        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.updateTime()

    def  updateTime(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss AP')
        self.time_label.setText(display_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = digitalClock()
    clock.show()
    app.exec()