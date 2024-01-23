from django.urls import path 
from dashboard.cms.comment.views import (
                                        cms_comment_list, 
                                        blogCommentEdit,
                                        blogCommentDelete,
                                        delete_multiple_comments, 
                                    )


app_name='comment'
urlpatterns = [
    path('', cms_comment_list, name='comments'),
    path('edit/<int:id>/',blogCommentEdit, name='blogCommentEdit'),
    path('delete/<int:id>/',blogCommentDelete, name='blogCommentDelete'),
    path('delete-multiple-comments/',delete_multiple_comments, name='delete-multiple-comments'),
    
]