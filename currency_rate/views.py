from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from .utils import response_data

from .models import Сurrency


def index(request):
    data = Сurrency.objects.filter(date=date.today())
    if not data.exists():
        currence = response_data()
        data, _ = Сurrency.objects.get_or_create(usd=currence['USD'], eur=currence['EUR'])
    else:
        data = data[0]
    return render(request, 'index.html', {'data': data})


def former_course(request, day):
    date_cur = date.today() - timedelta(days=day)
    data = get_object_or_404(Сurrency, date=date_cur)
    return render(request, 'index.html', {'data': data})
