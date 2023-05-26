# from django.shortcuts import render
# from .forms import QuestionnaireForm
#
# def questionnaire(request):
#     if request.method == 'POST':
#         form = QuestionnaireForm(request.POST)
#         if form.is_valid():
#             # Process the questionnaire responses
#             for question_id, choice_id in form.cleaned_data.items():
#                 # Perform actions with the selected choices
#                 # For example, save the responses to the database
#                 # or perform calculations based on the choices
#                 # You can access the selected choice using the choice_id
#             return render(request, "Thank you")
#     else:
#         form = QuestionnaireForm()
#     return render(request, 'Questionnaire/questions.html', {'form': form})

