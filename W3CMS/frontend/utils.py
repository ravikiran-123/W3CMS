from dashboard import setup_config

def nodes_per_page():
    load_config_data = setup_config.loadConfig()
    nodes_per_page =  int(load_config_data['Reading']['nodes_per_page']['value'])
    return nodes_per_page

month_name={
    "1":"January",
    "2":"February",
    "3":"March",
    "4":"April",
    "5":"May",
    "6":"June",
    "7":"July",
    "8":"August",
    "9":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}

