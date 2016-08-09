from django.shortcuts import render


def index(request):
    return render(request, 'market/index.html', {})

def advertentie(request):
    return render(request, 'market/advertentie.html', {})

def register(request):
    return render(request, 'market/register.html', {})