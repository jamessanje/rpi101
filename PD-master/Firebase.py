from firebase import firebase

firebase = firebase.FirebaseApplication('https://hvccare-5b4bc.firebaseio.com/');

result = firebase.get('/Standard_Parameters', '2');

print(result);
