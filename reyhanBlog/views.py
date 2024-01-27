from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    #return HttpResponse('hi alireza')
    return render(request, 'about.html')

def home(request):
     #return HttpResponse('hello')
      return render(request, 'Home.html')
