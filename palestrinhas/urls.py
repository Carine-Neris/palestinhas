from django.urls import path
from .views import palestras, palestra_delete, palestra_create, palestra_detail


urlpatterns = [
    path('palestras/', palestras, name='palestras'),
    path('palestra/create/', palestra_create, name='palestracreate'),
    path('palestra/<int:pk>/delete', palestra_delete, name='palestradelete'),
    path('palestra/detail/<int:pk>/', palestra_detail, name='palestradetail'),
]
