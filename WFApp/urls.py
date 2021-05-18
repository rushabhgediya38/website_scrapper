from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('frequency/', FreqUrlGet, name='freq-url'),
    path('result/', ResultFreq, name='ResultFreq')
]
