def battery_is_ok(temperature, soc, charge_rate):
    attribute_ranges = {'temperature': (0, 45), 'soc': (20, 80), 'charge_rate': (0, 0.8)}
    
    for attribute, (lower_limit, upper_limit) in attribute_ranges.items():
        if not (lower_limit <= eval(attribute) <= upper_limit):
            print(f'{attribute} is out of range!')
            return False
        return True
