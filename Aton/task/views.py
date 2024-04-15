from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Client


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('client_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def client_list(request):
    if request.user.is_authenticated:
        clients = Client.objects.filter(respons=request.user)
        return render(request, 'client_list.html', {'clients': clients})
    else:
        return redirect('login')


def change_status(request, client_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        client = Client.objects.get(id=client_id)
        client.status = new_status
        client.save()
    return redirect('client_list')

