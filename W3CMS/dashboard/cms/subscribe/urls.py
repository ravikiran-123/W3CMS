from django.urls import path, include
from dashboard.cms.subscribe import views


app_name='subscribe'
urlpatterns = [
    path('',views.subscribe, name='subscribers'),
    path('edit/<int:id>/',views.edit_subscribe, name='edit_subscriber'),
    path('delete/<int:id>/',views.delete_subscriber, name='delete_subscriber'),
    path('post/ajax/addsubscribe/', views.add_subscriber, name = "add-subscriber"),
]