from firebase import firebase

firebase = firebase.FirebaseApplication('https://hvccare-5b4bc.firebaseio.com/')


result = firebase.put('Standard_Parameters','Strawberry',{'Crop_Name':'Strawberry',
                                                 'Lowest_Opt_Temp_C':18,
                                                 'Average_Temp_C':21,
                                                 'Highest_Opt_Temp_C':24,
                                                 'Lowest_Opt_Humidity':70,
                                                 'Average_Humidity':80,
                                                 'Highest_Opt_Humidity':90,
                                                 'Lowest_Opt_HeatIndex_C':18,
                                                 'Average_HeatIndex_C':21,
                                                 'Highest_Opt_HeatIndex_C':21,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6.5})

result11 = firebase.put('Standard_Parameters','Lettuce',{'Crop_Name':'Lettuce',
                                                 'Lowest_Opt_Temp_C':18,
                                                 'Average_Temp_C':21,
                                                 'Highest_Opt_Temp_C':24,
                                                 'Lowest_Opt_Humidity':80,
                                                 'Average_Humidity':65,
                                                 'Highest_Opt_Humidity':80,
                                                 'Lowest_Opt_HeatIndex_C':17,
                                                 'Average_HeatIndex_C':21,
                                                 'Highest_Opt_HeatIndex_C':25,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':7,
                                                 'Highest_Opt_PHLevel':8})


result12 = firebase.put('Standard_Parameters','Basil',{'Crop_Name':'Basil',
                                                 'Lowest_Opt_Temp_C':20,
                                                 'Average_Temp_C':22.5,
                                                 'Highest_Opt_Temp_C':25,
                                                 'Lowest_Opt_Humidity':60,
                                                 'Average_Humidity':70,
                                                 'Highest_Opt_Humidity':80,
                                                 'Lowest_Opt_HeatIndex_C':20,
                                                 'Average_HeatIndex_C':23,
                                                 'Highest_Opt_HeatIndex_C':26,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6.5})

result1 = firebase.put('Standard_Parameters','Beans and Peas',{'Crop_Name':'Beans and Peas',
                                                 'Lowest_Opt_Temp_C':22,
                                                 'Average_Temp_C':24,
                                                 'Highest_Opt_Temp_C':26,
                                                 'Lowest_Opt_Humidity':60,
                                                 'Average_Humidity':70,
                                                 'Highest_Opt_Humidity':80,
                                                 'Lowest_Opt_HeatIndex_C':22,
                                                 'Average_HeatIndex_C':24,
                                                 'Highest_Opt_HeatIndex_C':28,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6.25,
                                                 'Highest_Opt_PHLevel':7})

result2 = firebase.put('Standard_Parameters','Broccoli',{'Crop_Name':'Broccoli',
                                                 'Lowest_Opt_Temp_C':18,
                                                 'Average_Temp_C':21.5,
                                                 'Highest_Opt_Temp_C':25,
                                                 'Lowest_Opt_Humidity':90,
                                                 'Average_Humidity':92.5,
                                                 'Highest_Opt_Humidity':95,
                                                 'Lowest_Opt_HeatIndex_C':18,
                                                 'Average_HeatIndex_C':22,
                                                 'Highest_Opt_HeatIndex_C':26,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':6.5,
                                                 'Highest_Opt_PHLevel':7})


result3 = firebase.put('Standard_Parameters','Cabbage',{'Crop_Name':'Cabbage',
                                                 'Lowest_Opt_Temp_C':15,
                                                 'Average_Temp_C':20,
                                                 'Highest_Opt_Temp_C':25,
                                                 'Lowest_Opt_Humidity':80,
                                                 'Average_Humidity':87.5,
                                                 'Highest_Opt_Humidity':95,
                                                 'Lowest_Opt_HeatIndex_C':15,
                                                 'Average_HeatIndex_C':20,
                                                 'Highest_Opt_HeatIndex_C':26,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':6.6,
                                                 'Highest_Opt_PHLevel':7.2})


result4 = firebase.put('Standard_Parameters','Cauliflower',{'Crop_Name':'Cauliflower',
                                                 'Lowest_Opt_Temp_C':20,
                                                 'Average_Temp_C':22.5,
                                                 'Highest_Opt_Temp_C':25,
                                                 'Lowest_Opt_Humidity':90,
                                                 'Average_Humidity':92.5,
                                                 'Highest_Opt_Humidity':95,
                                                 'Lowest_Opt_HeatIndex_C':20,
                                                 'Average_HeatIndex_C':23,
                                                 'Highest_Opt_HeatIndex_C':26,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6})


