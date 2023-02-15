from check_limits_test_functions import TestBattery

test_object = TestBattery()

test_object.test_battery_is_ok_True(25, 70, 0.7)
test_object.test_battery_is_ok_False(50, 85, 0)
test_object.test_charge_rate_between_0_and_1(0.1)
