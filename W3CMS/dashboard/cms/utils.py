import re
from dashboard import setup_config

def nodes_per_page():
    load_config_data = setup_config.loadConfig()
    nodes_per_page =  int(load_config_data['Reading']['nodes_per_page']['value'])
    return nodes_per_page

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

def data_filter(filter_form_data,model_obj):
    title = filter_form_data.get('filter_title')
    status = filter_form_data.get('filter_status')
    date = filter_form_data.get('filter_date')
    filter_data=None

    if title :
        print("I am in page title")
        if filter_data:
            filter_data = filter_data.filter(title__icontains=title)
        else:
            filter_data = model_obj.objects.filter(title__icontains=title)

    if status:
        print("I am in page status")
        if filter_data:
            print("status on filter_data")
            filter_data = filter_data.filter(status__exact=status)
        else:
            print("new filter_data")
            filter_data = model_obj.objects.filter(status__exact=status)

    if date:
        print("I am in page date")
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]

        if filter_data:
            filter_data = filter_data.filter(publish_on__year=year,publish_on__month=month,publish_on__day=day)
        else:
            filter_data = model_obj.objects.filter(publish_on__year=year,publish_on__month=month,publish_on__day=day)
    
    return filter_data

#Data filter for contactus and Subscribers

def data_filter_other(filter_form_data,model_obj):
    name = filter_form_data.get('filter_name')
    email = filter_form_data.get('filter_email')
    phone = filter_form_data.get('filter_phone')
    filter_data=None

    if name :
        if filter_data:
            filter_data = filter_data.filter(name__icontains=name)
        else:
            filter_data = model_obj.objects.filter(name__icontains=name)

    if email:
        if filter_data:
            filter_data = filter_data.filter(email__icontains=email)
        else:
            filter_data = model_obj.objects.filter(email__icontains=email)

    if phone:
        if filter_data:
            filter_data = filter_data.filter(phone__icontains=phone)
        else:
            filter_data = model_obj.objects.filter(phone__icontains=phone)

    return filter_data

def data_filter_comment(filter_comment_form_data,comment_model_obj):
    comment_name = filter_comment_form_data.get('filter_comment_name')
    comment_email = filter_comment_form_data.get('filter_comment_email')
    comment_status = filter_comment_form_data.get('filter_comment_status')
    filter_comment_data=None

    if comment_name :
        if filter_comment_data:
            filter_comment_data = filter_comment_data.filter(name__icontains=comment_name)
        else:
            filter_comment_data = comment_model_obj.objects.filter(name__icontains=comment_name)

    if comment_email:
        if filter_comment_data:
            filter_comment_data = filter_comment_data.filter(email__icontains=comment_email)
        else:
            filter_comment_data = comment_model_obj.objects.filter(email__icontains=comment_email)

    if comment_status:
        if filter_comment_data:
            filter_comment_data = filter_comment_data.filter(status__icontains=comment_status)
        else:
            filter_comment_data = comment_model_obj.objects.filter(status__icontains=comment_status)

    return filter_comment_data
    