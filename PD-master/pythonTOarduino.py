import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('COM10', 9600, timeout=.1)


while True:
    data = arduino.readline().decode().strip() #the last bit gets rid of the new-line chars
    print(data)
    splitData = data.split()
   
    
    if not splitData:
        print()
    else:
        tempSensor = float(splitData[0])
        phSensor = float(splitData[1])
        
    
    if tempSensor =="22.":
        print(data)
        arduino.write('H'.encode()) 
    elif data =="4.82":
        print(data)
        arduino.write('L'.encode())
