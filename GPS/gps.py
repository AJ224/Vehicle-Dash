#https://www.engineersgarage.com/articles-raspberry-pi-neo-6m-gps-module-interfacing/

import serial              
from time import sleep
import sys

ser = serial.Serial (ā/dev/ttyS0ā)
try:
    while True:
        received_data = (str)(ser.readline()) #read NMEA string received
        print(received_data, ā\nā)
except KeyboardInterrupt:
    sys.exit(0)  
