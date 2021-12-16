from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('serviceDetails/', serviceDetails, name='serviceDetails'),
    path('realisation/', realisation, name='realisation'),
    path('contact/', contact, name='contact'),
    path('GetMessage/', GetMessage, name='GetMessage'),
    path('about/', about, name='about'),
    path('new/', new, name='new'),
    path('confirm/', confirm, name='confirm'),
]