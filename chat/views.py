from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Message , Room
# Create your views here.
def room(request , room):
    
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)
    return render(request , 'chat/room.html' ,
     {'room':room , 'username':username , 'room_details':room_details})

def home(request):
    return render(request , 'chat/home.html')
   

def checkview(request):
    if request.method == "POST":
        room_name = request.POST['roomname']
        username = request.POST['username']
        if Room.objects.filter(name = room_name).exists():
            return redirect('/'+ room_name + '/?username=' + username)
        else:
            new_room = Room.objects.create(name = room_name)
            new_room.save()
            return redirect('/' +  room_name + '/?username=' + username )
def send(request):
    if request.method == "POST":
        username = request.POST['username']
        room_id = request.POST['room_id']
        message = request.POST['message']

        new_message = Message.objects.create(msg = message , room = room_id , msg_user = username)
        new_message.save()
        return HttpResponse("Message sent successfully!!")

def getmessages(request , room_name):
    room_details =Room.objects.get(name = room_name)
    messages = Message.objects.filter(room = room_details.id)
    return JsonResponse({'messages':list(messages.values())})

