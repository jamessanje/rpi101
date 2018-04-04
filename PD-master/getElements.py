import pyrebase

config = {
  "apiKey": "AIzaSyCfOVS4fKzugZEv2o26Ir8rjkH2XwayfJo",
  "authDomain": "hvccare-5b4bc.firebaseapp.com",
  "databaseURL": "https://hvccare-5b4bc.firebaseio.com",
  "storageBucket": "hvccare-5b4bc.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



results = db.child("Crop_Data").child("Element").order_by_key().limit_to_first(1).get()
for result in results.each():
    index = result.val()
    print(index)

