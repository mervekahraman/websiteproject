
from django.urls import path, include
from Accounts.views import login

urlpatterns = [
    path('', login, name='login'),

]