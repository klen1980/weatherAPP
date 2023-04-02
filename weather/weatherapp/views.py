from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def homework(request):
    return render(request, 'weather/homework.html')

# Create your views here.
