import os
from django.shortcuts import render


def hello_world(request):
    return render(request, 'pages/hello.html', {'BG_COLOR': os.environ.get('BG_COLOR'), 'PAGE_TITLE': os.environ.get('PAGE_TITLE')})