from config import product_config
from coin_processing import coin_intake
def sum_helper(arg):
    total = 0
    for val in arg:
        total += val
    return total

def product_cost(product):
    if product not in product_config.products_available:
        return "Item not available"
    else:
        return product_config.products_available.get(product)

def display_product_cost():
    item_list =["1","2","3"]
    print("Please enter number of product to purchase")
    while True:
        customer_input = input(
            "1: Cola: $1.00 \n"
            "2: Chips: $0.50\n"
            "3: Candy: $0.65 \n"
        )
        if customer_input not in item_list:
            print("please enter valid option")
        else:
            return customer_input
def user_selection_response():
    coin_intake.users_current_count()
    print("THANK YOU")

# def user_selects_item(user_input):

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_selection_response()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
