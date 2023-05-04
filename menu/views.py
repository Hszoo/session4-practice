from django.shortcuts import render

# Create your views here.

def menuhome(request) :
    return render(request, "menuhome.html")