from django.urls import path
from core.views import mostar,mostarDateTime

urlpatterns = [
    path('ruta1/', mostar),
    path('datetime/', mostarDateTime),
]