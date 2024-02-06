from django.shortcuts import render
from django.http import HttpResponse

from .models import Room
from .forms import RoomForm

# Create your views here.

'''
rooms= [
    {'id':1, 'name': 'Let\'s learn python!'},
    {'id':2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Devlopers'},
]
'''


def home(request):
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):

    rooms =Room.objects.get(id=pk)

    
    context = {'room': rooms}

    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        print(request.POST)


    context ={'form': form}
    return render(request, 'base/room_form.html', context)