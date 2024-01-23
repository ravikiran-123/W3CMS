from dz import dz_array
from dashboard import setup_config


'''
A context processor is a function that accepts an argument and returns a dictionary as its output.
In our case, the returning dictionary is added as the context and the biggest advantage is that,
it can be accessed globally i.e, across all templates. 
'''

def dz_static(request):
    # we can send data as {"dz_array":dz_array} than you get all dict, using <h1>{{ dz_array }}</h1>
    return {
        "dz_array":dz_array
        }

def site_config(request):
    return {
        "site_config":setup_config.loadConfig()
    }


