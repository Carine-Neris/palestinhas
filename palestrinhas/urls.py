from django.urls import path
from .views import palestras, palestra_delete, palestra_create


urlpatterns = [
    path('palestras/',palestras, name='palestras'),
    path('palestra/create/',palestra_create,name='palestracreate'),
    path('palestra/<int:pk>/',palestra_delete, name='palestradelete'),
]