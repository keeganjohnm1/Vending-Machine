from config import coin_config

# def implement_count_dict():
#     customer_count_dict = {}
#     for item in coin_config.coins_available:
#         customer_count_dict[item] = 0
#     return customer_count_dict


def users_current_count(product_selected):
    valid_curr_count = 0
    invalid_curr_count = 0
    curr_count_dict = {
        "valid": 0,
        "invalid": 0
    }
    valid_curr_count
    product_dispensed = False
    while not product_dispensed:
        if product_selected:
            print("INSERT COINS")
        customer_input = input(
            "Please enter your coin choice from options below: \n\t"
            "1: Penny\n\t"
            "5: Nickel\n\t"
            "10: Dime \n\t"
            "25: Quarter\n\t"
        )
        customer_input.lower()
        # curr_count = implement_count_dict()
        if len(customer_input) == 5:
            invalid_curr_count += coin_config.coins_available.get(customer_input)
            curr_count_dict['invalid'] = invalid_curr_count
        if len(customer_input) == 6:
            valid_curr_count += coin_config.coins_available.get(customer_input)
            curr_count_dict['valid'] +=valid_curr_count
        if len(customer_input) == 4:
            valid_curr_count += coin_config.coins_available.get(customer_input)
            curr_count_dict['valid'] +=valid_curr_count
        if len(customer_input) == 7:
            valid_curr_count += coin_config.coins_available.get(customer_input)
            curr_count_dict['valid'] +=valid_curr_count
        #keep track of valid count and invalid count
    return curr_count_dict
