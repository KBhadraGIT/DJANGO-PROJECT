from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Creating a function to print "Welcome to django" instead of displaying admin page.

def home(request):
    """
    This will display 'welcome to django' instead of admin page
    """
    return render(request, 'home.html')

def room(request):
    """
    At certain route i.e. 'room' it will display ROOM
    """
    return render(request, 'room.html')