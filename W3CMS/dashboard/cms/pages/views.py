from django.shortcuts import render, redirect, get_object_or_404
from dashboard.cms.pages.models import Page, PageMeta, PageSeo
from dashboard.cms.pages.forms import PageForm, PageMetaForm, PageSeoForm
from django.contrib import messages
from dashboard.users.models import CustomUser
from django.forms import modelformset_factory
from dashboard.cms.pages.page_config import ScreenOption
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required, permission_required 
from dashboard.cms import utils




@login_required(login_url='dashboard:login')
@permission_required({'pages.view_page'}, raise_exception=True)
def cms_page_list(request):
    template_name = 'pages/pages.html'
    page_list=None
    filter_form_data={}
    message=''
    pages=None
    status=[
        {"label":"Select Status","value":""},
        {"label":"Published","value":"Published"},
        {"label":"Draft","value":"Draft"},
        {"label":"Pending","value":"Pending"}
        ]

    if request.method == 'POST':
        filter_title = request.POST.get('filter-page-title').strip()
        filter_status = request.POST.get('filter-page-status')
        filter_date = request.POST.get('filter-page-bydate').strip()

        filter_form_data = {
            "filter_title":filter_title,
            "filter_status":filter_status,
            "filter_date":filter_date
        }
        page_list = utils.data_filter(filter_form_data,Page)

        if filter_form_data:
            request.session['page_filter_data'] = filter_form_data
    else:
        if 'page_filter_data' in list(request.session.keys()) and 'page' in list(request.GET.keys()):
            session_data = request.session.get('page_filter_data')
            page_list = utils.data_filter(session_data,Page)
            filter_form_data=request.session.get('page_filter_data')
        else:
            page_list = Page.objects.all()
            if 'page_filter_data' in list(request.session.keys()):
                del request.session['page_filter_data']
    if page_list:
        paginator = Paginator(page_list, utils.nodes_per_page()) 
        pages = paginator.get_page(request.GET.get('page'))
    else:
        message = 'Data Not Found'
    context={
        "pages": pages,
        "status":status,
        "form_data":filter_form_data,
        'message':message,
        "page_title":"Pages"
    }
    return render(request, template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'pages.view_page','pages.delete_page'}, raise_exception=True)
def cms_page_delete(request,id):
    page = Page.objects.get(id=id)
    if page:
        page.delete()
        messages.success(request,'Page Delete Successfully')
    else:
        messages.warning(request,'Page Does Not Exist')
    return redirect('dashboard:pages:pages')

@login_required(login_url='dashboard:login')
@permission_required({'pages.view_page','pages.add_page'}, raise_exception=True)
def cms_page_create(request):
    template_name = 'pages/page_create_update.html'
    Page_MetaFormSet = modelformset_factory(PageMeta, form=PageMetaForm, extra=0, can_delete=True)

    if request.method == 'POST':
        context={
            "form_page" : PageForm(request.POST, request.FILES),
            "form_page_seo" : PageSeoForm(request.POST, prefix='seo'),
            "page_meta_formset": Page_MetaFormSet(request.POST),
            "ScreenOption":json.dumps(ScreenOption),
            "pages":Page.objects.all(),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":False,
            "page_title":"Create Page"
        }
        form_page = context.get('form_page')
        form_page_seo = context.get('form_page_seo')
        page_meta_formset = context.get('page_meta_formset')
        if form_page.is_valid():
            page_obj = form_page.save()

            if page_meta_formset.is_valid():
                for page_metaform in page_meta_formset:
                    print("########CLEAN DATA CRATE#####")
                    print(page_metaform.cleaned_data)
                    page_metaform_obj=page_metaform.save(commit=False)
                    page_metaform_obj.page = page_obj
                    print("page_metaform_obj Len: ",len(page_metaform.cleaned_data))
                    if len(page_metaform.cleaned_data) > 0:
                        page_metaform_obj.save()
            else:
                page_obj.delete()
                messages.warning(request,'Somthing went wrong in Add Custom Fields')
                return render(request,template_name, context)

            if form_page_seo.is_valid():
                page_seo_obj = form_page_seo.save(commit=False)
                page_seo_obj.page = page_obj
                page_seo_obj.save()
                return redirect('dashboard:pages:pages')
            else:
                page_obj.delete()
                messages.warning(request,'Somthing went wrong in SEO Fields')
                return render(request,template_name, context)
        else:
            messages.warning(request,'Somthing went wrong in Page')
    else:
        context={
            "form_page" : PageForm(),
            "page_meta_formset": Page_MetaFormSet(queryset=PageMeta.objects.none()),
            "form_page_seo" : PageSeoForm(prefix='seo'),
            "ScreenOption":json.dumps(ScreenOption),
            "pages":Page.objects.all(),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":False,
            "page_title":"Create Page"
        }
    return render(request,template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'pages.view_page','pages.change_page'}, raise_exception=True)
