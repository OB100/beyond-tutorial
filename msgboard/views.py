from django.shortcuts import render, redirect
from .models import Message


def board(request):
    messages = Message.objects.order_by('-date')
    return render(request, 'msgboard/board.html', {
        'messages': messages,
    })
# Create your views here.
