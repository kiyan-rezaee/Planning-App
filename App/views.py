from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime, date
from .models import User
from .models import Course
from django.shortcuts import redirect
from django.contrib import messages


def checkSignUp(username, email, pas):
    try:
        User.objects.get(Email=str(email))
        return False
    except:
        try:
            User.objects.get(Username=str(username))
            return False
        except:
            return True
    return True


def checkLogin(info, pas):
    try:
        acc = User.objects.get(Email=str(info))
    except:
        try:
            acc = User.objects.get(Username=str(info))
        except:
            return False
    if acc.Password == str(pas):
        return True
    return False


def index(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get(
                'email') and request.POST.get('password'):
            if checkSignUp(request.POST.get('username'),
                           request.POST.get('email'),
                           request.POST.get('password')):
                post = User()
                post.Username = request.POST.get('username')
                post.Email = request.POST.get('email')
                post.Password = request.POST.get('password')
                request.session['username'] = request.POST.get('username')
                post.save()
                response = redirect('/signUp')
                return response
            elif len(request.POST.get('password')) < 8:
                messages.add_message(
                    request, messages.INFO,
                    'Your password must be at least 8 characters!')
            else:
                messages.add_message(
                    request, messages.INFO,
                    'That email or username is already taken, Try another!')
        elif request.POST.get('email') and request.POST.get('password'):
            if checkLogin(request.POST.get('email'),
                          request.POST.get('password')):
                request.session['username'] = request.POST.get('email')
                response = redirect('/dashboard')
                return response
            else:
                messages.add_message(request, messages.INFO,
                                     'Wrong password or username!')
    else:
        return home(request)
    return home(request)


def home(request):
    return render(request, 'index.html', {
        'title': 'Home Page',
        'year': datetime.now().year,
    })


def dashboard(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 'dashboard.html', {
            'title': 'Dashboard Page',
            'year': datetime.now().year,
            'firstname': user.Username,
            'lastname': user.Lastname,
            'coin': user.Coin
        })


def signUp(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    if request.method == 'POST':
        if request.POST.get('Firstname'):
            user.Firstname = request.POST.get('Firstname')
            user.Lastname = request.POST.get('Lastname')
            user.Dob = request.POST.get('DOB')
            user.save()
            i = 0
            while True:
                i += 1
                if request.POST.get(f'course{i}'):
                    post = Course()
                    post.user = user
                    post.Name = str(
                        request.POST.get(f'course{i}') + "/" + user.Username)
                    post.Priority = request.POST.get(f'priority{i}')
                    post.save()
                else:
                    break
            request.session['username'] = user.Username
            response = redirect('/dashboard')
            return response
    assert isinstance(request, HttpRequest)
    return render(request, 'signUp.html', {
        'title': 'Sign Up Page',
        'year': datetime.now().year
    })


def profile(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    li = [
        str(x.Name).replace(f'/{user.Username}', '')
        for x in Course.objects.filter(user_id=user.Email)
    ]
    assert isinstance(request, HttpRequest)
    return render(
        request, 'profile.html', {
            'title': 'Profile Page',
            'year': datetime.now().year,
            'fullname': f'Hi, {user.Firstname} {user.Lastname}',
            'firstname': user.Firstname,
            'lastname': user.Lastname,
            'username': user.Username,
            'email': user.Email,
            'age': f'{(date.today()-user.Dob).days//365} Years Old!',
            'coin': user.Coin,
            'course': li
        })


def pom(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    li = [
        str(x.Name).replace(f'/{user.Username}', '')
        for x in Course.objects.filter(user_id=user.Email)
    ]
    print(request.POST.get('selectedCourse'))
    return render(
        request, 'pom.html', {
            'title': 'Home Page',
            'year': datetime.now().year,
            'username': user.Username,
            'course': li
        })
