from django.http import HttpResponse
from django.shortcuts import redirect
def index(request):
    return Httpreponse('index')
def login(request):
    return redirect('/index')
