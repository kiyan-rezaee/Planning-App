from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
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


def checkLogin(email, pas):
    try:
        acc = User.objects.get(Email=str(email))
    except:
        try:
            acc = User.objects.get(Username=str(email))
        except:
            return False
    if acc.Password == str(pas):
        return True
    return False


def index(request):
    # assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        # messages.add_message(request, messages.INFO, 'Hello world.')
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
                print(request)
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
    user = User.objects.get(Username=str(request.session['username']))
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'dashboard.html', {
        'title': 'Dashboard Page',
        'year': datetime.now().year,
        'firstname': user.Username,
        'lastname': user.Lastname,
        'coin': user.Coin
    })


def signUp(request):
    user = User.objects.get(Username=str(request.session['username']))
    print(user, 11111)
    if request.method == 'POST':
        if request.POST.get('Firstname'):
            print(request.POST)
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
                    post.Name = str(request.POST.get(f'course{i}') +"/"+ user.Username)
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
    user = User.objects.get(Username=str(request.session['username']))
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'profile.html', {
        'title': 'Profile Page',
        'year': datetime.now().year,
    })
