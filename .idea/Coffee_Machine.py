water_available = 400
milk_available = 540
beans_available = 120
cups_available = 9
money_available = 550

def buy_espresso():

    global water_available, milk_available, beans_available, cups_available, money_available

    if water_available <= 250:
        print("Sorry, not enough water!")
        if beans_available <= 16:
            print("Sorry, not enough beans!")
    else:
        water_available = water_available - 250
        milk_available = milk_available
        beans_available = beans_available - 16
        cups_available = cups_available - 1
        money_available = money_available + 4
        print("I have enough resources, making you a coffee!")

def buy_latte():

    global water_available, milk_available, beans_available, cups_available, money_available

    if water_available <= 350:
        print("Sorry, not enough water!")
        if milk_available <= 75:
            print("Sorry, not enough milk!")
            if beans_available <= 20:
                print("Sorry, not enough beans!")
    else:
        water_available = water_available - 350
        milk_available = milk_available - 75
        beans_available = beans_available - 20
        cups_available = cups_available - 1
        money_available = money_available + 7
        print("I have enough resources, making you a coffee!")

def buy_cappuccino():

    global water_available, milk_available, beans_available, cups_available, money_available

    if water_available <= 200:
        print("Sorry, not enough water!")
        if milk_available <= 100:
            print("Sorry, not enough milk!")
            if beans_available <= 12:
                print("Sorry, not enough beans!")
    else:
        water_available = water_available - 200
        milk_available = milk_available - 100
        beans_available = beans_available - 12
        cups_available = cups_available - 1
        money_available = money_available + 6
        print("I have enough resources, making you a coffee!")

def buy():

    global cups_available

    drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

    if drink == "back":
        return
    elif cups_available >= 1:
        if drink == "1":
            buy_espresso()
        elif drink == "2":
            buy_latte()
        elif drink == "3":
            buy_cappuccino()

def fill():

    global water_available, milk_available, beans_available, cups_available

    print("Write how many ml of water do you want to add:")
    add_water = int(input())
    print("Write how many ml of milk do you want to add:")
    add_milk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    add_beans = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    add_cups = int(input())

    water_available = water_available + add_water
    milk_available = milk_available + add_milk
    beans_available = beans_available + add_beans
    cups_available = cups_available + add_cups

def take():

    global money_available

    print("I gave you $" + str(money_available))

    money_available = money_available - money_available

def remaining():

    print("The coffee machine has:")
    print(str(water_available) + " of water")
    print(str(milk_available) + " of milk")
    print(str(beans_available) + " of coffee beans")
    print(str(cups_available) + " of disposable cups")
    print(str(money_available) + " of money")

def main_menu():

    pointer = True

    while pointer == True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            print("")
            buy()
            print("")
            pointer = True
        elif action == "fill":
            print("")
            fill()
            print("")
            pointer = True
        elif action == "take":
            print("")
            take()
            print("")
            pointer = True
        elif action == "remaining":
            print("")
            remaining()
            print("")
            pointer = True
        else:
            None
            pointer = False

main_menu()