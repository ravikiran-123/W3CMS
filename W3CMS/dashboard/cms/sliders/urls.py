from django.urls import path 
from . import views 

app_name='sliders'


urlpatterns = [ 
    path('list/', views.slider_list, name='slider_list'),
    path('create/', views.slider_create, name='slider_create'),
    path('edit/<int:id>/', views.slider_edit, name='slider_edit'),
    path('delete/<int:id>/', views.slider_delete, name='slider_delete'),
    ]