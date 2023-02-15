from check_limits_test_functions import TestBattery

test_object = TestBattery()

test_object.test_battery_is_ok_status_all_attributes_normal(25, 70, 0.7)
test_object.test_battery_is_ok_temperature_status_high(50, 70, 0.7)
test_object.test_battery_is_ok_temperature_status_low(-1, 70, 0.7)
test_object.test_battery_is_ok_soc_status_high(25, 85, 0.7)
test_object.test_battery_is_ok_soc_status_low(25, 10, 0.7)
test_object.test_battery_is_ok_charge_rate_status_high(25, 70, 90)
test_object.test_battery_is_ok_charge_rate_status_low(25, 70, -0.1)
