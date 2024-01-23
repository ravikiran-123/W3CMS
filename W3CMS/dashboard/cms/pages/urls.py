from django.urls import path, include
from dashboard.cms.pages.views import ( 
                                        cms_page_list,
                                        cms_page_create,
                                        cms_page_delete,
                                        cms_page_edit,
                                        # custom_field_delete,
                                        delete_multiple_pages,
                                      
                                    )
app_name = 'pages'
urlpatterns = [
    path('',cms_page_list, name='pages'),
    path('create/',cms_page_create, name='page_create'),
    path('page_delete/<int:id>/',cms_page_delete, name='page_delete'),
    path('page_edit/<int:id>/',cms_page_edit, name='page_edit'),
    # path('custom_field_delete/<int:id>/',custom_field_delete, name='custom_field_delete'),
    path('delete-multiple-pages/',delete_multiple_pages, name='delete-multiple-pages'),

]