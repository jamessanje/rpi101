import pyrebase
config = {
  "apiKey": "AIzaSyCfOVS4fKzugZEv2o26Ir8rjkH2XwayfJo",
  "authDomain": "hvccare-5b4bc.firebaseapp.com",
  "databaseURL": "https://hvccare-5b4bc.firebaseio.com",
  "storageBucket": "hvccare-5b4bc.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



results = db.child("Standard_Parameters").child("1").get()
for value in results.each():
    if value.key() == "Average_Humidity":
        humidity = value.val()

print(humidity)
