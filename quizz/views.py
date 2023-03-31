# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from .models import Quiz, Question, Answer
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse
from django.template.loader import get_template


def question_list(request):
    quiz = Quiz.objects.all()
    quiz_name = "C/C++ "
    questions = Question.objects.filter(quiz=1)
    answers = Answer.objects.all()
    return render(request, 'cquestion.html', {'questions': questions, 'answers': answers, 'quiz_name': quiz_name})


def question_list1(request):
    quiz = Quiz.objects.all()

    questions = Question.objects.filter(quiz=2)
    quiz_name = "JAVA"
    answers = Answer.objects.all()
    return render(request, 'javaquestion.html', {'questions': questions, 'answers': answers, 'quiz_name': quiz_name})


def calculate_result(request):
    # Get quiz results
    if request.method == 'POST':
        questions = Question.objects.filter(quiz=1)
        answers = Answer.objects.all()
        qscore = 0
        for answer in answers:
            selected_option = request.POST.get(str(answer.question.id))
            if answer.is_correct(selected_option):
                qscore += 1

        total_questions = len(questions)
        incorrect_questions = total_questions - qscore

        # Calculate the percentage of correct answers
        percentage_correct = round((qscore / total_questions) * 100, 2)

        # Create pie chart
        labels = ['Correct', 'Incorrect']
        sizes = [qscore, incorrect_questions]
        explode = (0.1, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        chart = get_graph(fig)

        # Render the HTML template
        template = get_template('result.html')
        context = {'qscore': qscore, 'total_questions': total_questions, 'qscore': qscore, 'chart': chart,
                'percentage_correct': percentage_correct}
        html = template.render(context)

        return HttpResponse(html)

def calculate_result1(request):
    # Get quiz results
    if request.method == 'POST':
        questions = Question.objects.filter(quiz=2)
        answers = Answer.objects.all()
        qscore = 0
        equestions = Question.objects.filter(level="Easy",quiz=2)
        hquestions = Question.objects.filter(level="Hard",quiz=2)
        mquestions = Question.objects.filter(level="Medium",quiz=2)
        ecount = len(equestions)
        hcount = len(hquestions)
        mcount = len(mquestions)
        escore = 0 

        
        for answer in answers:
            selected_option = request.POST.get(str(answer.question.id))
            if answer.is_correct(selected_option):
                qscore += 1

        total_questions = len(questions)
        incorrect_questions = total_questions - qscore

        # Calculate the percentage of correct answers
        percentage_correct = round((qscore / total_questions) * 100, 2)

        # Create pie chart
        labels = ['Correct', 'Incorrect']
        sizes = [qscore, incorrect_questions]
        explode = (0.1, 0)


        labels1 = ['Easy','Medium','Hard']
        sizes1 = [ecount, mcount, hcount]
        explode1 = (0.2, 0.1, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        chart1 = get_graph1(fig1)


        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        chart = get_graph(fig)

        # Render the HTML template
        template = get_template('result.html')
        context = {'qscore': qscore, 'total_questions': total_questions, 'qscore': qscore, 'chart': chart,
                'percentage_correct': percentage_correct, 'chart1' : chart1}
        html = template.render(context)

        return HttpResponse(html)


def get_graph(fig):
    # Get the figure and export it to a bytes object
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100)
    plt.close(fig)

    # Convert the bytes object to a base64 string
    data = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Embed the base64 string in an HTML img tag
    src = f"data:image/png;base64,{data}"
    return src

def get_graph1(fig1):
    # Get the figure and export it to a bytes object
    buf = io.BytesIO()
    fig1.savefig(buf, format='png', dpi=100)
    plt.close(fig1)

    # Convert the bytes object to a base64 string
    data = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Embed the base64 string in an HTML img tag
    src = f"data:image/png;base64,{data}"
    return src
