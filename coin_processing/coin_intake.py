from config import coin_config, product_config
import main

curr_count_dict = {
    "valid": 0,
    "invalid": 0
}

def get_customer_selection(customer_total, product_selected):
    customer_dict = {
        "product_dispensed" : False,
        "customer_final_total": 0
    }
    map_num_selected_to_product = {
        1 : "Cola",
        2 : "Chips",
        3 : "Candy"
    }
    map_selected_product = map_num_selected_to_product.get(product_selected)
    product_cost = round(product_config.products_available.get(map_selected_product), 2)
    if customer_total >= product_cost:
        print("THANK YOU")
        customer_dict['customer_final_total'] = customer_total - product_cost
        customer_dict['product_dispensed'] = True
    elif customer_total < product_cost:
        print(f"{map_selected_product} cost ${product_cost} - you have ${customer_total}")
        users_current_count()
    return customer_dict
def handle_users_selection(total):
    users_product_selection = main.display_product_cost()
    return get_customer_selection(total, users_product_selection)

def users_current_count():
    customer_input_lower = ''
    while True:
        product_selected = False
        if curr_count_dict['valid'] == 0:
            print("INSERT COINS")
        customer_input = input(
            "Please insert coins from options below: \n\t"
            "Penny\n\t"
            "Nickel\n\t"
            "Dime \n\t"
            "Quarter\n\t"
        )
        customer_input_lower = str(customer_input.lower())
        if customer_input_lower not in coin_config.coins_available:
            print("Please enter insert valid coin")
        elif len(customer_input_lower) == 5:
            curr_count_dict['invalid'] += round(coin_config.coins_available.get(customer_input_lower), 2)
            total = handle_users_selection(curr_count_dict['invalid'])
        elif len(customer_input_lower) == 6:
            curr_count_dict['valid'] += round(coin_config.coins_available.get(customer_input_lower), 2)
            total = handle_users_selection(curr_count_dict['valid'])
        elif len(customer_input_lower) == 4:
            curr_count_dict['valid'] += round(coin_config.coins_available.get(customer_input_lower), 2)
            total = handle_users_selection(curr_count_dict['valid'])
        elif len(customer_input_lower) == 7:
            curr_count_dict['valid'] += round(coin_config.coins_available.get(customer_input_lower), 2)
            total = handle_users_selection(curr_count_dict['valid'])
            product_selected = total['product_dispensed']
        if product_selected:
            break
        print("Amount in coin return:", curr_count_dict['invalid'])
    return "Thanks"
