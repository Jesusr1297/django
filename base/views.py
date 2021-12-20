from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room_ = None
    for i in rooms:
        if i['id'] == int(pk):
            room_ = i
    context = {'room': room_}

    return render(request, 'base/room.html', context)


rooms = [
    {'id': 1, 'name': 'lets learn some python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'frontend developers '},

]
