from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'rnd/homep.html')

def login(request):
    return render(request,'rnd/loginp.html')

def prephd(request):
    return render(request,'rnd/prephd.html')

def resmtd(request):
    return render(request,'rnd/resmtd.html')

def rrm(request):
    return render(request,'rnd/rrm.html')