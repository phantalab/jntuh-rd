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

def prephdSubmit(request):
    studroll=request.POST.get('studroll')
    subject=request.POST.get('subject')
    regMonth=request.POST.get('regMonth')
    marks=request.POST.get('marks')
    print(studroll,subject,regMonth,marks)
    return render(request, 'rnd/prephd.html')

def resmtd(request):
    return render(request, 'rnd/researchMethod.html')

def resmtdSubmit(request):
    studroll=request.POST.get('studroll')
    monyear=request.POST.get('monyear')
    satisfaction=request.POST.get('satisfactionRadio')
    completed=request.POST.get('completedRadio')
    print(studroll,monyear,satisfaction,completed)
    return render(request, 'rnd/researchMethod.html')

def rrm(request):
    return render(request, 'rnd/rrm.html')

def rrmSubmit(request):

    temp=request.POST
    studroll=temp.get('studroll')
    rrmNO=temp.get('rrmNo')
    regMonth=temp.get('regMonth')
    satisfaction=temp.get('satisfactionRadio')
    marks=temp.get('marks')
    print(studroll,rrmNO,regMonth,satisfaction,marks)
    return render(request, 'rnd/rrm.html')

def collaq(request):
    return render(request, 'rnd/collaq.html')

def collaqSubmit(request):
    temp=request.POST
    studroll=temp.get('studroll')
    submonyear=temp.get('submonyear')
    satisfaction=temp.get('satisfactionRadio')
    print(studroll,submonyear,satisfaction)
    return render(request, 'rnd/collaq.html')

def revsubmit(request):
    return render(request, 'rnd/reviseResubmit.html')

def revsubmitSubmit(request):
    #submit the values from revsubmit :3
    temp=request.POST
    studroll=temp.get('studroll')
    revisedDate=temp.get('revisedDate')
    deDate=temp.get('deDate')
    print(studroll,revisedDate,deDate)
    return render(request, 'rnd/reviseResubmit.html')

def plagarism(request):
    return render(request, 'rnd/plagarism.html')

def plagarismSubmit(request):
    temp=request.POST
    studroll=temp.get('studroll')
    date=temp.get('date')
    fileUploaded=temp.get('file')
    return render(request, 'rnd/plagarism.html')

def vivavoca(request):
    return render(request, 'rnd/vivavoca.html')

def vivavocaSubmit(request):
    temp=request.POST
    studroll=temp.get('studroll')
    deDate=temp.get('deDate')
    finalDate=temp.get('finalDate')
    ExtExam=temp.get('ExtExam')
    return render(request, 'rnd/vivavoca.html')

def theSubmit(request):
    return render(request, 'rnd/thesisSubmit.html')

def theSubmitSubmit(request):
    #submit function for thesisSubmit
    temp=request.POST
    studroll=temp.get('studroll')
    studentDate=temp.get('studentDate')
    DEDate=temp.get('DEDate')
    EXTExam=temp.get('EXTExam')
    studCum=temp.get('studCum')
    return render(request, 'rnd/thesisSubmit.html')

def extend(request):
    return render(request, 'rnd/extensionPeriod.html')
    
def extendSubmit(request):
    temp=request.POST
    studroll=temp.get('studroll')
    extendDate=temp.get('extendDate')
    permission=temp.get('Permission')
    print(studroll,extendDate,permission)
    return render(request, 'rnd/extensionPeriod.html')

def changeSuper(request):
    return render(request, 'rnd/supervisorChange.html')

def changeSuperSubmit(request):
    appDate=request.POST.get('appDate')
    studroll=request.POST.get('studroll')
    return render(request, 'rnd/supervisorChange.html')