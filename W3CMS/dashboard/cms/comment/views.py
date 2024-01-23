from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from dashboard.cms.comment.models import Comment
from dashboard.cms.comment.forms import  BlogCommentForm
from dashboard.cms.pages.models import Page
from django.http import JsonResponse
from django.core.paginator import Paginator
from dashboard.cms import utils
from dashboard.cms.menu.menu_config import ScreenOption
from django.contrib.auth.decorators import login_required, permission_required 

import json

type_dict = {
    #"Page":"Page",
    #"Blog":"Blog",
}

@login_required(login_url='dashboard:login')
@permission_required({'comment.view_comment'}, raise_exception=True)
def cms_comment_list(request):
    template_name = 'comment/comments.html'
    message=''
    filter_comment_form_data=None
    comment_list = Comment.objects.all()
    comment_form = BlogCommentForm()
    status=[
        {"label":"Select Status","value":""},
        {"label":"Pending","value":"pending"},
        {"label":"Approved","value":"approved"},
        {"label":"Spam","value":"spam"},
        {"label":"Trash","value":"trash"}
        ]
    if request.method == "POST":
        filter_comment_name = request.POST.get('filter-comment-name')
        filter_comment_email = request.POST.get('filter-comment-email')
        filter_comment_status = request.POST.get('filter-comment-status')
        print('comment_title: ',filter_comment_name)
        print('comment_email: ',filter_comment_email)
        print('comment_status: ',filter_comment_status)
        
        if filter_comment_name or filter_comment_email or filter_comment_status:
            comment_form = BlogCommentForm()
            filter_comment_form_data = {
                "filter_comment_name":filter_comment_name,
                "filter_comment_email":filter_comment_email,
                "filter_comment_status":filter_comment_status
            }
            comment_list = utils.data_filter_comment(filter_comment_form_data,Comment)
            if filter_comment_form_data:
                request.session['comment_filter_data']=filter_comment_form_data   
    else:
        if 'comment_filter_data' in list(request.session.keys()) and 'page' in list(request.GET.keys()):
            session_data = request.session.get('comment_filter_data')
            comment_list = utils.data_filter_comment(session_data,Comment)
            filter_comment_form_data=request.session.get('comment_filter_data')
        else:
            if 'comment_filter_data' in list(request.session.keys()):
                del request.session['comment_filter_data']
            
    if comment_list:
        paginator = Paginator(comment_list, utils.nodes_per_page()) 
        comment_list=paginator.get_page(request.GET.get('page'))
    else:
        message='Data Not Found'

    context={
        "comments": comment_list,
        'message':message,
        "status":status,
        "form_data":filter_comment_form_data,
        "page_title":"Comment",
        "comment_form":comment_form,
    }
    return render(request, template_name, context)


@login_required(login_url='dashboard:login')
@permission_required({'comment.view_comment','comment.change_comment'}, raise_exception=True)
def blogCommentEdit(request,id):
    template_name = 'comment/comment-edit.html'
    comment_obj = get_object_or_404(Comment,id=id)

    if request.method == "POST":
        comment_form = BlogCommentForm(request.POST,instance=comment_obj)
    
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request,"Comment Update Successfully")
            return redirect(request.path)
        else:
            messages.warning(request, comment_form.errors)
    
    else:
        comment_form = BlogCommentForm(instance=comment_obj)
        

    context={
        "page_title":"Edit Comment",
        "comment_form":comment_form,
        "edit":True
    }
    return render(request, template_name,context)

@login_required(login_url='dashboard:login')
@permission_required({'comment.view_comment','comment.delete_comment'}, raise_exception=True)
def blogCommentDelete(request,id):
    comment_obj = Comment.objects.get(id=id)
    
    if comment_obj:
        comment_obj.delete()
        messages.success(request,'Comment Deleted Successfully')
    else:
        messages.warning(request,'Comment Not Valid')
    return redirect("dashboard:comment:comments")

@login_required(login_url='dashboard:login')
@permission_required({'comment.view_comment','comment.delete_comment'}, raise_exception=True)
def delete_multiple_comments(request):
    if request.method=='POST':
        id_list=request.POST.getlist('ids[]')
        id_list = [i for i in id_list if i != '']
        for id in id_list:
            comment_obj = Comment.objects.get(id=id)
            if comment_obj:
                comment_obj.delete()
                response = JsonResponse({"success": 'Comment deleted successfully'})
            else:
                response = JsonResponse({"warning": f'Id {id} is not valid'})

    
    return response