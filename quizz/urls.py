from django.urls.resolvers import URLPattern
from django.urls import path
from . import views


urlpatterns = [
    
    path("cquestion.html",views.question_list, name="question_list"),
    path("javaquestion.html",views.question_list1,name="question_list1"),
    path("result.html",views.calculate_result,name="calculate_result"),
    path("result1.html",views.calculate_result1,name="calculate_result1")
]

