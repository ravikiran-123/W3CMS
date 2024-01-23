from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from dashboard.cms.sliders.models import Slider
from dashboard.cms.sliders.forms import  SliderForm
from dashboard.cms.pages.models import Page
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from dashboard.cms import utils

import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Slider
from .forms import SliderForm

@login_required(login_url='dashboard:login')
def slider_list(request):
    template_name = 'slider_list.html'
    slider_list = Slider.objects.all()
    context = {
        "sliders": slider_list,
        "page_title": "Sliders"
    }
    return render(request, template_name, context)

@login_required(login_url='dashboard:login')
def slider_create(request):
    template_name = 'slider_create.html'
    if request.method == 'POST':
        form=SliderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:sliders:slider_list')
    else:
        form=SliderForm()
    return render(request, template_name,{'form':form})

@login_required(login_url='dashboard:login')
def slider_edit(request, id):
    template_name = 'slider_edit.html'

    try:
        # Step 1: Retrieve the existing Video object
        slider_obj = Slider.objects.get(id=id)

        if request.method == 'POST':
            # Step 2: Use the VideoForm to handle the form data (including files)
            form = SliderForm(request.POST, request.FILES, instance=slider_obj)

            if form.is_valid():
                # Step 3: Save the updated Video object
                form.save()
                return redirect('dashboard:sliders:slider_list')
        else:
            # Step 4: Render the form for editing
            form = SliderForm(instance=slider_obj)

        return render(request, template_name, {'form': form, 'slider_obj': slider_obj})
    except Slider.DoesNotExist:
        # Handle the case where the specified Video object does not exist
        return HttpResponse('Image not found', status=404)


@login_required(login_url='dashboard:login')
def slider_delete(request, id):
    slider = Slider.objects.get(id=id)
    if slider:
        slider.delete()
    return redirect('dashboard:sliders:slider_list')
