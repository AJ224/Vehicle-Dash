import RPi.GPIO as GPIO 

import time 
GPIO.setmode(GPIO.BCM) 
GPIO_TRIG = 11 
GPIO_ECHO = 18
GPIO.setup(GPIO_TRIG, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN) 
GPIO.output(GPIO_TRIG, GPIO.LOW) 
time.sleep(2) 
GPIO.output(GPIO_TRIG, GPIO.HIGH) 
time.sleep(0.00001) 
GPIO.output(GPIO_TRIG, GPIO.LOW) 
while GPIO.input(GPIO_ECHO)==0: 
    start_time = time.time() 
while GPIO.input(GPIO_ECHO)==1: 
    Bounce_back_time = time.time() 
pulse_duration = Bounce_back_time - start_time 
distance = round(pulse_duration * 17150, 2)

import customtkinter
from tkdial import Meter

app = customtkinter.CTk()
app.geometry("950x350")
customtkinter.set_appearance_mode("Dark") 

meter1 = Meter(app, bg="#242424", radius=300, start=0, end=80, border_width=0,
               fg="black", text_color="white", start_angle=270, end_angle=-270,
               text_font="DS-Digital 30", scale_color="white", needle_color="red")
meter1.set_mark(140, 160) # set red marking from 140 to 160
meter1.grid(row=0, column=1, padx=20, pady=30)
meter1.set(distance)
app.mainloop()
#print (f"Distance: {distance} cm") 
#GPIO.cleanup() 
