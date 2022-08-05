import unittest
from unittest import mock

from application import main


class TestProducts(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = main.sum_helper(data)
        self.assertEqual(result, 6)

    def test_product_values(self):
        get_coke_cost = main.product_cost("Cola")
        get_chip_cost = main.product_cost("Chips")
        self.assertEqual(get_coke_cost, 0.50)
        self.assertEqual(get_chip_cost, 0.75)


    @mock.patch('application.main.display_product_cost', return_value = "Fake Chips")
    def test_user_selects_product(self, mock_product_cost):
        actual_result = main.display_product_cost()
        expected_result = "Fake Chips"
        self.assertEqual(expected_result, actual_result)

    @mock.patch('application.main.user_selection_response', return_value = "THANKS")
    def test_user_selection_returns_thankyou(self, mock_product_cost_for_display):
        actual_response = main.user_selection_response()
        expected_response = "THANKS"
        self.assertEqual(expected_response,actual_response)






if __name__ == '__main__':
    unittest.main()
