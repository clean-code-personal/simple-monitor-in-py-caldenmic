from check_limits_production import name_mappings

def battery_reporter(attribute_status, abnormality):
    if not abnormality:
        print("-------------------------------------------")
        print("Battery is working under optimal conditions")
        print("-------------------------------------------")
    else:
        print("-------------------------------------------")
        for attribute, status in attribute_status.items():
            print(f'{name_mappings[attribute]} is {status}!')
        print("-------------------------------------------")
