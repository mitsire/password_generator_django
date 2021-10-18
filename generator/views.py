from django.shortcuts import render
# import this
from django.http import HttpResponse
import random

# make a function for the urls
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get("length", 12))


    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("special"):
        characters.extend(list('!@#$%^*&()'))

    if request.GET.get("numbers"):
        characters.extend(list('0987654321'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def eggs(request):
    return HttpResponse("EGGS ARE GOOD")

# Create your views here.
