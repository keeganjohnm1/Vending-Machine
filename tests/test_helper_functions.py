import unittest
from unittest import mock

import product_helper.helper_functions as helpers

class TestProducts(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = helpers.sum_helper(data)
        self.assertEqual(result, 6)

    def test_product_values(self):
        get_coke_cost = helpers.product_cost("Cola")
        get_chip_cost = helpers.product_cost("Chips")
        self.assertEqual(get_coke_cost, 1.00)
        self.assertEqual(get_chip_cost, 0.50)


    @mock.patch('product_helper.helper_functions.display_product_cost', return_value = "Fake Chips")
    def test_user_selects_product(self, mock_product_cost):
        actual_result = helpers.display_product_cost()
        expected_result = "Fake Chips"
        self.assertEqual(expected_result, actual_result)

    @mock.patch('product_helper.helper_functions.user_selection_response', return_value = "THANKS")
    def test_user_selection_returns_thankyou(self, mock_product_cost_for_display):
        actual_response = helpers.user_selection_response()
        expected_response = "THANKS"
        self.assertEqual(expected_response,actual_response)

if __name__ == '__main__':
    unittest.main()
