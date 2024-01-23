
from django.contrib import messages
from django.shortcuts import render,redirect
from dashboard.cms.blog.models import Blogs, Categories
from dashboard.cms.menu.models import  Menus, Items
from dashboard.cms.pages.models import Page
from django.http import JsonResponse
from dashboard.cms.menu.menu_config import ScreenOption
from django.contrib.auth.decorators import login_required, permission_required 

import json

type_dict = {
    "Page":"Page",
    "Blog":"Blog",
    "Category":"Category",
    "CustomLink":"CustomLink"
}


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_menus'}, raise_exception=True)
def cms_menu_setup(request,id=None):
    template_name = 'menu/menu_setup.html'
    menu_type_view=False

    # Create Menu
    if request.method == 'POST':
        menu_name = request.POST.get('menu_create').strip()
        # print('menu_name')
        # print(menu_name)
        if menu_name:
            menu_obj = Menus(title=menu_name,user=request.user)
            menu_obj.save()

            

            return redirect(f'/dashboard/menus/setup/{menu_obj.id}/')
    # Create Menu END

    if id==None:
        menu_count = Menus.objects.all().count()
        if menu_count > 0:
            menu_obj = Menus.objects.all().first()
            menu_items = Items.objects.filter(menu=menu_obj)
        else:
            menu_obj=None
            menu_items=None
    else:
        menu_obj = Menus.objects.get(id=id)
        menu_items = Items.objects.filter(menu=menu_obj)

    if request.user.has_perm('menu.add_items'):
        menu_type_view=True
    
    context={
        "menu_items":menu_items,
        "menu_obj":menu_obj,
        "menus":Menus.objects.all(),
        "pages":Page.objects.filter(status='Published'),
        "blogs":Blogs.objects.filter(status='Published'),
        "categories":Categories.objects.all(),
        "ScreenOption":json.dumps(ScreenOption),
        "page_title":"Menu Setup",
        "menu_type_view":menu_type_view
    }
    return render(request, template_name, context)

@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items','menu.add_items'}, raise_exception=True)
def add_link_to_menu(request):
    html_data=''
    menu_obj = Menus.objects.get(id=request.POST.get('menu_id'))


    if request.method == 'POST':
        new_menu_item = Items(  menu=menu_obj,
                                title=request.POST.get('linktitle').strip(),
                                type='Link',
                            
                                link = request.POST.get('link')
                            )
        new_menu_item.save()
        html_data = f'''
                <li class="dd-item menu-ac-item xLi_{new_menu_item.id}" data-id="{new_menu_item.id}">
                    <!-- <div class="dd-handle"></div> -->
                    <div class="accordion" id="accordionExample-1">
                        <div class="accordion-item">
                            <div class="accordion-header p-0 border-0" id="heading-1">
                                <div class="move-media dd-handle" style="cursor: move;">
                                    <i class="fa-solid fa-arrows-up-down-left-right"></i>
                                </div>
                                <button class="accordion-button contact collapsed justify-content-between"  type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{new_menu_item.id}" aria-expanded="false" aria-controls="collapse-{new_menu_item.id}">
                                    
                                    <span class="fw-bold showLabel_{new_menu_item.id}">{new_menu_item.title}</span><span class="mx-3">|</span><span class="text-primary">{new_menu_item.type}</span>
                                </button>

                            </div>
                            <div id="collapse-{new_menu_item.id}" class="accordion-collapse collapse" aria-labelledby="heading-1" data-bs-parent="#accordionExample-1" style="">
                                <div class="accordion-body dd-content">
                                    
                                    <div class="row">
                                        <div class="col-xl-6">
                                                <div class="mb-3">
                                                    <label class="form-label">Navigation Label</label>
                                                    <input  type="text" name="item_label{new_menu_item.id}" class="form-control itemLabel" id="MenuItem{new_menu_item.id}Title" value="{new_menu_item.title}" rel="{new_menu_item.id}">
                                                    
                                                </div>	
                                        </div>
                                        <div class="col-xl-6 XTitleAttribute" >
                                                <div class="mb-3">
                                                    <label class="form-label">Title Attribute</label>
                                                    <input type="text" name="item_title_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}TitleAttribute" value="">
                                                </div>
                                        </div>
                                        <div class="col-xl-6 XClassAttribute">
                                                <div class="mb-3">
                                                    <label class="form-label">Class Attribute</label>
                                                    <input type="text" name="item_class_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}ClassAttribute" value="">
                                                </div>
                                        </div>
                                        <div class="col-xl-6 XTargetAttribute">
                                                <div class="mb-3">
                                                    <label class="form-label">Target Attribute</label>
                                                    <input type="text" name="item_target_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}TargetAttribute" value="">
                                                </div>
                                        </div>
                                        <div class="col-xl-12 XDescription">
                                                <div class="mb-3">
                                                    <label class="form-label">Description</label>
                                                    <textarea name="item_description{new_menu_item.id}" class="form-control" rows="4" id="MenuItem{new_menu_item.id}Description"></textarea>
                                                </div>
                                        </div>
                                    
                                        <div class="col-xl-12">
                                                <div class="mb-3">
                                                    <label class="form-label">Link</label>
                                                    <input type="text" name="item_url{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}Link" value="{new_menu_item.link}">
                                                </div>
                                        </div>
                                    
                                        <div class="d-flex align-items-center">'''
                                        
                                        
        if request.user.has_perm('menu.delete_items'):
            html_data += f''' <a href="javascript:void(0);" class="RemoveItem text-primary" rel="{new_menu_item.id}" item-name="{new_menu_item.title}">Remove</a><span class="mx-2">|</span>'''


        html_data += '''
            <a href="javascript:void(0);" class="CancelItem" >Cancel</a>            
                </div>
                </div>

                </div>
                </div>
                </div>
                </div>	

                </li>
                '''

    if html_data:
        response = JsonResponse({"success":html_data })
    else:
        response = JsonResponse({"error":'item not found' })

    response.status_code = 200
    return response
   
