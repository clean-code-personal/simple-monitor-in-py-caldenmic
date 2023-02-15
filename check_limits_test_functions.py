import unittest
from check_limits_production import battery_is_ok
from check_limits_battery_reporter import battery_reporter

class TestBattery(unittest.TestCase):
    def assertion_for_status(self, temperature, soc, charge_rate, attribute, status):
        attribute_status = battery_is_ok(temperature, soc, charge_rate, battery_reporter)
        self.assertEqual(attribute_status[attribute], status)
    def test_battery_is_ok_status_all_attributes_normal(self, temperature, soc, charge_rate):
        attribute_status = battery_is_ok(temperature, soc, charge_rate, battery_reporter)
        for attribute, status in attribute_status.items():
            self.assertEqual(status, 'normal')
    def test_battery_is_ok_temperature_status_high(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'temperature', 'high')
    def test_battery_is_ok_temperature_status_low(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'temperature', 'low')
    def test_battery_is_ok_soc_status_high(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'soc', 'high')
    def test_battery_is_ok_soc_status_low(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'soc', 'low')
    def test_battery_is_ok_charge_rate_status_high(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'charge_rate', 'high')
    def test_battery_is_ok_charge_rate_status_low(self, temperature, soc, charge_rate):
        self.assertion_for_status(temperature, soc, charge_rate, 'charge_rate', 'low')
