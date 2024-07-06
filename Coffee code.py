menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

enough_money = False
enough_resource = False

# This is the money that coffee maker has
money = 0

# this is money inserted by user
user_money = 0


# To check the availablity
def check_avab():
    global enough_resource
    for items in user_resources:
        if user_resources[items] > our_resources[items]:
            print(f"Sorry there is not enough {[items]}")
        else:
            enough_resource = True


# ask user to input the coins
def sumamount():
    global user_money
    quarter = int(input("How many quarters?")) * 0.25;
    dimes = int(input("How many dimes?")) * 0.1;
    nickels = int(input("How many nickels?")) * 0.05;
    pennies = int(input("How many pennies?")) * 0.01;

    user_sum = float(quarter + dimes + nickels + pennies)
    user_money = user_sum
    print(f"You gave {user_money}")

# To validate the user input money
def validate_enough_money():
    global user_money
    global money
    global our_resources
    global user_resources
    global enough_money
    if user_money < menu[user_input]["cost"]:
        print(f"Sorry there is not enough money for a  {[user_input]} ! money will be refunded")
    elif user_money >= menu[user_input]["cost"]:
        return_money = user_money - menu[user_input]["cost"]
        print (f"Your change is {return_money}")
        money += menu[user_input]["cost"]
        enough_money = True
        for item in user_resources:
            our_resources[item] -= user_resources[item]

play_again = True

while play_again:
    # This is to know what user wants
    user_input = input("What would you like? (espresso/latte/cappuccino) :\n").lower()

    # To know what user want and get the ingredients for it
    user_resources = menu[user_input]["ingredients"]
    our_resources = resources

    # To call the avc check function
    check_avab()

    # To call the sum of amount user inputs
    sumamount()

    # To call money validation
    validate_enough_money()

    if enough_resource == True and enough_money == True:
        print(f"Here is your{user_input} Enjoy ☕")
        # Print the report of inventory
        Report = input("Would you like to report this report? (y/n) ").lower()
        if Report in ["y", "yes"]:
            print(f"water :{resources["water"]}")
            print(f"milk :{resources["milk"]}")
            print(f"coffee :{resources["coffee"]}")
            print(money)
        play_again = True