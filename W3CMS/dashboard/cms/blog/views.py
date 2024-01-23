from django.shortcuts import render, redirect, get_object_or_404
from dashboard.cms.blog.models import Blogs, Metas, Tags, Categories, Seo
from django.core.paginator import Paginator
from django.contrib import messages
from dashboard.cms.blog.forms import BlogForm, MetaForm, SeoForm, CategoriesForm,TagForm
from django.forms import modelformset_factory
from dashboard.users.models import CustomUser
from django.http import JsonResponse
from dashboard.cms.blog.blog_config import ScreenOption
import json
from django.contrib.auth.decorators import login_required, permission_required 
from dashboard.cms import utils
from django.db import IntegrityError
import datetime



@login_required(login_url='dashboard:login')
@permission_required({'blog.view_tags','blog.delete_tags'}, raise_exception=True)
def blogTagDelete(request, id):
    tag = Tags.objects.get(id=id)
    if tag:
        tag.delete()
        messages.success(request,'Tag Delete Successfully')
    
    else:
        messages.warning(request,'Tag Does Not Exist')
    return redirect('dashboard:blog:blogTag')
    


@login_required(login_url='dashboard:login')
@permission_required({'blog.view_tags'}, raise_exception=True)
def blogTag(request):
    template_name = 'blog/tag.html'
    left_side_view = False
    query = request.GET.get('tag-search')
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_obj = tag_form.save(commit=False)
            tag_obj.name = tag_obj.name.lower()
            
            try:
                tag_obj.save()
            except IntegrityError as e:
                messages.warning(request,e.args[0])    
        else:
            messages.warning(request,tag_form.errors)
            
    if query:
        tags = Tags.objects.filter(name__icontains=query)
    else:
        tags = Tags.objects.all().order_by('-updated_at')

    tag_form = TagForm()
    paginator = Paginator(tags, utils.nodes_per_page())
    tags=paginator.get_page(request.GET.get('page'))
    if request.user.has_perm('blog.add_tags'):
        left_side_view=True
    context={
        "page_title":"Tags",
        "tags":tags,
        "tag_form":tag_form,
        "left_side_view":left_side_view,
        "edit":False,
        "query":query
    }   
    

    return render(request, template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'blog.view_tags','blog.change_tags'}, raise_exception=True)
def blogTagEdit(request,id):
    template_name = 'blog/tag.html'
    left_side_view=False,
    tag = Tags.objects.get(id=id)
    query = request.GET.get('tag-search')
    
    if request.method == 'POST':
        tag_form = TagForm(request.POST,instance=tag)

        if tag_form.is_valid():
            tag_obj = tag_form.save(commit=False)
            tag_obj.name = tag_obj.name.lower()
            tag_obj.save()
            return redirect('dashboard:blog:blogTag')
        else:
            messages.warning(request,tag_form.errors)
    

    if query:
        tags = Tags.objects.filter(name__icontains=query)
    else:
        tags = Tags.objects.all().order_by('-updated_at')
            
    tag_form = TagForm(instance=tag)
    paginator = Paginator(tags, utils.nodes_per_page())
    tags=paginator.get_page(request.GET.get('page'))
    if request.user.has_perm('blog.change_tags'):
        left_side_view=True
    context={
        "page_title":"Tags",
        "tags":tags,
        "tag_form":tag_form,
        "left_side_view":left_side_view,
        "edit":True,
        "query":query
    }   
    
    return render(request, template_name, context)

#Categories

@login_required(login_url='dashboard:login')
@permission_required({'blog.view_categories'}, raise_exception=True)
def blogCategory(request):
    template_name = 'blog/category.html'
    left_side_view = False
    query = request.GET.get('category-search')
    if request.method == 'POST':
        category_form = CategoriesForm(request.POST)
        if category_form.is_valid():
            category_form.save()
        else:
            messages.warning(request,category_form.errors)
    if query:
        categories = Categories.objects.filter(title__icontains=query)
    else:
        categories = Categories.objects.all()


    category_form = CategoriesForm()
    categories_for_select = Categories.objects.all()
    
    paginator = Paginator(categories, utils.nodes_per_page())
    categories=paginator.get_page(request.GET.get('page'))


    if request.user.has_perm('blog.add_categories'):
        left_side_view=True

    context={
        "page_title":"Categories",
        "categories":categories,
        "category_form":category_form,
        "categories_for_select":categories_for_select,
        "edit":False,
        "left_side_view":left_side_view,
        "query":query
    }
    return render(request, template_name,context)




