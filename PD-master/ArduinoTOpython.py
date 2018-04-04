import serial
arduino = serial.Serial('COM10', 115200, timeout=.1)

while True:
    data = arduino.readline().decode().strip() #the last bit gets rid of the new-line chars
    if data:
        print(data)
