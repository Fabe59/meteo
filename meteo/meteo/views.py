from django.shortcuts import render

def index(request):
    return render(request, 'meteo/index.html') #returns the index.html template