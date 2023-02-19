import sys
import Adafruit_DHT
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.temp_label = QLabel("Temperature: ")
        self.humidity_label = QLabel("Humidity: ")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.temp_label)
        self.layout().addWidget(self.humidity_label)

        # Set up QTimer to update GUI every 5 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(5000)

    def update_data(self):
        # Read data from DHT11 sensor and update GUI
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature is not None:
            self.temp_label.setText(f"Temperature: {temperature:.1f} °C")
            self.humidity_label.setText(f"Humidity: {humidity:.1f}%")
        else:
            self.temp_label.setText("Failed to read temperature and humidity")
            self.humidity_label.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

'''
In this example, we first import the Adafruit_DHT library to read data from the DHT11 sensor connected to the Raspberry Pi. We then create a PyQt5 GUI with two QLabel widgets to display the temperature and humidity readings from the sensor.

We set up a QTimer object to call the update_data method every 5 seconds. The update_data method reads the temperature and humidity data from the DHT11 sensor using the read_retry function from the Adafruit_DHT library, and updates the QLabel widgets with the new data.

When you run this code on a Raspberry Pi with a DHT11 sensor connected to pin 4, it will display a simple PyQt5 GUI with two QLabel widgets that display the temperature and humidity readings from the sensor. The GUI will update every 5 seconds with new readings from the sensor. You can modify the code to read and update other data from other sensors connected to the Raspberry Pi, and adjust the QTimer interval as needed.
'''
