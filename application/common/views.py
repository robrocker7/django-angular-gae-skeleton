from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'base.html', {})

def warmup(request):
    return HttpResponse('warmed up')