from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Creating a function to print "Welcome to django" instead of displaying admin page.

def home(request):
    """
    This will display 'welcome to django' instead of admin page
    """
    return HttpResponse('Welcome to django')

def room(request):
    """
    At certain route i.e. 'room' it will display ROOM
    """
    return HttpResponse('ROOM')