from django.shortcuts import render
# from quizz import Quiz, Question, Answer
# from app import Student,Teacher

def dashboard(request):
    return render(request,'dashboard.html')