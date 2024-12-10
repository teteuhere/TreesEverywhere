from django.shortcuts import render, redirect
from ..forms.register import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})