@login_required(login_url='dashboard:login')
@permission_required({'blog.view_categories','blog.change_categories'}, raise_exception=True)
def blogCategoryEdit(request,id):
    template_name = 'blog/category.html'
    left_side_view = False
    category = Categories.objects.get(id=id)
    query = request.GET.get('category-search')
    
    if request.method == 'POST':
        category_form = CategoriesForm(request.POST,instance=category)
        
        if category_form.is_valid():
            category_form.save()
            return redirect("dashboard:blog:blogCategory")
        else:
            messages.warning(request,category_form.errors)



    if query:
        categories = Categories.objects.filter(title__icontains=query)
    else:
        categories = Categories.objects.all()
        
    category_form = CategoriesForm(instance=category)
    categories_for_select = Categories.objects.all().exclude(id=id)
    
    paginator = Paginator(categories, utils.nodes_per_page())
    categories=paginator.get_page(request.GET.get('page'))
    if request.user.has_perm('blog.change_categories'):
        left_side_view=True
    context={
        "page_title":"Categories",
        "categories":categories,
        "category_form":category_form,
        "categories_for_select":categories_for_select,
        "edit":True,
        "left_side_view":left_side_view,
        "query":query
    }
    return render(request, template_name,context)
    

@login_required(login_url='dashboard:login')
@permission_required({'blog.view_categories','blog.delete_categories'}, raise_exception=True)
def blogCategoryDelete(request,id):
    category = Categories.objects.get(id=id)
    if category:
        category.delete()
        messages.success(request,'Category Delete Successfully')
    else:
        messages.warning(request,'Category Does Not Exist')
    return redirect('dashboard:blog:blogCategory')
    



@login_required(login_url='dashboard:login')
@permission_required({'blog.view_blogs'}, raise_exception=True)
def cms_blog_list(request):
    template_name = 'blog/blogs.html'
    blog_list = None
    filter_form_data={}
    message=''
    blogs=None
    status=[
        {"label":"Select Status","value":""},
        {"label":"Published","value":"Published"},
        {"label":"Draft","value":"Draft"},
        {"label":"Pending","value":"Pending"}
        ]
    
    
    if request.method=='POST':
        filter_title = request.POST.get('filter-blog-title').strip()
        filter_status = request.POST.get('filter-blog-status')
        filter_date = request.POST.get('filter-blog-bydate').strip()
        print('blog_title: ',filter_title)
        print('blog_status: ',filter_status)
        print('blog_date: ',filter_status)

        filter_form_data = {
            "filter_title":filter_title,
            "filter_status":filter_status,
            "filter_date":filter_date
        }
        blog_list = utils.data_filter(filter_form_data,Blogs)

        if filter_form_data:
            request.session['blog_filter_data']=filter_form_data
    else:
        if 'blog_filter_data' in list(request.session.keys()) and 'page' in list(request.GET.keys()):
            session_data = request.session.get('blog_filter_data')
            blog_list = utils.data_filter(session_data,Blogs)
            filter_form_data=request.session.get('blog_filter_data')
        else:
            blog_list = Blogs.objects.all()
            if 'blog_filter_data' in list(request.session.keys()):
                del request.session['blog_filter_data']
    
    
    if blog_list:
        paginator = Paginator(blog_list, utils.nodes_per_page())
        blogs=paginator.get_page(request.GET.get('page'))
    else:
        message='Data Not Found'
    context={
        "blogs": blogs,
        "status":status,
        "form_data":filter_form_data,
        'message':message,
        "page_title":"Blogs"
    }
    return render(request, template_name, context)

