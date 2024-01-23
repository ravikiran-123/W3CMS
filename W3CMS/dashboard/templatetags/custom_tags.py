from django import template
from django.urls import resolve
from django.urls.exceptions import Resolver404
from loguru import logger
from dashboard.cms.menu.models import Menus, Items
from dashboard.cms.pages.models import Page
from dashboard.cms.blog.models import Blogs,Categories,Tags
from dashboard.models import Configurations
import json



register = template.Library()



#This the custom filter, name is getitems

def getdata(json_data, args):    
    func_name=''
    try:
        myfunc, myargs, mykwargs = resolve(args)
        if myfunc:
            logger.success("*"*50)
            print()
            logger.debug("Function Name:> {} ",myfunc.__name__,feature="f-strings")
            logger.debug("Module Name:> {} ",myfunc.__module__,feature="f-strings")
            logger.debug("URL_Path:> {} ",args,feature="f-strings")
            func_name=myfunc.__name__
            print()
            logger.success("*"*50)
    except Resolver404:
        logger.debug("something went wrong",feature="f-strings")
        pass

    return json_data.get(func_name)


register.filter('getdata', getdata)



# Get Menus

def getMenu(menu_slug):
    menu_items=[]
    if Menus.objects.filter(slug=menu_slug).exists():
        menu_object = Menus.objects.get(slug=menu_slug)
        menu_items = Items.objects.filter(menu=menu_object)
    return menu_items
    
register.filter('getMenu', getMenu)





def getMenuItemUrl(item_type,id):
    base_url=''

    if item_type == 'Page':

        if Page.objects.filter(id=id).exists():
            page_obj = Page.objects.get(id=id)
            slug=page_obj.slug
            base_url=f'/{slug}/'
        else:
            base_url='#'
        
    if item_type == 'Blog':
        if Blogs.objects.filter(id=id).exists():
            blog_obj = Blogs.objects.get(id=id)
            slug = blog_obj.slug
            base_url=f'/blog/{slug}/'
        else:
            base_url='#'

    return base_url

register.filter('getMenuItemUrl', getMenuItemUrl)




def is_menu_item_delete(item_type,item_id):

    is_deleted=''

    if item_type == 'Page':
        if Page.objects.filter(id=item_id).exists():
            is_deleted=False
        else:
            is_deleted=True

    if item_type == 'Blog':
        if Blogs.objects.filter(id=item_id).exists():
            is_deleted=False
        else:
            is_deleted=True

    return is_deleted

register.filter('is_menu_item_delete', is_menu_item_delete)



def getAllprefix(var):
    name_list = Configurations.objects.all().order_by('created_at').values_list('name',flat=True)
    prefixes=[]
    for name in name_list:
        if len(name.split('.')) > 1:
            prefix=name.split('.')[0]
            if prefix not in prefixes:
                prefixes.append(prefix)
        else:
            prefixes.append(name)            
    
    return prefixes

register.filter('getAllprefix', getAllprefix)



def split(val,args):
    return val.split(args)
register.filter('split', split)


def getWidgetCategories(val):
    return Categories.objects.all()
register.filter('getWidgetCategories', getWidgetCategories)

def getRecentPOST(count):
    blogs = Blogs.objects.filter(status='Published').exclude(visibility='Pr').order_by('-publish_on')[:int(count)]
    return blogs
register.filter('getRecentPOST', getRecentPOST)


def getPopularTags(val):
    tags = Tags.objects.all()
    return tags
register.filter('getPopularTags', getPopularTags)


def getWidgetArchives(val):
    import datetime as dt
   
    arc_list = []
    month_temp_list = []
    archive_list = Blogs.objects.filter(status='Published').exclude(visibility='Pr').values_list("publish_on",flat=True)

    for date in set([i.strftime("%Y-%m-%d") for i in archive_list]):
        date_splited = date.split('-')
        year = int(date_splited[0])
        month = int(date_splited[1])
        day = int(date_splited[2])
        
        if month not in month_temp_list:
            arc_list.append(dt.date(year,month,day)) 
            month_temp_list.append(month)
    return arc_list
register.filter('getWidgetArchives', getWidgetArchives)


def multiply(val1,val2):
    return val1*val2
register.filter('multiply', multiply)



# def getCustomRedirLang(url_fullpath):
#     ls_urls = url_fullpath.split('/')
#     print(ls_urls)
    
#     #dashboard = 'dashboard'
#     #if ls_urls [1] == dashboard: 
#     #del ls_urls[1]
#     return '/'.join(ls_urls)

# register.filter('getCustomRedirLang', getCustomRedirLang)





# def getStringToJson(val):
#     print("String to Dict")
#     print(val)
#     print(type(val))
   
#     return val
    
# register.filter('getStringToJson', getStringToJson)


# request.path	                  /home/
# request.get_full_path	         /home/?q=test
# request.build_absolute_uri	 http://127.0.0.1:8000/home/?q=test