def cms_page_edit(request,id):
    template_name = 'pages/page_create_update.html'
    PageMetaFormSet = modelformset_factory(PageMeta, form=PageMetaForm, extra=0, can_delete=True)
    page = get_object_or_404(Page,id=id)
    pageseo = PageSeo.objects.get(page=page)
    pagemeta_queryset = PageMeta.objects.filter(page=page).order_by('created_at')
    
    if request.method == 'POST':
        
        context={
            "form_page" : PageForm(request.POST, request.FILES, instance=page),
            "page_meta_formset": PageMetaFormSet(request.POST, queryset=pagemeta_queryset),
            "form_page_seo" : PageSeoForm(request.POST,prefix='seo',instance=pageseo),
            "ScreenOption":json.dumps(ScreenOption),
            "pages":Page.objects.all(),
            "users":CustomUser.objects.filter(is_superuser=False),
            "edit":True,
            "page_title":"Edit Page"
        }
        form_page = context.get('form_page')
        form_page_seo = context.get('form_page_seo')
        page_meta_formset = context.get('page_meta_formset')
        
        if form_page.is_valid():
            page_obj = form_page.save(commit=False)
            if page_obj.visibility == 'Pu' or page_obj.visibility == 'Pr':
                page_obj.password = None
            page_obj.save()
            if page_meta_formset.is_valid():
                for page_metaform in page_meta_formset:
                    print('######CLEAN DATA######')
                    print(page_metaform.cleaned_data)
                    page_metaform_obj=page_metaform.save(commit=False)
                    page_metaform_obj.page = page_obj

                    if len(page_metaform.cleaned_data) > 0:
                        if page_metaform.cleaned_data["DELETE"]:
                            page_metaform_obj.delete()
                        else:
                            page_metaform_obj.save()
            else:
                print(page_meta_formset.errors)
                messages.warning(request,'Somthing went wrong in Add Custom Fields')
                return render(request,template_name, context)

            if form_page_seo.is_valid():
                page_seo_obj = form_page_seo.save(commit=False)
                page_seo_obj.page = page_obj
                page_seo_obj.save()
                return redirect('dashboard:pages:pages')
            else:
                messages.warning(request,'Somthing went wrong in SEO Fields')
                return render(request,template_name, context)
        else:
            messages.warning(request,'Somthing went wrong in Page Fields')
    
    else:
        context={
                "form_page" : PageForm(instance=page),
                "page_meta_formset": PageMetaFormSet(queryset=pagemeta_queryset),
                "form_page_seo" : PageSeoForm(prefix='seo',instance=pageseo),
                "ScreenOption":json.dumps(ScreenOption),
                "pages":Page.objects.all(),
                "users":CustomUser.objects.filter(is_superuser=False),
                "edit":True,
                "page_title":"Edit Page"
            }
    return render(request,template_name, context)

@login_required(login_url='dashboard:login')
@permission_required({'pages.view_page','pages.delete_page'}, raise_exception=True)
def delete_multiple_pages(request):
    if request.method=='POST':
        id_list=request.POST.getlist('ids[]')
        id_list = [i for i in id_list if i != '']
        for id in id_list:
            page_obj = Page.objects.get(id=id)
            if page_obj:
                page_obj.delete()
                response = JsonResponse({"success": 'Page deleted successfully'})
            else:
                response = JsonResponse({"warning": f'Id {id} is not valid'})

    return response



