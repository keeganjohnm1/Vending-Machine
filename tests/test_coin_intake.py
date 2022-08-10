import unittest
from unittest import mock
from coin_processing import coin_intake

class Test(unittest.TestCase):
    # @mock.patch('coin_processing.coin_intake.users_current_count', return_value=1)
    def test_users_current_count(self):
        user_input = 1
        user_count = coin_intake.users_current_count(user_input)
        expected_valid_count = 0
        expected_invalid_count = 0
        actual_valid_count = 0
        actual_invalid_count =0
        #user selects item
        ##user is directed to input coin
        #user inputs coins until item is paid for
        ##item cost needs to be mapped from product_config
        self.assertEqual(expected_valid_count, actual_valid_count)
        self.assertEqual(expected_invalid_count, actual_invalid_count)
