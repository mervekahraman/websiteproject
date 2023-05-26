from django.db import models

# Create your models here.
class Title(models.Model):
    title= models.CharField(max_length=300)

class Question(models.Model):
    questionnaire= models.ForeignKey(Title,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    gender_question = Title.objects.create(questionnaire=questionnaire, text="What is your gender?")
    questionnaire.objects.create(question=gender_question, optionsText="Woman")
    questionnaire.objects.create(question=gender_question, optionsText="Man")

class Options(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    optionsText= models.CharField(max_length=500)


