import datetime
import pyrebase
import statistics
import serial 
import time
import itertools
import operator


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)


def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

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


#getStandards
crops_suggest = []
name = ""
crop = ""
results = db.child("Standard_Parameters").get()
for value in results.each():
    name = value.key()
    result = db.child("Standard_Parameters").child(value.key()).get()
    for val in result.each():
        if val.key() == "Average_Temp_C":
            if(val.val() == 22.5):
                crops_suggest.append(name)
        if val.key() == "Average_Humidity":
            if(val.val() == 70):
                crops_suggest.append(name)

print(crops_suggest)
        
db.child("Suggested_Crop").update({"Crop_Suggested": most_common(crops_suggest) })
suggested = most_common(crops_suggest)
print(most_common(crops_suggest))

results = db.child("Standard_Parameters").child(suggested).get()
for value in results.each():
    if value.key() == "Average_Temp_C":
        db.child("Sensor_Data_Hackathon").update({"Optimal_Temperature": str(value.val()) })
    if value.key() == "Average_PHLevel":
        db.child("Sensor_Data_Hackathon").update({"Optimal_PhLevel": str(value.val()) })
    if value.key() == "Average_Humidity":
        db.child("Sensor_Data_Hackathon").update({"Optimal_Humidity": str(value.val()) })




tempSensor = 0.0
soilmoistureSensor = 0.0
humiditySensor = 0.0

reference = datetime.datetime.today()

def set_database():
    now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    year_now = datetime.datetime.today().strftime("%Y")
    month_now = datetime.datetime.today().strftime("%m")
    day_now = datetime.datetime.today().strftime("%d")
    date_now = datetime.datetime.today().strftime("%Y-%m-%d")    
    date_name = datetime.datetime.today().strftime("%B %d, %Y")
    time_now = datetime.datetime.today().strftime("%H:%M:%S")

    result = db.child("Realtime_Data_Hackathon").child(year_now).child(month_now).child(day_now).child(date_now).child(now).set({'Date':now,'Time':time_now,'Date_Complete':date_name,'Measured_Temp_C':tempSensor,'Measured_Humidity':humiditySensor,'Measured_PhLevel': soilmoistureSensor})
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
            soilmoistureSensor = float(splitData[1])
            humiditySensor = float(splitData[2])

        if reference <= (datetime.datetime.now() - datetime.timedelta(minutes = 1)):
            set_database()
            reference = datetime.datetime.today()
        
        
                    
        db.child("Sensor_Data_Hackathon").update({"Measured_Temperature": str(tempSensor) })
        db.child("Sensor_Data_Hackathon").update({"Measured_Humidity": str(humiditySensor) })
        db.child("Sensor_Data_Hackathon").update({"Measured_SoilMoisture": str(soilmoistureSensor) })

        
        

        '''
        #print(median_temp-0.5)
        if  tempSensor <= (median_temp-0.5):
            print("#TurnOff Peltier")
            arduino.write('A'.encode())
        elif tempSensor >= (median_temp+1):
            print("#TurnOn Peltier")
            arduino.write('B'.encode())
        elif phSensor <= (median_phlevel-0.5):
            #PhUp TurnedOn
            arduino.write('C'.encode())
        elif phSensor >= (median_phlevel+5):
            #PhDown TurnedOn
            arduino.write('D'.encode())
        elif tempSensor >= (median_temp+2):
            #TurnOn Pump
            arduino.write('E'.encode())
        '''
    except BaseException as error:
        print('An exception occurred: {}'.format(error))        

