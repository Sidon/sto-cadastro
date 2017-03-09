from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Profile

def create_account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Cria um novo usuario sem salva-lo
            new_user = user_form.save(commit=False)
            # Salva o objeto User
            new_user.save()
            # Cria o profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'core/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'core/register.html', {'user_form': user_form})



