from django.urls import path
from Questionnaire.views import question

urlpatterns = [
    path("",question)

]