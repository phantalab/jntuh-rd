from django.shortcuts import render
import pyrebase
from django.shortcuts import render 



config = {
    'apiKey': "AIzaSyAwTQ43TVqlmBvMyXZjRI5UJAj70GZJ1CE",
    'authDomain': "project-randd.firebaseapp.com",
    'databaseURL': "https://project-randd.firebaseio.com",
    'projectId' : "project-randd",
    'storageBucket': "project-randd.appspot.com",
    'messagingSenderId' : "700682061122",
    'appId' : "1:700682061122:web:f258f9ec0dc888bafb34db",
    'measurementId' : "G-1E8M7F2DC7"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
email = input("enter Email ID :")
pwd = input("enter password : ")
user = auth.sign_in_with_email_and_password(email,pwd)
print("current user is ",user['localId'])


# Create your views here.


def home(request):
    return render(request, 'rnd/homep.html')


def login(request):
    return render(request,'rnd/login1.html')

def prephd(request):
    return render(request, 'rnd/prephd.html')


def resmtd(request):
    return render(request,'rnd/researchMethod.html')

def rrm(request):
    return render(request,'rnd/rrm.html')

def collaq(request):
    return render(request,'rnd/collaq.html')

def revsubmit(request):
    return render(request,'rnd/reviseResubmit.html')

def plagarism(request):
    return render(request,'rnd/plagarism.html')

def vivavoca(request):
    return render(request,'rnd/vivavoca.html')

def theSubmit(request):
    return render(request,'rnd/thesisSubmit.html')

def extend(request):
    return render(request,'rnd/extensionPeriod.html')

def changeSuper(request):
    return render(request,'rnd/supervisorChange.html')
