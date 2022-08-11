from config import coin_config, product_config
from application import main




def get_customer_selection(customer_total, product_selected):
    product_cost = product_config.products_available.get(product_selected)
    if customer_total >= product_cost:
        customer_total = customer_total - product_cost
    elif customer_total < product_cost:
        print('INSERT COINS')
    return customer_total
def handle_users_selection(total):
    users_product_selection = main.user_selection_response()
    return get_customer_selection(total, users_product_selection)

def users_current_count():
    curr_count_dict = {
        "valid": 0,
        "invalid": 0
    }
    product_selected = False
    while not product_selected:
        if curr_count_dict['valid'] == 0:
            print("INSERT COINS")
        customer_input = input(
            "Please enter your coin choice from options below: \n\t"
            "Penny\n\t"
            "Nickel\n\t"
            "Dime \n\t"
            "Quarter\n\t"
        )
        customer_input.lower()
        if customer_input not in coin_config.coins_available:
            print("Please enter insert valid coin")
        if len(customer_input) == 5:
            curr_count_dict['invalid'] = coin_config.coins_available.get(customer_input)
        if len(customer_input) == 6:
            curr_count_dict['valid'] += coin_config.coins_available.get(customer_input)
        if len(customer_input) == 4:
            curr_count_dict['valid'] += coin_config.coins_available.get(customer_input)
        if len(customer_input) == 7:
            curr_count_dict['valid'] += coin_config.coins_available.get(customer_input)
        customers_total = handle_users_selection(curr_count_dict['valid'])
        print("Coin total: ", customers_total)
        print("Amount in coin return:", curr_count_dict['invalid'])
    return curr_count_dict
