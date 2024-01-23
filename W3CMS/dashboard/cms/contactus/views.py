from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from dashboard.cms.contactus.models import ContactUs
from dashboard.cms.contactus.forms import ContactusForm
from django.core.paginator import Paginator
from dashboard.cms import utils
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required 



@login_required(login_url='dashboard:login')
@permission_required({'contactus.view_contactus'}, raise_exception=True)
def view_contact_us(request):
    id = request.GET.get('id')
    html_data = None
    if id:
        contact_obj = ContactUs.objects.get(id=id)
        html_data=f'''
            <h4>{contact_obj.name}<h4>
            <h4>{contact_obj.email}<h4>
            <h4>{contact_obj.phone}<h4>
            <h4>{contact_obj.message}<h4>
        '''
        response = JsonResponse({"data": html_data})
        response.status_code = 200
    else:
        response = JsonResponse({"data": html_data})
        response.status_code = 200
        
    return response
        

@login_required(login_url='dashboard:login')
@permission_required({'contactus.view_contactus'}, raise_exception=True)
def contact_us(request):
    template_name = "contact-us/contact-us.html"
    add_edit_view = False
    contact_form = ContactusForm()
    contact_list = ContactUs.objects.all()
    filter_form_data=None
    if request.method == "POST":
        filter_name = request.POST.get('filter-contactus-name')
        filter_email = request.POST.get('filter-contactus-email')
        filter_phone = request.POST.get('filter-contactus-phone')
        
        if filter_name or filter_email or filter_phone:
            contact_form = ContactusForm()
            filter_form_data = {
                "filter_name":filter_name,
                "filter_email":filter_email,
                "filter_phone":filter_phone
            }
            contact_list = utils.data_filter_other(filter_form_data,ContactUs)
            if filter_form_data:
                request.session['contactus_filter_data']=filter_form_data   
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            if name or email or phone:
                contact_form = ContactusForm(request.POST)
                if contact_form.is_valid():
                    contact_form.save()
                    contact_list = ContactUs.objects.all()
                    messages.success(request,"Contact Add Successfully")
                else:
                    messages.warning(request, contact_form.errors)
    else:
        if 'contactus_filter_data' in list(request.session.keys()) and 'page' in list(request.GET.keys()):
            session_data = request.session.get('contactus_filter_data')
            contact_list = utils.data_filter_other(session_data,ContactUs)
            filter_form_data=request.session.get('contactus_filter_data')
        else:
            if 'contactus_filter_data' in list(request.session.keys()):
                del request.session['contactus_filter_data']
            
    if contact_list:
        paginator = Paginator(contact_list, utils.nodes_per_page()) 
        contact_list=paginator.get_page(request.GET.get('page'))


    if request.user.has_perm('contactus.add_contactus'):
        add_edit_view=True

    context={
        "page_title":"Contact Us",
        "contact_list":contact_list,
        "form_data":filter_form_data,
        "contact_form":contact_form,
        "add_edit_view":add_edit_view,
        "edit":False
    }
    return render(request, template_name,context)


@login_required(login_url='dashboard:login')
@permission_required({'contactus.view_contactus','contactus.change_contactus'}, raise_exception=True)
def edit_contact_us(request,id):
    template_name = "contact-us/contact-us.html"
    add_edit_view = False
    contact_us_obj = get_object_or_404(ContactUs,id=id)

    if request.method == "POST":
        contact_form = ContactusForm(request.POST,instance=contact_us_obj)
    
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,"Contact Update Successfully")
            return redirect("dashboard:contactus:contact-us")
        else:
            messages.warning(request, contact_form.errors)
    
    else:
        contact_form = ContactusForm(instance=contact_us_obj)
        

    contact_list = ContactUs.objects.all()
    if contact_list:
        paginator = Paginator(contact_list, utils.nodes_per_page()) 
        contact_list=paginator.get_page(request.GET.get('page'))

    if request.user.has_perm('contactus.change_contactus'):
        add_edit_view=True
    context={
        "page_title":"Contact Us",
        "contact_list":contact_list,
        "contact_form":contact_form,
        "add_edit_view":add_edit_view,
        "edit":True
    }
    return render(request, template_name,context)

@login_required(login_url='dashboard:login')
@permission_required({'contactus.view_contactus','contactus.delete_contactus'}, raise_exception=True)
def delete_contact_us(request,id):
    contact_us_obj = ContactUs.objects.get(id=id)
    
    if contact_us_obj:
        contact_us_obj.delete()
        messages.success(request,'Contact Deleted Successfully')
    else:
        messages.warning(request,'Contact Not Valid')
    return redirect("dashboard:contactus:contact-us")
        
    