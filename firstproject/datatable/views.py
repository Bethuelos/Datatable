from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config = {
  "apiKey": "AIzaSyDcRXxLt5OoL_WhnzCH25puhSB0rtNdBAg",
  "authDomain": "call-logs-a024b.firebaseapp.com",
  "databaseURL": "https://call-logs-a024b-default-rtdb.firebaseio.com",
  "projectId": "call-logs-a024b",
  "storageBucket": "call-logs-a024b.appspot.com",
  "messagingSenderId": "433884624359",
  "appId": "1:433884624359:web:c89b4be763332eeb1df942",
#   measurementId: "G-B5FXSF67CR"
};

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

def index(request):
    data = database.child('call_log').shallow().get().val()
    logList = []
    Names = []
    Numbers = []
    Operators = []
    Types = []
    Durations = []

    for i in data:
      logs = logList.append(i)
      # print('logs: {}'.format(logs))

    for i in logList:
      nameVal = database.child('call_log').child(i).child('name').get().val()
      numberVal = database.child('call_log').child(i).child('number').get().val()
      operatorVal = database.child('call_log').child(i).child('operator').get().val()
      typeVal = database.child('call_log').child(i).child('type').get().val()
      durationVal = database.child('call_log').child(i).child('duration').get().val()
      Names.append(nameVal)
      Numbers.append(numberVal)
      Operators.append(operatorVal)
      Types.append(typeVal)
      Durations.append(durationVal)
      # print('val: {}'.format(val))

    comb_list = zip(Names, Numbers, Operators, Types, Durations)
    # Val = []
    # Val.append(val)
    # print('val2: {}'.format(Val))

    name = database.child('call_log').child('name').get().val()
    number = database.child('call_log').child('number').get().val()
    operator = database.child('call_log').child('operator').get().val()
    type = database.child('call_log').child('type').get().val()
    # data = database.get()
    return render(request,"index.html", 
    # {"result":Val}
    {"database":comb_list}
    # {
    #     "name":Names,
    #     "number":Numbers,
    #     "operator":Operators,
    #     "type":Types,
    #     "duration":Durations,
    # }
    )
    # return HttpResponse('name is :' + name + '\n number is :' + type);