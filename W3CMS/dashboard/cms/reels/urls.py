
from django.urls import path 
from . import views 

app_name='reels'


urlpatterns = [ 
    path('list/', views.reel_list, name='reel_list'),
    path('create/', views.reel_create, name='reel_create'),
    path('edit/<int:id>/', views.reel_edit, name='reel_edit'),
    path('delete/<int:id>/', views.reel_delete, name='reel_delete'),
    ]