from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    age = models.IntegerField()
    state = models.CharField(max_length=255)
    types = models.CharField(max_length=255,default='Student')
    city = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    age = models.IntegerField()
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    types = models.CharField(max_length=255,default='Teacher')
    password = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    age = models.IntegerField()
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    TYPES_CHOICES = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    types = models.CharField(max_length=50, choices=TYPES_CHOICES, null=True)
    password = models.CharField(max_length=255)

class Feedback(models.Model):
    username = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=25,null=True)
    message = models.CharField(max_length=255,null=True)