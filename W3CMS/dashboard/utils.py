from dashboard.cms.pages.models import Page
from django.core import serializers
from django.conf import settings
import json
import os
import xml.dom.minidom

base_dir = settings.BASE_DIR
filepath = os.path.join(base_dir,'dashboard/content')

