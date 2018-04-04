import time
import datetime
import pyrebase

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



x = 0

def some_job():
    now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    year_now = datetime.datetime.today().strftime("%Y")
    month_now = datetime.datetime.today().strftime("%m")
    day_now = datetime.datetime.today().strftime("%d")
    date_now = datetime.datetime.today().strftime("%Y-%m-%d")    
    date_name = datetime.datetime.today().strftime("%B %d, %Y")
    

    
    result = db.child("Realtime_Data").child(year_now).child(month_now).child(day_now).child(date_now).child(now).set({'Date':now,'Date_Complete':date_name,'Measured_Temp_C':19,'Measured_Humidity':70,'Measured_PHLevel': 7})
    print(result)

while True:
    if x == 600:
        some_job()
        x = 0
        
    time.sleep(1)
    x = x + 1



    
