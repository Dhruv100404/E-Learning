# Generated by Django 4.0 on 2023-03-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_alter_answer_correct_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct_option',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=255),
        ),
    ]
