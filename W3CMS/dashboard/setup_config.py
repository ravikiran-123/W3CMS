from dashboard.models import Configurations
import pickle
from django.core import serializers
from django.conf import settings
import json
import os

base_dir = settings.BASE_DIR
filepath = os.path.join(base_dir,'configurations/Config')

def updateConfig():
    # initializing data to be stored in db
    configdata = {}
    items = {}
    for conf in Configurations.objects.all():
        serialized_obj = serializers.serialize('json', [ conf, ])
        json_data = json.loads(serialized_obj)[0]
        name = json_data.get('fields').get('name')
        fields = json_data.get('fields')
        if '.' in name:
            splited_name = name.split('.')
            prefix = splited_name[0]
            if prefix in configdata.keys():
                configdata[prefix].update({f"{splited_name[1]}":fields})
            else:
                configdata.update({f"{prefix}":{f"{splited_name[1]}":fields}})
        else:
            configdata.update({f"{name}":fields})
            
    objfile = open(filepath, 'wb')
    # source, destination
    pickle.dump(configdata, objfile)
    print("Data Update Successfully")
    objfile.close()

def loadConfig():
    dbfile = open(filepath, 'rb')
    config_data = pickle.load(dbfile)
    dbfile.close()
    return config_data
