from django.urls import path, include
from dashboard.cms.contactus import views


app_name='contactus'
urlpatterns = [
    path('',views.contact_us, name='contact-us'),
    path('edit/<int:id>/',views.edit_contact_us, name='edit-contact-us'),
    path('view/',views.view_contact_us, name='view-contact-us'),
    path('delete/<int:id>/',views.delete_contact_us, name='delete-contact-us'),
   
]

