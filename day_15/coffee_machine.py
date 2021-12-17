import machine_resources


def take_money():
    """This function gives the amount user paid to the machine."""
    print("Please insert money.")
    hundreds = int(input("How many hundreds? Rs. "))
    tens = int(input("How many tens? Rs. "))
    rupees = int(input("How many rupees? Rs. "))
    total_price_given = hundreds+tens+rupees
    return total_price_given


def check_resources(waters, coffees, milks, order):
    """This function checks the resources available in the machine."""
    if waters >= machine_resources.MENU[order]["ingredients"]["water"]:
        if coffees >= machine_resources.MENU[order]["ingredients"]["coffee"]:
            if milks >= machine_resources.MENU[order]["ingredients"]["milk"]:
                return True
            else:
                print("Sorry, there is not enough milk.")
                return False
        else:
            print("Sorry, there is not enough coffee.")
            return False
    else:
        print("Sorry, there is not enough water.")
        return False


def return_change(total_cost, actual_cost):
    """This function returns the change remaining."""
    return total_cost-actual_cost


def execute_order(orders):
    """This function take user order and gives the item by executing order."""
    order_money = int(take_money())
    actual_cost = machine_resources.MENU[orders]["cost"]
    if order_money >= actual_cost:
        global money, water, coffee, milk
        money += actual_cost
        water -= machine_resources.MENU[orders]["ingredients"]["water"]
        coffee -= machine_resources.MENU[orders]["ingredients"]["coffee"]
        milk -= machine_resources.MENU[orders]["ingredients"]["milk"]
        print(f"Here is your {orders}, Please enjoy!")
        change_left = return_change(order_money, actual_cost)
        print(f"Here is Rs.{change_left} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded.")


def coffee_machine():
    order = input("What would you like? (espresso/latte/cappuccino):").lower()

    if order == "report":
        print("water : " + str(water))
        print("milk : " + str(milk))
        print("coffee : " + str(coffee))
        print("money : "+str(money))
        coffee_machine()
    elif order == "stop":
        exit()
    else:
        while check_resources(water, coffee, milk, order):
            execute_order(order)
            coffee_machine()


money = 0
water = machine_resources.resources["water"]
milk = machine_resources.resources["milk"]
coffee = machine_resources.resources["coffee"]
coffee_machine()
