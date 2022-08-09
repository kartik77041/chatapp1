from django.shortcuts import render
from .models import chat, Group
def index(request,group_name):
    group = Group.objects.filter(name = group_name).first()
    chats = []
    if group:
        chats=chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()
    return render(request, 'app/index.html',{'groupname':group_name,'chats':chats})
