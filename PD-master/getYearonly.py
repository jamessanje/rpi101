from firebase import firebase
import datetime
import pyrebase

#firebaseDb = firebase.FirebaseApplication('https://hvccare-5b4bc.firebaseio.com/')

now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
year_now = datetime.datetime.today().strftime("%Y")
month_now = datetime.datetime.today().strftime("%m")
day_now = datetime.datetime.today().strftime("%d")
date_now = datetime.datetime.today().strftime("%Y-%m-%d")

#result = firebaseDb.put('Realtime_Data',{'Date':date_now} )
#print(result)

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

db.child("Realtime_Data").child(year_now).child(month_now).child(day_now).child(date_now).child(now).set({'Date':now,'Measured_Temp_C':21,'Measured_Humidity':63,'Measured_PHLevel': 5})