@login_required(login_url='dashboard:login')
@permission_required({'blog.view_blogs','blog.add_blogs'}, raise_exception=True)
def cms_blog_create(request):
    template_name = 'blog/blog_create_update.html'
    Blog_MetaFormSet = modelformset_factory(Metas, form=MetaForm, extra=0, can_delete=True)

    if request.method == 'POST':
        context = {
            "blog_form":BlogForm(request.POST, request.FILES),
            "category_form":CategoriesForm(prefix='category'),
            "categories":Categories.objects.all(),
            "blog_meta_formset": Blog_MetaFormSet(request.POST),
            "blog_seo_form":SeoForm(request.POST,prefix='seo'),
            "blog_videourl":Blogs.objects.all(),
            "str_tags":request.POST.get('input-tags').strip('').strip(','),
            "ScreenOption":json.dumps(ScreenOption),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":False,
            "page_title":"Create Blog"
        }
        blog_form = context.get('blog_form')
        blog_meta_formset = context.get('blog_meta_formset')
        blog_seo_form = context.get('blog_seo_form')
        str_tags = context.get('str_tags')



        if blog_form.is_valid():
            blog_obj = blog_form.save(commit=False)

            blog_obj.user = CustomUser.objects.get(id=int(request.POST.get('user')))
            if blog_obj.publish_on == None or blog_obj.publish_on == '':
                blog_obj.publish_on = datetime.date.today()
            blog_obj.save()

            cat_checks_id_list = request.POST.getlist('cat_checks[]')
            if len(cat_checks_id_list)!=0:
                for id in cat_checks_id_list:
                    blog_obj.categories.add(Categories.objects.get(id=int(id))) 
            blog_obj.save()

            if str_tags != '' and str_tags != None:
                for input_tag in str_tags.split(','):
                    input_tag=input_tag.lower()
                    if utils.slugify(input_tag) not in Tags.objects.all().values_list('slug', flat=True):
                        blog_obj.tags.create(name=input_tag)
                    else:
                        blog_obj.tags.add(Tags.objects.get(slug=utils.slugify(input_tag)))
                    blog_obj.save()

            if blog_meta_formset.is_valid():
                for metaform in blog_meta_formset:
                    print("########CLEAN DATA CRATE#####")
                    print(metaform.cleaned_data)
                    meta_obj = metaform.save(commit=False)
                    meta_obj.blog = blog_obj
                    if len(metaform.cleaned_data) > 0:
                        meta_obj.save()

                        

                # for blog_metaform in blog_meta_formset:
                #     blog_metaform_obj = blog_metaform.save(commit=False)
                #     blog_metaform_obj.blog = blog_obj
                #     blog_metaform_obj.save()
            else:
                blog_obj.delete()
                messages.warning(request,'Somthing want wrong in Add Custom Fields')
                return render(request,template_name, context)

            if blog_seo_form.is_valid():
                blog_seo_obj = blog_seo_form.save(commit=False)
                blog_seo_obj.blog = blog_obj
                blog_seo_obj.save()
                return redirect('dashboard:blog:blogs')
            else:
                blog_obj.delete()
                messages.warning(request,'Somthing want wrong in SEO Fields')
                return render(request,template_name, context)
        else:
            print(blog_form.errors)
            messages.warning(request,'Somthing want wrong in Blog')
    else:
        context = {
            "blog_form":BlogForm(),
            "category_form":CategoriesForm(prefix='category'),
            "categories":Categories.objects.all(),
            "blog_meta_formset": Blog_MetaFormSet(queryset=Metas.objects.none()),
            "blog_seo_form":SeoForm(prefix='seo'),
            "blog_videourl":Blogs.objects.all(),
            "ScreenOption":json.dumps(ScreenOption),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":False,
            "page_title":"Create Blog"
        }
    return render(request, template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'blog.view_blogs','blog.change_blogs'}, raise_exception=True)
def cms_blog_edit(request, id):
    template_name = 'blog/blog_create_update.html'
    blog_obj = get_object_or_404(Blogs,id=id)
    seo_obj = Seo.objects.get(blog=blog_obj)
    Blog_MetaFormSet = modelformset_factory(Metas, form=MetaForm, extra=0, can_delete=True)
    Blog_MetaQuerySet = Metas.objects.filter(blog=blog_obj).order_by('-updated_at')

    if request.method == 'POST':
        context = {
            "blog_form":BlogForm(request.POST, request.FILES, instance=blog_obj),
            "category_form":CategoriesForm(prefix='category'),
            "categories":Categories.objects.all(),
            "selected_categories":list(blog_obj.categories.all()),
            "blog_meta_formset": Blog_MetaFormSet(request.POST,queryset=Blog_MetaQuerySet),
            "blog_seo_form":SeoForm(request.POST,prefix='seo',instance=seo_obj),
            "blog_videourl":Blogs.objects.all(),
            "str_tags":request.POST.get('input-tags').strip('').strip(','),
            "ScreenOption":json.dumps(ScreenOption),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":True,
            "page_title":"Edit Blog"
        }
        blog_form = context.get('blog_form')
        blog_meta_formset = context.get('blog_meta_formset')
        blog_seo_form = context.get('blog_seo_form')
        str_tags = context.get('str_tags')

        if blog_form.is_valid():
            blog_obj = blog_form.save(commit=False)

            blog_obj.user = CustomUser.objects.get(id=int(request.POST.get('user')))
            if blog_obj.visibility == 'Pu' or blog_obj.visibility == 'Pr':
                blog_obj.password = None
            blog_obj.save()

            cat_checks_id_list = request.POST.getlist('cat_checks[]')
            blog_obj.categories.clear()

            if len(cat_checks_id_list)!=0:
                for id in cat_checks_id_list:
                    blog_obj.categories.add(Categories.objects.get(id=int(id)))
            blog_obj.save()

            if str_tags != '' and str_tags != None:
                for input_tag in str_tags.split(','):
                    input_tag=input_tag.lower()
                    if utils.slugify(input_tag) not in Tags.objects.all().values_list('slug', flat=True):
                        blog_obj.tags.create(name=input_tag)
                    else:
                        blog_obj.tags.add(Tags.objects.get(slug=utils.slugify(input_tag)))
                    blog_obj.save()

            if blog_meta_formset.is_valid():
                for metaform in blog_meta_formset:
                    print('######CLEAN DATA######')
                    print(metaform.cleaned_data)
                    meta_obj = metaform.save(commit=False)
                    meta_obj.blog = blog_obj
                    if len(metaform.cleaned_data) > 0:
                        if metaform.cleaned_data["DELETE"]:
                            meta_obj.delete()
                        else:
                            meta_obj.save()
            else:
                messages.warning(request,'Somthing want wrong in Add Custom Fields')
                return render(request,template_name, context)

            if blog_seo_form.is_valid():
                blog_seo_obj = blog_seo_form.save(commit=False)

                blog_seo_obj.blog = blog_obj
                blog_seo_obj.save()
                return redirect('dashboard:blog:blogs')
            else:
                messages.warning(request,'Somthing want wrong in SEO Fields')
                return render(request,template_name, context)
        else:
            messages.warning(request,'Somthing want wrong in Blog')
    

        
    else:
        context = {
            "blog_form":BlogForm(instance=blog_obj),
            "category_form":CategoriesForm(prefix='category'),
            "categories":Categories.objects.all(),
            "selected_categories":list(blog_obj.categories.all()),
            "blog_meta_formset": Blog_MetaFormSet(queryset=Blog_MetaQuerySet),
            "blog_seo_form":SeoForm(prefix='seo',instance=seo_obj),
            "blog_videourl":Blogs.objects.all(),
            "str_tags":','.join(blog_obj.tags.all().values_list('name', flat=True)),
            "ScreenOption":json.dumps(ScreenOption),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":True,
            "page_title":"Edit Blog"
        }
    return render(request, template_name, context)



