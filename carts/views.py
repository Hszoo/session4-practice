from django.shortcuts import render

# Create your views here.

def carthome(request) :
    return render(request, "index.html")