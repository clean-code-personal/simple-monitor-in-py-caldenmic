import unittest
from check_limits_production import battery_is_ok

class TestBattery(unittest.TestCase):
    
    def test_battery_is_ok_status_all_attributes_normal(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        for attribute, status in attribute_status.items():
            self.assertEqual(status, 'normal')
    
    def test_battery_is_ok_temperature_status_high(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['temperature'], 'high')
        
    def test_battery_is_ok_temperature_status_low(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['temperature'], 'low')
        
    def test_battery_is_ok_soc_status_high(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['soc'], 'high')
        
    def test_battery_is_ok_soc_status_low(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['soc'], 'low')
        
    def test_battery_is_ok_charge_rate_status_high(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['charge_rate'], 'high')
        
    def test_battery_is_ok_charge_rate_status_low(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate)
        self.assertEqual(attribute_status['charge_rate'], 'low')
