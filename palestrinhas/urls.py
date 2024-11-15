from django.urls import path, include
from django.contrib.auth import views as auth_views
from jedi.api import parso_to_jedi_errors

from palestrinhas import views


urlpatterns = [
    path('', views.palestras, name='palestras'),
    path('palestras/by-user/',views.palestras_by_user,name='palestrasuser'),

    path('palestra/create/', views.palestra_create, name='palestracreate'),
    path('palestra/<int:pk>/delete', views.palestra_delete, name='palestradelete'),
    path('palestra/detail/<int:pk>/', views.palestra_detail, name='palestradetail'),
    path('palestra/<int:palestra_id>/comentar/', views.adicionar_comentario, name='comentario'),
    path('palestra/edit/<int:pk>',views.palestra_edit,name='palestraedit'),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", auth_views.LogoutView.as_view(redirect_field_name='palestras')),

]
