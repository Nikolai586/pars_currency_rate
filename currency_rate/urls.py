from django.urls import path
from .views import index, former_course


urlpatterns =[
    path('', index, name='index'),
    path('former_course/<int:day>/', former_course, name='former_course')
]
