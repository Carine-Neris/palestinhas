from django.urls import path
from .views import palestras_list


urlpatterns = [
    path('palestras',palestras_list),
]