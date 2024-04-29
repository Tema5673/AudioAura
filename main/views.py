from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/search.html')

def personal_area(request):
    return render(request, 'main/personal_area.html')