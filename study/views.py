from django.shortcuts import render
from django.http import HttpRequest
from .models import Room
# from django.http import HttpResponse -- original

# rooms = [
#     {'id': 1, 'name': "Let's learn python!"},
#     {'id': 2, 'name': "Design with me"},
#     {'id': 3, 'name': "Frontend development"}
# ]

def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)