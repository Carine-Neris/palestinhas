from django.urls import path
from palestrinhas import views


urlpatterns = [
    path('', views.palestras, name='palestras'),
    path('palestra/create/', views.palestra_create, name='palestracreate'),
    path('palestra/<int:pk>/delete', views.palestra_delete, name='palestradelete'),
    path('palestra/detail/<int:pk>/', views.palestra_detail, name='palestradetail'),
    path('palestras/by-user/',views.palestras_by_user,name='palestrasuser')
]
