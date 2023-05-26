from django.urls import path
from Accounts.views import index, index_form, save_therapist

urlpatterns = [
    path("",index),
    path("success", index_form),
]

