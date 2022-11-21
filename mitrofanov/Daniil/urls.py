from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home', kwargs={'name': 'Даниил', 'suname': 'Митрофанов', 'age': '16', 'intristings': 'Программирование'}),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts')
]