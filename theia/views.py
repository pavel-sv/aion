from django.shortcuts import render
from .services import events

html_view = 'theia/theia.html'
event = events.UIEventHandler()


def index(request):
    # print(request.POST)
    event.request_handler(request)
    view_context = event.view_context
    return render(request, html_view, view_context)
