from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

from app.models import Student,Teacher,User,Feedback
    
def login(request):
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Types = request.POST.get("types")

        if Types == "Student" :
            intakes = Student.objects.all().filter(email=Email,password=Password,types = Types)
            for intake in intakes:
                if intake.email == Email and intake.password == Password and intake.types:
                    return redirect('index.html')
                else:
                    return render(request, 'login.html')

        elif Types == "Teacher":    
            intakes1 = Teacher.objects.all().filter(email=Email,password=Password,types = Types)
            for intake in intakes1:
                if intake.email == Email and intake.password == Password and intake.types:
                    return redirect('index.html')
                else:
                    return render(request, 'login.html')
        
        return render(request, 'login.html')

def register(request):
    
    if request.method == 'POST':
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Phonenumber = request.POST.get("phonenumber")
        Age = request.POST.get("age")
        State = request.POST.get("state")
        City = request.POST.get("city")
        Types = request.POST.get("types")
        Password = request.POST.get("password")

        if User.objects.filter(email=Email).exists():
            messages.error(request, 'User with the same email address already exists')
            return render(request, 'register.html')
        

        user = User(name=Name, email=Email, phonenumber=Phonenumber, age=Age, state=State, city=City,types = Types, password=Password)
        user.save()

        
        if Types == "Student" :
                student = Student(name=Name, email=Email, phonenumber=Phonenumber, age=Age, state=State, city=City,types = Types, password=Password)
                student.save()
                return redirect('index.html')
            
        elif Types == "Teacher":
                teacher = Teacher(name=Name, email=Email, phonenumber=Phonenumber, age=Age, state=State, city=City,types = Types, password=Password)
                teacher.save()
                return redirect('index.html')
        
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')
    
def courses(request):
    return render(request, 'courses.html')

def contact(request):

    if request.method == 'POST':
        Username = request.POST.get("username")
        Email = request.POST.get("email")
        Message = request.POST.get("message")

        feed = Feedback(username=Username,email=Email,message=Message)
        feed.save()
        return render(request, 'contact.html')


    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def c(request):
    return render(request, 'c.html')

def cplus(request):
    return render(request, 'c++.html')

def java(request):
    return render(request, 'java.html')

def python(request):
    return render(request, 'python.html')

def sql(request):
    return render(request, 'sql.html')

def textbook(request):
    return render(request, 'textbook.html')

def notes(request):
    return render(request, 'notes.html')

def papers(request):
    return render(request, 'papers.html')

def tindex(request):
    return render(request, 'tindex.html')

def test(request):
    return render(request, 'test.html')

def ctest(request):
    return render(request, 'ctest.html')   

