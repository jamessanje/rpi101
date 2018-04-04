
import datetime
import pyrebase
import statistics
import serial 
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)


config = {
    "apiKey" : "AIzaSyCfOVS4fKzugZEv2o26Ir8rjkH2XwayfJo",
    "authDomain" : "hvccare-5b4bc.firebaseapp.com",
    "databaseURL" : "https://hvccare-5b4bc.firebaseio.com",
    "projectId" : "hvccare-5b4bc",
    "storageBucket": "hvccare-5b4bc.appspot.com",
    "messagingSenderId": "706149028538"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

crops_temp = []
crops_phlevel = []
crops_hum = []


results = db.child("Crop_Data").child("Crop_Name").get()
#print(results)
for result in results.each():
    results = db.child("Standard_Parameters").child(result.val()).get()
    for value in results.each():
        if value.key() == "Average_Temp_C":
            temperature = value.val()
            crops_temp.append(temperature)
        if value.key() == "Average_PHLevel":
            phlevel = value.val()
            crops_phlevel.append(phlevel)
        if value.key() == "Average_Humidity":
            hum = value.val()
            crops_hum.append(hum)

#print(crops_temp)
#print(crops_phlevel)

#print(statistics.median(map(float,crops_temp)))
#print(statistics.median(map(float,crops_phlevel)))

median_temp = statistics.median(map(float,crops_temp))
median_phlevel = statistics.median(map(float,crops_phlevel))
median_hum = statistics.median(map(float,crops_hum))

db.child("Sensor_Data").update({"Optimal_PhLevel": str(median_phlevel) })
db.child("Sensor_Data").update({"Optimal_Temperature": str(median_temp) })
db.child("Sensor_Data").update({"Optimal_Humidity": str(median_hum) })
    
tempSensor = 0.0
phSensor = 0.0
humiditySensor = 0.0

every = 0
reference = datetime.datetime.today()

def set_database():
    now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    year_now = datetime.datetime.today().strftime("%Y")
    month_now = datetime.datetime.today().strftime("%m")
    day_now = datetime.datetime.today().strftime("%d")
    date_now = datetime.datetime.today().strftime("%Y-%m-%d")    
    date_name = datetime.datetime.today().strftime("%B %d, %Y")
    time_now = datetime.datetime.today().strftime("%H:%M:%S")

    result = db.child("Realtime_Data").child(year_now).child(month_now).child(day_now).child(date_now).child(now).set({'Date':now,'Time':time_now,'Date_Complete':date_name,'Measured_Temp_C':tempSensor,'Measured_Humidity':humiditySensor,'Measured_PHLevel': phSensor})
    print(result)

while True:
    try:
        data = arduino.readline().decode().strip()
        
        splitData = data.split()
        print(splitData)
        
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()
        

        if splitData:
            tempSensor = float(splitData[0])
            phSensor = float(splitData[1])
            humiditySensor = float(splitData[2])
            

        

        if reference <= (datetime.datetime.now() - datetime.timedelta(minutes = 1)):
            set_database()
            reference = datetime.datetime.today()
        
            
        db.child("Sensor_Data").update({"Measured_PhLevel": str(phSensor) })
        db.child("Sensor_Data").update({"Measured_Temperature": str(tempSensor) })
        db.child("Sensor_Data").update({"Measured_Humidity": str(humiditySensor) })

        
        #print(median_temp-0.5)
        if  tempSensor <= (median_temp-0.5):
            #TurnOff Peltier
            arduino.write('A'.encode())
        elif tempSensor >= (median_temp+1):
            #TurnOn Peltier
            arduino.write('B'.encode())
        elif phSensor <= (median_phlevel-0.5):
            #PhUp TurnedOn
            arduino.write('C'.encode())
        elif phSensor >= (median_phlevel+5):
            #PhDown TurnedOn
            arduino.write('D'.encode())
    except BaseException as error:
        print('An exception occurred: {}'.format(error))        

