import unittest
from check_limits_production import battery_is_ok

class TestBattery(unittest.TestCase):
    
    def test_battery_is_ok_True(self, temperature, soc, charge_rate):
        self.assertTrue(battery_is_ok(temperature, soc, charge_rate))
    
    def test_battery_is_ok_False(self, temperature, soc, charge_rate):
        self.assertFalse(battery_is_ok(temperature, soc, charge_rate))
        
    def test_charge_rate_not_negative(self, charge_rate):
        self.assertTrue(charge_rate !< 0)
