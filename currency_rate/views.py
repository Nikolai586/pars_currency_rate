from django.shortcuts import render
from .utils import response_data


def index(request):
    print(response_data())
    return render(request, 'index.html', {'data': response_data()})
