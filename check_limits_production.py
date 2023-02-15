name_mappings = {
    'temperature': 'Temperature',
    'soc': 'State of Charge', 
    'charge_rate': 'Charge rate'
}

def battery_is_ok(temperature, soc, charge_rate, reporter=None):
    attribute_ranges = {
        'temperature': (0, 45), 
        'soc': (20, 80), 
        'charge_rate': (0, 0.8)
    }
    attribute_status = {
        'temperature': 'normal', 
        'soc': 'normal', 
        'charge_rate': 'normal'
    }
    
    abnormality = 0
    
    for attribute, (lower_limit, upper_limit) in attribute_ranges.items():
        if (eval(attribute) < lower_limit):
            attribute_status[attribute] = 'low'
            abnormality = 1
            # print(f'{attribute} is low!')
        elif (eval(attribute) > upper_limit):
            attribute_status[attribute] = 'high'
            abnormality = 1
            # print(f'{attribute} is high!')
    reporter(attribute_status, abnormality)
    return attribute_status
