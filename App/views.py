from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def index(request):
    """Renders the home page."""
    # assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            post = newuser()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.save()
            return render(request, 'index.html', {
                'title': 'Home Page',
                'year': datetime.now().year,
            })
        else:
            return render(request, 'index.html', {
                'title': 'Home Page',
                'year': datetime.now().year,
            })
    return render(request, 'index.html', {
                'title': 'Home Page',
                'year': datetime.now().year,
            })


def dashboard(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'dashboard.html', {
        'title': 'Dashboard Page',
        'year': datetime.now().year,
    })

def signUp(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'signUp.html', {
        'title': 'Sign Up Page',
        'year': datetime.now().year,
    })


# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request, 'contact.html', {
#             'title': 'Contact',
#             'message': 'Your contact page.',
#             'year': datetime.now().year,
#         })

# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request, 'about.html', {
#             'title': 'About',
#             'message': 'Your application description page.',
#             'year': datetime.now().year,
#         })