@login_required(login_url='dashboard:login')
@permission_required({'blog.view_categories','blog.delete_categories'}, raise_exception=True)
def cms_blog_add_category(request):
    if request.method =='POST':
        print(request.POST)
        title = request.POST['name']
        parent = request.POST['parent']

        if parent == '':
            parent = None
        else:
            parent = Categories.objects.get(pk=parent)


        if not Categories.objects.filter(title=title).exists():
            category_obj = Categories(title=title,parent=parent)
            category_obj.save()
            print(category_obj.is_root_node())
            # print(category_obj.is_leaf_node())
            # print(category_obj.is_child_node())
            # print(dir(category_obj))


            if category_obj.is_root_node():
                html_data = f'''<li class="BlogCategory{category_obj.id}">
                                        <div class="form-check custom-checkbox">
                                            <input type="checkbox" name="cat_checks[]" value="{category_obj.id}" class="form-check-input blog_categories">
                                            <label class="form-check-label">{category_obj.title}</label>
                                        </div>
                                    </li>'''
            else:
                html_data = f'''<ul class="category-checkbox-list">                      
                                        <li class="BlogCategory{category_obj.id}">
                                            <div class="form-check custom-checkbox">
                                                <input type="checkbox" name="cat_checks[]" value="{category_obj.id}" class="form-check-input blog_categories">
                                                <label class="form-check-label">{category_obj.title}</label>
                                            </div>
                                        </li>
                                    </ul>'''

            # for cat in Categories.objects.all():
            #     print(cat.title)
            #     print(cat.level)
            indent = '+--'
            select_option_html = f'<option value="{category_obj.id}">{category_obj.level * indent }{category_obj.title}</option>'

            response = JsonResponse({"success": {'html_data':html_data, 'select_option_html':select_option_html} })
        else:
            print('category already exits')
            response = JsonResponse({"warning": 'Category already exists'})

        return response



@login_required(login_url='dashboard:login')
@permission_required({'blog.view_blogs','blog.delete_blogs'}, raise_exception=True)
def cms_blog_delete(request,id):
    blog = Blogs.objects.get(id=id)
    if blog:
        blog.delete()
        messages.success(request,'Blog Delete Successfully')
    
    else:
        messages.warning(request,'Blog Does Not Exist')
    return redirect('dashboard:blog:blogs')


@login_required(login_url='dashboard:login')
@permission_required({'blog.view_blogs','blog.delete_blogs'}, raise_exception=True)
def delete_multiple_blogs(request):
    response = {
                    'waring':'Something Went Wrong'
                }
    if request.method=='POST':
        id_list=request.POST.getlist('ids[]')
        id_list = [i for i in id_list if i != '']
        for id in id_list:
            blog_obj = Blogs.objects.get(id=id)
            if blog_obj:
                blog_obj.delete()
                response = JsonResponse({"success": 'Blog deleted successfully'})
            else:
                response = JsonResponse({"warning": f'Id {id} is not valid'})

    return response