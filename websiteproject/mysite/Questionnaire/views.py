from django.shortcuts import render
from .models import Question
# Create your views here.

def Questionnaire_view(request):
    Questionnaires= Questionnaire_view().objects.all()
    return render(request,"questions.html",{"Questionnaires": Questionnaires})

def submit(request,q_id):
    if request.method == 'POST':
        test = submit().objects.get(id=q_id)
        questions= test.question_set.all()
        select= {}

        for question in questions:
            select[question.id]=request.POST.get("question_{}".format(question.id))

        return render(request,"submission.html",{"test":test,"select":select})

