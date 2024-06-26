from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request,f"{username}, вы успешно вошли в аккаунт!")
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request,user)
            messages.success(request, f"{user.username}, вы успешно вошли в аккаунт!")
            return HttpResponseRedirect(reverse('main:home'))
            # session_key = request.session.session_key
            #
            # user = form.instance
            # auth.login(request, user)
            #
            # if session_key:
            #     Cart.objects.filter(session_key=session_key).update(user=user)
            #     messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")

    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")

            if request.POST.get('next', None):
                return HttpResponseRedirect(request.POST.get('next'))

            return HttpResponseRedirect(reverse('user:index'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'form': form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:home'))