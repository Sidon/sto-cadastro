from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def create_account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request, 'core/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'core/register.html', {'user_form': user_form})



