# Generated by Django 4.1.7 on 2023-03-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_questions_alter_user_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question',
        ),
    ]
