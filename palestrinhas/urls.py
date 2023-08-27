from django.urls import path, include
from django.contrib.auth import views as auth_views

from palestrinhas import views


urlpatterns = [
    path('', views.palestras, name='palestras'),
    path('palestra/create/', views.palestra_create, name='palestracreate'),
    path('palestra/<int:pk>/delete', views.palestra_delete, name='palestradelete'),
    path('palestra/detail/<int:pk>/', views.palestra_detail, name='palestradetail'),
    path('palestras/by-user/',views.palestras_by_user,name='palestrasuser'),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", auth_views.LogoutView.as_view(redirect_field_name='palestras')),

]
