from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime, date, timedelta
from .models import User, Store, Course, Pom
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
        'title': 'Studier',
        'year': datetime.now().year,
    })


def dashboard(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    """Renders the dashboard page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 'dashboard.html', {
            'title': 'Dashboard Page',
            'year': datetime.now().year,
            'firstname': user.Username,
            'lastname': user.Lastname,
            'coin': user.Coin,
            'username': user.Username
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
            store = Store()
            store.user = user
            store.save()
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
    sum_pom = sum([
        x['Pom_count']
        for x in Course.objects.filter(user_id=user.Email).values('Pom_count')
    ]) * 25
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
            'age': f'You Are {(date.today()-user.Dob).days//365} Years Old!',
            'coin': user.Coin,
            'avatar': str(user.store.avatar),
            'course': li,
            'sum_pom': sum_pom
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

    li = [
        str(x.Name).replace(f'/{user.Username}', '')
        for x in Course.objects.filter(user_id=user.Email)
    ]
    if request.method == 'POST':
        coursename = str(
            request.POST.get('selectedCourse') + "/" + user.Username)
        course = Course.objects.get(Name=coursename)
        request.POST.get('mode')
        # request.POST.get('selectedCourse')
        # request.POST.get('time')/25
        try:
            if request.session['lastcourse'] == request.POST.get(
                    'selectedCourse'):
                if request.POST.get('time') == 0:
                    # course.Total_time += request.session['lasttime'] - \
                    # int(request.POST.get('time'))
                    request.session['lastpom'].Time = 1500 - request.POST.get(
                        'time')
                    request.session['lastpom'].Date = datetime.now()
                    request.session['lastpom'].Rating = 5
                    request.session['lastpom'].save()
                    del request.session['lastcourse']
                    del request.session['lastpom']
                else:
                    request.session['lastpom'].Time += (
                        request.session['lasttime'] -
                        int(request.POST.get('time')))
                    request.session['lastpom'].Date = datetime.now()
                    request.session['lastpom'].Rating = 5
                    request.session['lastpom'].save()
            else:
                del request.session['lastpom']
        except:
            request.session['lastpom'] = Pom()
            request.session['lastcourse'] = request.POST.get('selectedCourse')
            if request.POST.get('time') == 0:
                request.session['lastpom'].Time = 1500 - request.POST.get(
                    'time')
                request.session['lastpom'].Date = datetime.now()
                request.session['lastpom'].Rating = 5
                request.session['lastpom'].save()
                del request.session['lastcourse']
                del request.session['lastpom']
            else:
                request.session['lastpom'].Time = 1500 - int(
                    request.POST.get('time'))
                request.session['lasttime'] = int(request.POST.get('time'))
                request.session['lastpom'].Date = datetime.now()
                request.session['lastpom'].Rating = 5
                request.session['lastpom'].save()
    else:
        try:
            del request.session['lastcourse']
            del request.session['lasttime']
        except KeyError:
            pass
    return render(
        request, 'pom.html', {
            'title': 'Pomodoro Page',
            'year': datetime.now().year,
            'username': user.Username,
            'course': li,
            'firstname': user.Username,
            'lastname': user.Lastname,
            'coin': user.Coin
        })


def store(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    if request.method == 'POST':
        if request.POST.get('code') == 'username':
            try:
                for x in Course.objects.filter(user_id=user.Email):
                    x.Name = str(
                        str(x.Name).replace(f'/{user.Username}', '') + "/" +
                        user.Username)
                    x.save()
                user.Username = request.POST.get('newUsername')
                user.save()
            except Exception as a:
                messages.add_message(
                    request, messages.INFO,
                    'That username is already taken, Try another!')
        elif request.POST.get('code') == 'doubleCoin':
            mode = int(request.POST.get('mode'))
            user.store.Doublecoin = True
            if mode == 100:
                user.Coin -= 100
                user.store.Doublecoin_time = timedelta(days=2) + datetime.now()
                user.store.save()
                user.save()
            elif mode == 500:
                user.Coin -= 500
                user.store.Doublecoin_time = timedelta(
                    days=14) + datetime.now()
                user.store.save()
                user.save()
            elif mode == 800:
                user.Coin -= 800
                user.store.Doublecoin_time = timedelta(
                    days=31) + datetime.now()
                user.store.save()
                user.save()
        elif request.POST.get('code') == 'darkMode':
            if user.store.dark_mode:
                messages.add_message(request, messages.INFO,
                                     'You already bought it before')
            user.Coin -= 500
            user.store.dark_mode = True
            user.save()
        elif request.POST.get('code') == 'avatar':
            user.store.avatar = request.POST.get('avatarCode')
            user.store.save()
            user.save()
        elif request.POST.get('code') == 'ml':
            pass
            # user.save()
    else:
        pass
    return render(
        request, 'store.html', {
            'title': 'Store Page',
            'year': datetime.now().year,
            'firstname': user.Firstname,
            'lastname': user.Lastname,
            'username': user.Username,
            'coin': user.Coin,
            'doubleCoin': user.store.Doublecoin,
            'doubleCoinTime': user.store.Doublecoin_time,
            'avatarsCount': range(1, 17),
            'allUsernames': [x.Username for x in User.objects.all()]
        })


def analysis(request):
    try:
        user = User.objects.get(Username=str(request.session['username']))
    except:
        user = User.objects.get(Email=str(request.session['username']))
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 'analysis.html', {
            'title': 'Analysis Page',
            'year': datetime.now().year,
            'firstname': user.Username,
            'lastname': user.Lastname,
            'coin': user.Coin,
            'username': user.Username
        })
