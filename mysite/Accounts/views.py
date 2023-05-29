from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


