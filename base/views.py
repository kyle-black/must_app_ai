from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Room, Topic
from .models import Room, Topic 
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
    q= request.GET.get('q') if request.GET.get('q') != None else ''


    rooms = Room.objects.filter(topic__name__icontains=q)

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, pk):

    rooms =Room.objects.get(id=pk)

    
    context = {'room': rooms}

    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')




    context ={'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form= RoomForm(instance = room)

    if request.method =="POST":
        form = RoomForm(request.POST, instance= room)

        if form.is_valid():
            form.save()
            return redirect('home')



    context ={'form': form}

    return render(request, 'base/room_form.html', context )


def deleteRoom(request, pk):
    room = room.objects.get()
    return render(request, 'base/delete.html', {'obj': room})

