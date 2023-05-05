MENU = {
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


def coins():
    print("Please insert coins")
    q = float(input("How many quarters?:"))
    d = float(input("How many dimes?:"))
    n = float(input("How many nickles?:"))
    p = float(input("How many pennies?:"))
    return 0.25*q+0.1*d+0.05*n+0.01*p


resp = 0
money = 0
global moeda

while resp != "off":
    resp = input("What would you like? (espresso/latte/cappuccino):")
    if resp == "espresso":
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            moeda = coins()
            if moeda >= MENU["espresso"]['cost']:
                resources['water'] -= 50
                resources['coffee'] -= 18
                money = money + (moeda - MENU["espresso"]['cost'])
                print("Here is your espresso")
                # print(moeda)
                # print(money)
                # print(resources)
                    
                if moeda > MENU["espresso"]['cost']:
                    print("Here is your change: ", round(moeda - MENU["espresso"]['cost'],2))
            elif moeda < MENU["espresso"]['cost']:
                print("Sorry that's not enough money. Money refunded.")

        elif resources['water'] < 50:
            print("Sorry there is not enough water")
        elif resources['coffee'] < 18:
            print("Sorry there is not enough coffee")

    elif resp == "latte":

        if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            moeda = coins()
            if moeda >= MENU["latte"]['cost']:
                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
                money = money + (moeda - MENU["espresso"]['cost'])
                print("Here is your latte")
                # print(moeda)
                # print(money)
                # print(resources)
                if moeda > MENU["latte"]['cost']:
                    print("Here is your change: ", round(moeda - MENU["latte"]['cost'],2))
            elif moeda < MENU["latte"]['cost']:
                print("Sorry that's not enough money. Money refunded.")
        elif resources['water'] < 200:
            print("Sorry there is not enough water")
        elif resources['milk'] < 150:
            print("Sorry there is not enough milk")
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee")

    elif resp == "cappuccino":

        if resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
            moeda = coins()
            if moeda >= MENU["cappuccino"]['cost']:
                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24
                money = money + (moeda - MENU["cappuccino"]['cost'])
                print("Here is your cappuccino")
                # print(moeda)
                # print(money)
                # print(resources)
                if moeda > MENU["cappuccino"]['cost']:
                    print("Here is your change: ", round(moeda - MENU["cappuccino"]['cost'],2))
            elif moeda < MENU["cappuccino"]['cost']:
                print("Sorry that's not enough money. Money refunded.")
        elif resources['water'] < 250:
            print("Sorry there is not enough water")
        elif resources['milk'] < 100:
            print("Sorry there is not enough milk")
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee")

    elif resp == "report":
        print("Water: ", resources["water"], "Milk: ", resources['milk'], "Coffee: ", resources['coffee'],
              "Money: ", round(money,2))

