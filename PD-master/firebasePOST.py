from firebase import firebase

firebase = firebase.FirebaseApplication('https://hvccare-5b4bc.firebaseio.com/');

result = firebase.post('/Data',{'Acidity':'41','Temperature':'15','Humidity':'12'});
print(result);
