name_mappings = {'temperature': 'Temperature','soc': 'State of Charge', 'charge_rate': 'Charge rate'}

def update_status(attribute, lower_limit, upper_limit, abnormality, status):
    if (eval(attribute) < lower_limit):
        attribute_status[attribute] = 'low'
        abnormality = 1
    else (eval(attribute) > upper_limit):
        attribute_status[attribute] = 'high'
        abnormality = 1
        
def battery_is_ok(temperature, soc, charge_rate, reporter=None):
    attribute_ranges = {'temperature': (0, 45), 'soc': (20, 80), 'charge_rate': (0, 0.8)}
    attribute_status = {'temperature': 'normal', 'soc': 'normal', 'charge_rate': 'normal'}
    
    abnormality = 0
    
    for attribute, (lower_limit, upper_limit) in attribute_ranges.items():
        update_status(attribute, lower_limit, upper_limit, abnormality, attribute_status)
        
    reporter(attribute_status, abnormality)
    return attribute_status
