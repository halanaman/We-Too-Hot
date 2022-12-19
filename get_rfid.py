# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def get_values():
    rfid,name = "",""
    value = arduino.readline().decode("utf-8") 
    if "UID" in value:
        rfid = value.replace("UID tag : ","").replace("\r\n","")
        value = arduino.readline().decode("utf-8") 
        name = value.replace("Message : ","").replace("\r\n","")
        return rfid , name
    else:
        return "" , ""

"""
while True:
    rfid,name = get_values()
    if rfid != "":
        print(rfid,name)
    
arduino.close()
"""
