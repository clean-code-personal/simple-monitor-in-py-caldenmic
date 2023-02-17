import unittest
from check_limits_production import Battery

class TestBattery(unittest.TestCase):

    def assertHigh(self, battery, attribute):
        status = battery.get_attribute_satatus()
        if attribute in status.keys():
            self.assertEqual(status[attribute], 'high')

    def assertLow(self, battery, attribute):
        status = battery.get_attribute_satatus()
        if attribute in status.keys():
            self.assertEqual(status[attribute], 'low')

    def test_battery_is_okay(self):
        battery = Battery(40, 30, 0.7)
        self.assertTrue(battery.is_battery_okay())

    def test_battery_is_not_okay(self):
        param_list = [(50, 30, 0.7), (30, 90, 0.5), (30, 50, 0.95), (50, 90, 0.7), (50, 30, 0.90), (40, 90, 0.98), (50, 90, 0.94)]
        
        for (temperature, soc, charge_rate) in param_list:
            battery = Battery(temperature, soc, charge_rate)
            self.assertFalse(battery.is_battery_okay())

    def test_to_check_number_of_abnormalitites(self):
        param_list_abnormality_number = [(50, 30, 0.7, 1), (30, 90, 0.5, 1), (30, 50, 0.95, 1), (50, 90, 0.7, 2), 
        (50, 30, 0.90, 2), (40, 90, 0.98, 2), (50, 90, 0.94, 3)]

        for (temperature, soc, charge_rate, expected_abnormality_number) in param_list_abnormality_number:
            battery = Battery(temperature, soc, charge_rate)
            self.assertEqual(battery.number_of_abnormalities(), expected_abnormality_number)

    def test_battery_attribute_status(self):
        param_list = [((-10, 50, 0.5), {'temperature': 'low'}), ((50, 50, 0.5), {'temperature': 'high'}), ((25, 10, 0.5), {'soc': 'low'}), 
        ((25, 90, 0.5), {'soc': 'high'}), ((25, 50, -0.5), {'charge_rate': 'low'}), ((25, 50, 1.0), {'charge_rate': 'high'}), 
        ((-10, 90, 0.7), {'temperature': 'low', 'soc': 'high'}), ((90, 14, -0.1), {'temperature': 'high', 'soc': 'low', 'charge_rate': 'low'}), 
        ((65, 45, 0.98), {'temperature': 'high', 'charge_rate': 'high'})]

        for ((temperature, soc, charge_rate), expected_attribute_status) in param_list:
            battery = Battery(temperature, soc, charge_rate)
            status = battery.get_attribute_satatus()
            self.assertEqual(status, expected_attribute_status)

if __name__ == '__main__':
    unittest.main()
