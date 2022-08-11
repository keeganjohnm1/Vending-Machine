import unittest
from unittest import mock
from coin_processing import coin_intake

class Test(unittest.TestCase):
    @mock.patch('coin_processing.coin_intake.users_current_count', return_value=1)
    def test_users_invalid_current_count(self, mock_current_count):
        expected_invalid_count = 1
        actual_invalid_count = coin_intake.users_current_count()
        self.assertEqual(expected_invalid_count, actual_invalid_count)


    @mock.patch('coin_processing.coin_intake.users_current_count', return_value=5)
    def test_users_valid_current_count(self, mock_current_count):
        expected_valid_count = 5
        actual_valid_count = coin_intake.users_current_count()
        self.assertEqual(expected_valid_count, actual_valid_count)

    def test_user_selects_product(self):
        item_selected = 1 #Cola
        users_total_count = 1.00
        expected_coin_return = 0.0
        actual_coin_return = coin_intake.get_customer_selection(users_total_count, item_selected)
        self.assertEqual(expected_coin_return, actual_coin_return['customer_final_total'])
