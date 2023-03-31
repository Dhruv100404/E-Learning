from django.contrib import admin

from quizz.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)