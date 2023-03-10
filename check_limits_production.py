class Reporter:
    def __init__(self, attribute_status):
        self.attribute_status = attribute_status
        self.name_mappings = {'temperature': 'Temperature', 'soc': 'State of Charge', 'charge_rate': 'Charge Rate'}
        self.language_mappings = {
            'en': {'optimal': 'Battery working under optimal conditions!',
                    'low': '{attribute} is too low!',
                    'high': '{attribute} is too high!',
                    'warning high': '{attribute} approaching high conditions!',
                    'warning low': '{attribute} approaching low conditions!'},
            'fr': {'optimal': 'La batterie fonctionne dans des conditions optimales !',
                    'low': '{attribute} est trop bas !',
                    'high': '{attribute} est trop élevé !',
                    'warning high': '{attribute} approche des conditions élevées!',
                    'warning low': '{attribute} approche des conditions basses!'}
        }

    def abnormality_report(self, language='en'):
        if not any(self.attribute_status):
            self.print_report(language = language)
            return
        for attribute, abnormality_type in self.attribute_status.items():
            self.print_report(attribute, abnormality_type, language = language)

    def print_report(self, attribute = None, abnormality_type = None, language='en'):
        if not attribute and not abnormality_type:
            print(self.language_mappings[language]['optimal'])
        else:
            message_template = self.language_mappings[language][abnormality_type]
            message = message_template.format(attribute=self.name_mappings[attribute])
            print(message)

class Battery:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = temperature
        self.soc = soc
        self.charge_rate = charge_rate
        self.attribute_ranges = {'temperature': (0, 45), 'soc': (20, 80), 'charge_rate': (0, 0.8)}
        self.attribute_warning_required = {'temperature': 1, 'soc': 1, 'charge_rate': 1}
        self.attribute_status = {}

    def update_attribute_status(self):
        for attribute, (lower_limit, upper_limit) in self.attribute_ranges.items():
            self.update_single_attribute_status(attribute, upper_limit, lower_limit)

    def update_single_attribute_status(self, attribute, upper_limit, lower_limit):
        attribute_val = eval('self.' + attribute)

        if (attribute_val < lower_limit):
            self.attribute_status[attribute] = 'low'
        elif (attribute_val > upper_limit):
            self.attribute_status[attribute] = 'high'
        else:
            self.check_warning_attribute_status_required(attribute, upper_limit, lower_limit, attribute_val)

    def check_warning_attribute_status_required(self, attribute, upper_limit, lower_limit, attribute_val):
        if self.attribute_warning_required[attribute]:
            self.calculate_warning_attribute_status(attribute, upper_limit, lower_limit, attribute_val)
        else:
            return

    def calculate_warning_attribute_status(self, attribute, upper_limit, lower_limit, attribute_val):
        warning_range = 0.05 * upper_limit
        warning_upper_limit = upper_limit - warning_range
        warning_lower_limit = lower_limit + warning_range

        if (attribute_val >= warning_upper_limit):
            self.attribute_status[attribute] = 'warning high'
        elif (attribute_val <= warning_lower_limit):
            self.attribute_status[attribute] = 'warning low'

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

    def display_abnormality_report(self, language='en'):
        self.update_attribute_status()
        reporter = Reporter(self.attribute_status)
        reporter.abnormality_report(language)

    def get_attribute_satatus(self):
        self.update_attribute_status()
        return self.attribute_status
