from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'rnd/homep.html')


def login(request):
<<<<<<< HEAD
    return render(request, 'rnd/loginp.html')

=======
    return render(request,'rnd/login1.html')
>>>>>>> rosh

def prephd(request):
    return render(request, 'rnd/prephd.html')


def resmtd(request):
<<<<<<< HEAD
    return render(request, 'rnd/resmtd.html')


def rrm(request):
    return render(request, 'rnd/rrm.html')
=======
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
>>>>>>> rosh