@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items','menu.add_items'}, raise_exception=True)
def add_menu_content(request):
    html_data=''
    if request.method == 'POST':
        item_ids=request.POST.getlist('MenuItem[]')
        menu_type=request.POST.get('menu_type')
        menu_id=request.POST.get('menu_id')
        menu_obj = Menus.objects.get(id=menu_id)

    
        if menu_type == 'Page':
            allItems = Page.objects.filter(id__in=item_ids)
            linkType   = 'Page'

        if menu_type == 'Blog':
            allItems = Blogs.objects.filter(id__in=item_ids)
            linkType   = 'Blog'

        if menu_type == 'Category':
            allItems = Categories.objects.filter(id__in=item_ids)
            linkType   = 'Category'

        if allItems:
            for item_obj in allItems:
                new_menu_item = Items(
                                    menu=menu_obj,
                                    title=item_obj.title,
                                    item_id=item_obj.id, #item_id
                                    type=linkType,
                                    
                                    )
                new_menu_item.save()
                html_item = f'''
                    <li class="dd-item menu-ac-item xLi_{new_menu_item.id}" data-id="{new_menu_item.id}">
                        <!-- <div class="dd-handle"></div> -->
                        <div class="accordion" id="accordionExample-1">
                            <div class="accordion-item">
                                <div class="accordion-header p-0 border-0" id="heading-1">
                                    <div class="move-media dd-handle" style="cursor: move;">
                                        <i class="fa-solid fa-arrows-up-down-left-right"></i>
                                    </div>
                                    <button class="accordion-button contact collapsed justify-content-between"  type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{new_menu_item.id}" aria-expanded="false" aria-controls="collapse-{new_menu_item.id}">
                                        
                                        <span class="fw-bold showLabel_{new_menu_item.id}">{new_menu_item.title}</span><span class="mx-3">|</span><span class="text-primary">{new_menu_item.type}</span>
                                    </button>

                                </div>
                                <div id="collapse-{new_menu_item.id}" class="accordion-collapse collapse" aria-labelledby="heading-1" data-bs-parent="#accordionExample-1" style="">
                                    <div class="accordion-body dd-content">
                                        
                                        <div class="row">
                                            <div class="col-xl-12">
                                                    <div class="mb-3">
                                                        <label class="form-label">Navigation Label</label>
                                                        <input  type="text" name="item_label{new_menu_item.id}" class="form-control itemLabel" id="MenuItem{new_menu_item.id}Title" value="{new_menu_item.title}" rel="{new_menu_item.id}">
                                                        
                                                    </div>	
                                            </div>
                                            <div class="col-xl-6 XTitleAttribute">
                                                    <div class="mb-3">
                                                        <label class="form-label">Title Attribute</label>
                                                        <input type="text" name="item_title_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}TitleAttribute" value="">
                                                    </div>
                                            </div>
                                            <div class="col-xl-6 XClassAttribute">
                                                    <div class="mb-3">
                                                        <label class="form-label">Class Attribute</label>
                                                        <input type="text" name="item_class_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}ClassAttribute" value="">
                                                    </div>
                                            </div>
                                            <div class="col-xl-6 XTargetAttribute" >
                                                    <div class="mb-3">
                                                        <label class="form-label">Target Attribute</label>
                                                        <input type="text" name="item_target_attribute{new_menu_item.id}" class="form-control" id="MenuItem{new_menu_item.id}TargetAttribute" value="">
                                                    </div>
                                            </div>
                                            <div class="col-xl-12 XDescription" >
                                                    <div class="mb-3">
                                                        <label class="form-label">Description</label>
                                                        <textarea name="item_description{new_menu_item.id}" class="form-control" rows="4" id="MenuItem{new_menu_item.id}Description"></textarea>
                                                    </div>
                                            </div>

                                            <div class="d-flex align-items-center">'''

                
                if request.user.has_perm('menu.delete_items'):
                    html_item+=f'''<a href="javascript:void(0);" class="RemoveItem text-primary" rel="{new_menu_item.id}" item-name="{new_menu_item.title}">Remove</a><span class="mx-2">|</span>'''


                html_item +=''' <a href="javascript:void(0);" class="CancelItem" >Cancel</a>            
                            </div>
                            </div>

                            </div>
                            </div>
                            </div>
                            </div>	

                            </li>'''
                html_data+=html_item


        if html_data:
            response = JsonResponse({"success":html_data })
        else:
            response = JsonResponse({"error":'item not found' })

    response.status_code = 200
    return response



