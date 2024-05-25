from django.shortcuts import render
from django.http import HttpResponse

def mainMenu(request):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request, "mainmenu/index.html")

def aboutPage(request):
    #return HttpResponse("<h1>About Me!</h1>")
    return render(request, "about/about.html")
    