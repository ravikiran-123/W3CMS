from django.urls import path ,include
from frontend import views
from django.urls import re_path
from django.http.request import HttpRequest

app_name='frontend'

#httphost = HttpRequest()
#httphost2 = httphost.get_host()

#print('httphost2')
#print(HttpRequest.path)


urlpatterns = [
    
path('home/',views.index,name="home"),
     path('', views.home_slider, name='home_slider'),
    path('footer/', views.footerblog_list, name='footer_blog_list'),
    # path('contact_us/',views.contactus,name="contactus"),
    path('<slug:slug>/',views.page_detail,name="page-detail"),  
    path('blogs/list=true/',views.blog_list,name="blog_list"),#Blogs list and Search 
    path('home/blogs/list=true/',views.blog_list,name="blog_list"),#Blogs list and Search 

    path('blog/<slug:slug>/',views.blog_detail,name="blog-detail"),
    path('author/<str:username>/',views.author,name="author"),
    path('tag/<slug:slug>/',views.blogtag,name="blogtag"),
    path('category/<slug:slug>/',views.blogcategory,name="blogcategory"),
    
    path('archive/<int:year>/<int:month>/', views.month_archive, name="archive"),
    # path('video/', views.Video_url, name="Video_url")

    # re_path(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name="archive"),




 
]