from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Creating a function to print "Welcome to django" instead of displaying admin page.

def home(request):
    """
    This will display 'welcome to django' instead of admin page
    """
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    """
    At certain route i.e. 'room' it will display ROOM
    """
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

rooms = [
    {'id': 1,
     'name': 'Let\'s learn python!'},
    {'id': 2,
     'name': 'Design with me'},
    {'id': 3,
     'name':'Frontend developers'},
]