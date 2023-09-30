# from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html', context={
        'titulo': 'PVP S/A'
    })
