from django.shortcuts import render
from Accounts.models import Therapist
from Accounts.forms import TherapistForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def index_form(request):
    if request.method =="POST":
        form = TherapistForm(request.POST)

        if form.is_valid():
            firstname= form.cleaned_data["firstname"]
            lastname= form.cleaned_data["lastname"]
            a = Therapist(firstname=firstname, lastname=lastname)
            a.save()
            return render(request,"t_saved.html")

        else:
            form = TherapistForm()

            return render(request, "index_form.html", {"form": form})

def save_therapist(request):
    messages = []
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        a = Therapist(firstname=firstname, lastname=lastname)
        a.save()
        messages.append(str(a) + 'saved')
        return render(request, "author_saved.html", context={"messages": messages})