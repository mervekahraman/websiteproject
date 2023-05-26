from django.urls import path
from Questionnaire.views import Questionnaire_view,submit

urlpatterns = [
    path("",Questionnaire_view),
    path("submit",submit)
]