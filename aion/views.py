from django.shortcuts import render

html_view = 'aion/aion.html'


def index(request):
    return render(request, html_view)
