from django.shortcuts import render
import pyrebase
from . import cred


# Create your views here.


firebase = pyrebase.initialize_app(cred.config)
auth = firebase.auth()


def postlogin(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid cerediantials"
        return render(request, "login1.html", {"msg": message})
        print(user)
    print(email, passw)
    return render(request, "homep.html", {"e": email})


def home(request):
    print("current user---------->", auth.current_user)
    return render(request, 'rnd/homep.html')


def login(request):
    return render(request, 'rnd/login1.html')


def prephd(request):
    return render(request, 'rnd/prephd.html')


def resmtd(request):
    return render(request, 'rnd/researchMethod.html')


def rrm(request):
    return render(request, 'rnd/rrm.html')


def collaq(request):
    return render(request, 'rnd/collaq.html')


def revsubmit(request):
    return render(request, 'rnd/reviseResubmit.html')


def plagarism(request):
    return render(request, 'rnd/plagarism.html')


def vivavoca(request):
    return render(request, 'rnd/vivavoca.html')


def theSubmit(request):
    return render(request, 'rnd/thesisSubmit.html')


def extend(request):
    return render(request, 'rnd/extensionPeriod.html')


def changeSuper(request):
    return render(request, 'rnd/supervisorChange.html')
