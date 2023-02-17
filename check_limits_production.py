class Reporter:
    def __init__(self, attribute_status):
        self.attribute_status = attribute_status
        self.name_mappings = {'temperature': 'Temperature', 'soc': 'State of Charge', 'charge_rate': 'Charge Rate'}

    def abnormality_report(self):
        if not any(self.attribute_status):
            self.print_report_in_english()
            return
        for attribute, abnormality_type in self.attribute_status.items():
            self.print_report_in_english(attribute, abnormality_type)

    def print_report_in_english(self, attribute = None, abnormality_type = None):
        if not attribute and not abnormality_type:
            print("Battery working under optimal conditions!")
        else:
            print(f'{self.name_mappings[attribute]} is {abnormality_type}')

class Battery:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = temperature
        self.soc = soc
        self.charge_rate = charge_rate
        self.attribute_ranges = {'temperature': (0, 45), 'soc': (20, 80), 'charge_rate': (0, 0.8)}
        self.attribute_status = {}

    def update_attribute_status(self):
        for attribute, (lower_limit, upper_limit) in self.attribute_ranges.items():
            if (eval('self.' + attribute) < lower_limit):
                self.attribute_status[attribute] = 'low'
            elif (eval('self.' +attribute) > upper_limit):
                self.attribute_status[attribute] = 'high'
    
    def is_battery_okay(self):
        self.update_attribute_status()
        
        # self.display_abnormality_report()
        if not any(self.attribute_status):
            return True
        return False

    def number_of_abnormalities(self):
        self.update_attribute_status()
        return len(self.attribute_status)

    def print_battery_status(self):
        print(self.attribute_status)

    def display_abnormality_report(self):
        reporter = Reporter(self.attribute_status)
        reporter.abnormality_report()

    def get_attribute_satatus(self):
        self.update_attribute_status()
        return self.attribute_status
