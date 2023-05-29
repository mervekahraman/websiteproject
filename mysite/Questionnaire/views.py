from django.shortcuts import render
from .models import Question


def question(request):
    questions = Question.objects.all()
    context = {'questions': questions, 'score': 0}

    if request.method == 'GET':
        return render(request, "Questionnaire/hi.html", context)
    elif request.method == 'POST':
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken')
        score = 0
        for key, value in data.items():
            if Question.objects.get(pk=key).correct_answer == value:
                score += 1
        context['score'] = score
        return render(request, "Questionnaire/hi.html", context)

