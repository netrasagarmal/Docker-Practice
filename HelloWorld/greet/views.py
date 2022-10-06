from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHelloWorld(request):
    #print("\n\n\t H e l l o  W o r l d from cmd\n\n")
    return HttpResponse("Hello World on web browser")
