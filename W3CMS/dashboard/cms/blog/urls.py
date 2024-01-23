from django.urls import path 
from dashboard.cms.blog.views import (
                                        cms_blog_list,
                                        cms_blog_delete,
                                        cms_blog_create,
                                        cms_blog_add_category,
                                        cms_blog_edit,
                                        # cms_blog_custom_field_delete,
                                        delete_multiple_blogs,
                                        blogCategory,
                                        blogCategoryDelete,
                                        blogCategoryEdit,
                                        blogTag,
                                        blogTagEdit,
                                        blogTagDelete,
                                      
                                       
                                    )


app_name='blog'
urlpatterns = [
    path('', cms_blog_list, name='blogs'),
    path('create/',cms_blog_create, name='blog_create'),
    path('edit/<int:id>',cms_blog_edit, name='blog_edit'),
    path('blog_delete/<int:id>/',cms_blog_delete, name='blog_delete'),
    path('blog_category_add/',cms_blog_add_category, name='blog_category_add'),
    # path('blog_custom_field_delete/<int:id>/',cms_blog_custom_field_delete, name="blog_custom_field_delete"),
    path('delete-multiple-blogs/',delete_multiple_blogs, name='delete-multiple-blogs'),
    
    path('categories/',blogCategory, name='blogCategory'),
    path('category-delete/<int:id>/',blogCategoryDelete, name='blogCategoryDelete'),
    path('category-edit/<int:id>/',blogCategoryEdit, name='blogCategoryEdit'),
    
    path('tags/',blogTag, name='blogTag'),
    path('tag-edit/<int:id>/',blogTagEdit, name='blogTagEdit'),
    path('tag-delete/<int:id>/',blogTagDelete, name='blogTagDelete'),


    

   
]