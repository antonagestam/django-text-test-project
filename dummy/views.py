from django.shortcuts import render


def uhn_tiss(request):
    return render(request, 'index.html')
