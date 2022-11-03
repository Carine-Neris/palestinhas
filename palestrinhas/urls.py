from django.urls import path
from .views import palestras, palestra_delete


urlpatterns = [
    path('palestras/',palestras, name='palestras'),
    path('palestras/<int:pk>/', palestra_delete, name='palestrasdelete')
]