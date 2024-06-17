from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


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

def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # just list the name, not url path

    context = {'form': form}
    return render (request, 'base/room_form.html', context)