result5 = firebase.put('Standard_Parameters','Cucumber',{'Crop_Name':'Cucumber',
                                                 'Lowest_Opt_Temp_C':18,
                                                 'Average_Temp_C':19,
                                                 'Highest_Opt_Temp_C':20,
                                                 'Lowest_Opt_Humidity':65,
                                                 'Average_Humidity':75,
                                                 'Highest_Opt_Humidity':85,
                                                 'Lowest_Opt_HeatIndex_C':18,
                                                 'Average_HeatIndex_C':19,
                                                 'Highest_Opt_HeatIndex_C':20,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6.5})

result6 = firebase.put('Standard_Parameters','Eggplant',{'Crop_Name':'Eggplant',
                                                 'Lowest_Opt_Temp_C':15,
                                                 'Average_Temp_C':20.5,
                                                 'Highest_Opt_Temp_C':26,
                                                 'Lowest_Opt_Humidity':65,
                                                 'Average_Humidity':72.5,
                                                 'Highest_Opt_Humidity':80,
                                                 'Lowest_Opt_HeatIndex_C':14,
                                                 'Average_HeatIndex_C':21,
                                                 'Highest_Opt_HeatIndex_C':28,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6.25,
                                                 'Highest_Opt_PHLevel':7})


result7 = firebase.put('Standard_Parameters','Mangold',{'Crop_Name':'Mangold',
                                                 'Lowest_Opt_Temp_C':16,
                                                 'Average_Temp_C':20,
                                                 'Highest_Opt_Temp_C':24,
                                                 'Lowest_Opt_Humidity':50,
                                                 'Average_Humidity':65,
                                                 'Highest_Opt_Humidity':80,
                                                 'Lowest_Opt_HeatIndex_C':15,
                                                 'Average_HeatIndex_C':20,
                                                 'Highest_Opt_HeatIndex_C':25,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':6.75,
                                                 'Highest_Opt_PHLevel':7.5})


result8 = firebase.put('Standard_Parameters','Parsley',{'Crop_Name':'Parsley',
                                                 'Lowest_Opt_Temp_C':20,
                                                 'Average_Temp_C':22.5,
                                                 'Highest_Opt_Temp_C':25,
                                                 'Lowest_Opt_Humidity':60,
                                                 'Average_Humidity':65,
                                                 'Highest_Opt_Humidity':70,
                                                 'Lowest_Opt_HeatIndex_C':20,
                                                 'Average_HeatIndex_C':23,
                                                 'Highest_Opt_HeatIndex_C':25,
                                                 'Lowest_Opt_PHLevel':6,
                                                 'Average_PHLevel':6.5,
                                                 'Highest_Opt_PHLevel':7})

result9 = firebase.put('Standard_Parameters','Peppers',{'Crop_Name':'Peppers',
                                                 'Lowest_Opt_Temp_C':22,
                                                 'Average_Temp_C':26,
                                                 'Highest_Opt_Temp_C':30,
                                                 'Lowest_Opt_Humidity':50,
                                                 'Average_Humidity':60,
                                                 'Highest_Opt_Humidity':70,
                                                 'Lowest_Opt_HeatIndex_C':22,
                                                 'Average_HeatIndex_C':27,
                                                 'Highest_Opt_HeatIndex_C':35,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6.5})

result10 = firebase.put('Standard_Parameters','Tomato',{'Crop_Name':'Tomato',
                                                 'Lowest_Opt_Temp_C':22,
                                                 'Average_Temp_C':24,
                                                 'Highest_Opt_Temp_C':26,
                                                 'Lowest_Opt_Humidity':60,
                                                 'Average_Humidity':65,
                                                 'Highest_Opt_Humidity':70,
                                                 'Lowest_Opt_HeatIndex_C':22,
                                                 'Average_HeatIndex_C':24,
                                                 'Highest_Opt_HeatIndex_C':27,
                                                 'Lowest_Opt_PHLevel':5.5,
                                                 'Average_PHLevel':6,
                                                 'Highest_Opt_PHLevel':6.5})


print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
