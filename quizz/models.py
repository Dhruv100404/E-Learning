from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=255)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Question = models.CharField(max_length=255)
    level = models.CharField(choices=[('Easy','Easy'),('Medium','Medium'),('Hard','Hard')], max_length=255, default='Medium')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=255)

    def is_correct(self, selected_option):
        return selected_option == self.correct_option