@login_required(login_url='dashboard:login')
@permission_required({'menu.view_menus','menu.view_items','menu.change_menus','menu.change_items'}, raise_exception=True)
def cms_menu_structure_save(request):
    
    order_no=0

    form_data_dict = {}
    form_data_list = json.loads(request.POST.get('form_data'))
    for field in form_data_list:
        form_data_dict[field["name"]] = field["value"]
        

    # Start Save Menu Structure
    


    dd_data_list = json.loads(request.POST.get('dd_data'))
    menu_data = json.loads(request.POST.get('menu_data'))


    menu_obj = Menus.objects.get(id=menu_data.get('menu_id'))

   

    menu_obj.title = menu_data.get('menu_name')
    menu_obj.save()
    

    for dd_item_data in dd_data_list:
        item_obj = Items.objects.get(id=int(dd_item_data.get('id')))
        #Save ItemForm
        attributes={}
        item_obj.title = form_data_dict.get(f'item_label{item_obj.id}')
        
        
        title_attribute =  form_data_dict.get(f'item_title_attribute{item_obj.id}')
        class_attribute =  form_data_dict.get(f'item_class_attribute{item_obj.id}')
        target_attribute =  form_data_dict.get(f'item_target_attribute{item_obj.id}')
        
        attributes["title"]=title_attribute
        attributes["class"]=class_attribute
        attributes["target"]=target_attribute

                
        item_obj.attributes = attributes
    
        item_obj.description = form_data_dict.get(f'item_description{item_obj.id}')
        item_url = form_data_dict.get(f'item_url{item_obj.id}')
        
        order_no += 1
        item_obj.order=order_no
        

        if item_url:
            item_obj.link = item_url

        #End ItemForm


        parent_id = dd_item_data.get('parent_id')
        if parent_id:
            parent_obj = Items.objects.get(id=int(parent_id))
            item_obj.parent = parent_obj
            item_obj.save()
        else:
            item_obj.parent = None
            item_obj.save()
    #End Save Menu Structure

    response = JsonResponse({"success": 'Menu  Update successfully'})

       
    response.status_code = 200
    return response


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_menus','menu.add_menus'}, raise_exception=True)
def cms_menu_create(request):
    if request.method == 'POST':
        menu_name = request.POST.get('menu_create').strip()
        print('menu_name')
        print(menu_name)
        if menu_name:
            menu_obj = Menus(title=menu_name,user=request.user)
            menu_obj.save()
            return redirect(f'/dashboard/menus/setup/{menu_obj.id}/')
        
    return redirect(f'/dashboard/menus/setup/')   
    

@login_required(login_url='dashboard:login')
@permission_required({'menu.view_menus','menu.delete_menus'}, raise_exception=True)
def cms_menu_delete(request):
    menu_id = int(request.POST.get('menu_id'))
    if menu_id != '' or menu_id != None:
        menu_obj = Menus.objects.get(id=menu_id)
        if menu_obj:
            menu_obj.delete()
            redirect_url = '/dashboard/menus/setup/'
            response = JsonResponse({"success": redirect_url })
        
    else:
        response = JsonResponse({"error": "Menu id not exists" })

    response.status_code = 200
    return response


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items','menu.delete_items'}, raise_exception=True)
def cms_menu_item_delete(request):
    item_id = request.POST.get('item_id')
    item_obj = Items.objects.get(id=item_id)
    if item_obj:
        item_obj.delete()
        response = JsonResponse({"success": 'Menu Item Deleted Successfully'})
    else:
        response = JsonResponse({"error": 'Menu Item Not found'})
    
    response.status_code = 200
    return response




@login_required(login_url='dashboard:login')
@permission_required({'menu.view_menus'}, raise_exception=True)
def cms_search_menu(request):
    page_key = request.POST.get('page_key')
    search_type = request.POST.get('search_type')
    html_data=''

    if search_type == type_dict.get('Page'):
        query_list = Page.objects.filter(title__icontains = page_key).filter(status='Published')
    if search_type == type_dict.get('Blog'):
        query_list = Blogs.objects.filter(title__icontains = page_key).filter(status='Published')
    if search_type == type_dict.get('Category'):
        query_list = Categories.objects.filter(title__icontains = page_key)

    if query_list:
        for object in query_list:
            html_item =f'''
                <div class="form-check custom-checkbox">
                    <input 
                        type="checkbox"
                        name="MenuItem[]"
                        value="{object.id}"
                        class="form-check-input"
                        >
                    <label class="form-check-label">{object.title}</label>
                </div>
            '''
            html_data+=html_item
    else:
        html_data=f'''
        <div class="form-group px-3">
                <p>{search_type} not found.</p>
        </div>'''

    response = JsonResponse({"success":html_data })
    response.status_code = 200

    return response