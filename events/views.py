from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('welcome to the task')

def index(request):
    return render(request, 'index.html')

def contact( request):
    return HttpResponse('contact us')

def show_events(request):
    return HttpResponse('ji',show_events)