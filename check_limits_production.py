name_mappings = {
    'temperature': 'Temperature',
    'soc': 'State of Charge', 
    'charge_rate': 'Charge rate'
}

def battery_is_ok(temperature, soc, charge_rate):
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
    
    for attribute, (lower_limit, upper_limit) in attribute_ranges.items():
        if (eval(attribute) < lower_limit):
            attribute_status[attribute] = 'low'
            # print(f'{attribute} is low!')
        elif (eval(attribute) > upper_limit):
            attribute_status[attribute] = 'high'
            # print(f'{attribute} is high!')
    battery_info(attribute_status)
    return attribute_status
    
def battery_info(attribute_status):
    print("-----------------------------------")
    for attribute, status in attribute_status.items():
        print(f'{name_mappings[attribute]} is {status}!')
    print("-----------------------------------")
