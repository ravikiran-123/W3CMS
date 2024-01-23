from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from dashboard.cms.reels.models import Video
from dashboard.cms.reels.forms import  VideoForm
from dashboard.cms.pages.models import Page
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from dashboard.cms import utils

import json




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm

@login_required(login_url='dashboard:login')
def reel_list(request):
    template_name = 'reel_list.html'
    reel_list = Video.objects.all()
    context = {
        "reels": reel_list,
        "page_title": "Reels"
    }
    return render(request, template_name, context)

@login_required(login_url='dashboard:login')
def reel_create(request):
    template_name = 'reel_create.html'
    if request.method == 'POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:reels:reel_list')
    else:
        form=VideoForm()
    return render(request, template_name,{'form':form})

@login_required(login_url='dashboard:login')
def reel_edit(request, id):
    template_name = 'reel_edit.html'

    try:
        # Step 1: Retrieve the existing Video object
        reel_obj = Video.objects.get(id=id)

        if request.method == 'POST':
            # Step 2: Use the VideoForm to handle the form data (including files)
            form = VideoForm(request.POST, request.FILES, instance=reel_obj)

            if form.is_valid():
                # Step 3: Save the updated Video object
                form.save()
                return redirect('dashboard:reels:reel_list')
        else:
            # Step 4: Render the form for editing
            form = VideoForm(instance=reel_obj)

        return render(request, template_name, {'form': form, 'reel_obj': reel_obj})
    except Video.DoesNotExist:
        # Handle the case where the specified Video object does not exist
        return HttpResponse('Video not found', status=404)


@login_required(login_url='dashboard:login')
def reel_delete(request, id):
    reel = Video.objects.get(id=id)
    if reel:
        reel.delete()
    return redirect('dashboard:reels:reel_list')
