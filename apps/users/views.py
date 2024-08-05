from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages

from apps.users.models import User



def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email = email).first()
        
        if user:
            if user.check_password(password):
                login(request, user)
                return redirect('cinemas:index')
            else:
                messages.error(request, 'Неверный пароль')
        else:
            messages.error(request, 'Пользователь с такой почтой не найден')

    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)

    return redirect('users:login')
