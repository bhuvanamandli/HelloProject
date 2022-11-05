from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(request):
    ss="<h1>Hello this is your dearest person</h1>"
    return HttpResponse(ss)

def homepage(request):
    ss="<h1>Hello user!!</h1>"
    return HttpResponse(ss)