from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'pg1.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        contact= Contact(name=name, email=email, mobile=mobile, message=message)
        contact.save()
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')

def abt2(request):
    return render(request,'abt2.html')

def register(request):
    return render(request,'register.html')

def checker(request):
    return render(request,'checker.html')

def courses(request):
    return render(request,'courses.html')

def servicepage(request):
    return render(request,'servicepage.html')

def exam(request):
    return render(request,'exam.html')

def teachers(request):
    return render(request,'teachers.html')

def teacher_profile(request):
    return render(request,'teacher_profile.html')

def chat(request):
    return render(request,'chat.html')

