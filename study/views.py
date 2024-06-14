from django.shortcuts import render
# from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': "Let's learn python!"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend development"},
]

def index(request):
    return render(request, 'base/index.html', {'rooms': rooms})

def room(request):
    return render(request, 'base/room.html')

# def index(request):
#     return HttpResponse('Home Page')

# def room(request):
#     return HttpResponse('Room')