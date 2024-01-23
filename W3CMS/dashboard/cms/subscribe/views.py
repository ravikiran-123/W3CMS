from django.shortcuts import render, redirect, get_object_or_404
from dashboard.cms.subscribe import forms
from dashboard.cms.subscribe.models import Subscribes
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required 
from django.core.paginator import Paginator

from dashboard.cms import utils

@login_required(login_url='dashboard:login')
@permission_required({'subscribe.view_subscribes'},raise_exception=True)
def subscribe(request):
    template_name = "subscribe/subscribe.html"
    add_edit_view = False
    subscribers_list = Subscribes.objects.all()
    filter_form_data=None
    subscribe_form=forms.SubscribeForm()
    
    if request.method == 'POST':
        filter_name = request.POST.get('filter-subscribe-name')
        filter_email = request.POST.get('filter-subscribe-email')
        filter_phone = request.POST.get('filter-subscribe-phone')
        
        if filter_name or filter_email or filter_phone:
            subscribe_form=forms.SubscribeForm()
            filter_form_data = {
                "filter_name":filter_name,
                "filter_email":filter_email,
                "filter_phone":filter_phone
            }
            subscribers_list = utils.data_filter_other(filter_form_data,Subscribes)
    
            if filter_form_data:
                request.session['subscriber_filter_data']=filter_form_data   
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            status = request.POST.get('status')
            unsubscribe = request.POST.get('unsubscribe')
            if name or email or phone or status or unsubscribe:
                subscribe_form=forms.SubscribeForm(request.POST)
                if subscribe_form.is_valid():
                    subscriber_obj = subscribe_form.save(commit=False)
                    subscriber_obj.user_id = request.user
                    subscriber_obj.save()
                    messages.success(request,'Subscriber Add successfully')
                else:
                    messages.warning(request,'Somting Want Wrong')
    

    else:
        if 'subscriber_filter_data' in list(request.session.keys()) and 'page' in list(request.GET.keys()):
            session_data = request.session.get('subscriber_filter_data')
            subscribers_list = utils.data_filter_other(session_data,Subscribes)
            filter_form_data=request.session.get('subscriber_filter_data')
        else:
            if 'subscriber_filter_data' in list(request.session.keys()):
                del request.session['subscriber_filter_data']

        
    if subscribers_list:
        paginator = Paginator(subscribers_list, utils.nodes_per_page()) 
        subscribers_list=paginator.get_page(request.GET.get('page'))
    

    if request.user.has_perm('subscribe.add_subscribes'):
        add_edit_view=True

    context={
        "subscribe_form":subscribe_form,
        "subscribers":subscribers_list,
        "form_data":filter_form_data,
        "page_title":"Subscribers",
        "add_edit_view":add_edit_view,
        "edit":False
    }
    
    return render(request, template_name, context)

@login_required(login_url='dashboard:login')
@permission_required({'subscribe.view_subscribes','subscribe.change_subscribes'},raise_exception=True)
def edit_subscribe(request,id):
    template_name = "subscribe/subscribe.html"
    add_edit_view = False
    subscriber = get_object_or_404(Subscribes,id=id)
    
    if request.method == 'POST':
        subscribe_form = forms.SubscribeForm(request.POST,instance=subscriber)
      
        if subscribe_form.is_valid():
            subscriber_obj = subscribe_form.save(commit=False)
            subscriber_obj.user_id = request.user
            subscriber_obj.save()
            messages.success(request,'Subscriber update successfully')
            return redirect("dashboard:subscribe:subscribers")
        else:
            messages.warning(request,'Somting Want Wrong')
      

    if request.user.has_perm('subscribe.change_subscribes'):
        add_edit_view=True
    context={
        "subscribe_form":forms.SubscribeForm(instance=subscriber),
        "subscribers":Subscribes.objects.all(),
        "page_title":"Edit Subscriber",
        "edit":True,
        "add_edit_view":add_edit_view,
    }
    return render(request, template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'subscribe.view_subscribes','subscribe.delete_subscribes'},raise_exception=True)
def delete_subscriber(request,id):
    subscriber = get_object_or_404(Subscribes,id=id)
    if subscriber:
        subscriber.delete()
        messages.success(request,'Subscriber deleted successfully')
    else:
        messages.warning(request,'Subscriber Not Valid')
    return redirect("dashboard:subscribe:subscribers")
        
@login_required(login_url='dashboard:login')
@permission_required({'subscribe.view_subscribes','subscribe.add_subscribes'}, raise_exception=True)
def add_subscriber(request):
    if request.method == "POST":
        email = request.POST.get('dzEmail')
        if not Subscribes.objects.filter(email=email).exists():
            subscriber = Subscribes(email=email)
            subscriber.save()
            return JsonResponse({"message": 'Successfully Added'}, status=200)
        else:
            return JsonResponse({"message": 'You are already subscribed'}, status=200)

    else:
        return JsonResponse({"error": "Somthing went wrong."}, status=400)
