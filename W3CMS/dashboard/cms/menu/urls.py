from django.urls import path 
from dashboard.cms.menu.views import (

    cms_menu_setup,
    cms_menu_item_delete,
    cms_menu_structure_save,
    cms_menu_create,
    cms_menu_delete,
    cms_search_menu,
    add_menu_content,
    add_link_to_menu

)

app_name='menu'
urlpatterns = [
    path('setup/', cms_menu_setup, name='setup'),
    path('setup/<int:id>/', cms_menu_setup, name='setup'),
    path('menu_item_delete/', cms_menu_item_delete, name='menu_item_delete'),
    path('menu_structure_save/', cms_menu_structure_save, name='menu_structure_save'),
    path('create_menu/', cms_menu_create, name='create_menu'),
   
    path('menu_delete/', cms_menu_delete, name='menu_delete'),
    path('search_menu/', cms_search_menu, name='search_menu'),
    
    path('add_content_to_menu/',add_menu_content, name='add_content_to_menu'),
    path('add_link_to_menu/',add_link_to_menu, name='add_link_to_menu'),

]