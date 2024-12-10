from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.accounts.forms import LoginForm  

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('page/home.html')  # Redireciona para a página inicial após o login
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})