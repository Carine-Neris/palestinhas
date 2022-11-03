from django.urls import path
from .views import palestras


urlpatterns = [
    path('palestras/',palestras)
]