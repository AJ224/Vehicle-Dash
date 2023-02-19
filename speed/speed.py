import RPi.GPIO as GPIO
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        # Setting up GPIO
        GPIO.setmode(GPIO.BCM)
        self.rpm_pin = 4
        self.speed_pin = 18
        GPIO.setup(self.rpm_pin, GPIO.IN)
        GPIO.setup(self.speed_pin, GPIO.IN)

        # Setting up GUI
        self.setWindowTitle("Vehicle Dashboard")
        self.setFixedSize(800, 400)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Creating RPM gauge widget
        self.rpm_gauge = QWidget(self.central_widget)
        self.rpm_gauge.setGeometry(100, 100, 200, 200)
        self.rpm_value = 0

        # Creating speedometer gauge widget
        self.speed_gauge = QWidget(self.central_widget)
        self.speed_gauge.setGeometry(500, 100, 200, 200)
        self.speed_value = 0

        # Setting up timer to update gauges
        self.timer = QTimer(self)
        self.timer.setInterval(100) # Update every 0.1 seconds
        self.timer.timeout.connect(self.update_gauges)
        self.timer.start()

    def update_gauges(self):
        # Read RPM and speed values from sensors
        self.rpm_value = GPIO.input(self.rpm_pin)
        self.speed_value = GPIO.input(self.speed_pin)

        # Update RPM gauge
        rpm_painter = QPainter(self.rpm_gauge)
        rpm_painter.setRenderHint(QPainter.Antialiasing)
        rpm_painter.fillRect(0, 0, 200, 200, QBrush(Qt.white))
        rpm_painter.setPen(QPen(Qt.red, 5))
        rpm_painter.drawArc(10, 10, 180, 180, 30 * 16, 300 * 16)
        rpm_painter.setPen(QPen(Qt.black, 5))
        rpm_painter.drawArc(10, 10, 180, 180, 30 * 16, self.rpm_value * 300 * 16)

        # Update speedometer gauge
        speed_painter = QPainter(self.speed_gauge)
        speed_painter.setRenderHint(QPainter.Antialiasing)
        speed_painter.fillRect(0, 0, 200, 200, QBrush(Qt.white))
        speed_painter.setPen(QPen(Qt.blue, 5))
        speed_painter.drawArc(10, 10, 180, 180, 225 * 16, 90 * 16)
        speed_painter.setPen(QPen(Qt.black, 5))
        speed_painter.drawArc(10, 10, 180, 180, 225 * 16, self.speed_value * 90 * 16)

        # Update window title with RPM and speed values
        self.setWindowTitle(f"Vehicle Dashboard (RPM: {self.rpm_value}, Speed: {self.speed_value})")

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()
