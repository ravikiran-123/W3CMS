from dashboard import setup_config

def nodes_per_page():
    load_config_data = setup_config.loadConfig()
    nodes_per_page =  int(load_config_data['Reading']['nodes_per_page']['value'])
    return nodes_per_page

def data_filter(filter_form_data,model_obj):
    email = filter_form_data.get('filter_email')
    mobile = filter_form_data.get('filter_mobile')
    group = filter_form_data.get('filter_group')

    filter_data=None

    if email:
        if filter_data:
            filter_data = filter_data.filter(email__icontains=email)
        else:
            filter_data = model_obj.objects.filter(email__icontains=email)
    if mobile:
        if filter_data:
            filter_data = filter_data.filter(phone_number__icontains=mobile)
        else:
            filter_data = model_obj.objects.filter(phone_number__icontains=mobile)
    if group:
        if filter_data:
            filter_data = filter_data.filter(groups=group)
        else:
            filter_data = model_obj.objects.filter(groups=group)
    
    return filter_data
