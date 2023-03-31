from django.urls.resolvers import URLPattern
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('index.html', views.index, name='index'),
    path('courses.html', views.courses, name='courses'),
    path("contact.html", views.contact, name="contact"),
    path("about.html", views.about, name="about"),
    path("c.html",views.c, name="c"),
    path("c++.html",views.cplus, name="cplus"),
    path("java.html",views.java, name="java"),
    path("python.html",views.python, name="python"),
    path("sql.html",views.sql, name="sql"),
    path("textbook.html",views.textbook, name="textbook"),
    path("tindex.html",views.tindex, name="tindex"),
    path("test.html",views.test, name="test"),
    path("papers.html",views.papers, name="papers"),
    path("notes.html",views.notes, name="notes"),
    
]

