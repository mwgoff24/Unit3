# oregon trail game
import random

# introduction to game
print("Welcome to the Oregon Trail! \n"
"You are in Independence, Missouri, and you have 500 pounds of food and 5 health. \n"
"It is 03/01. You must travel 2000 miles to Oregon by 12/31. \n")

# asks for name
name = input("What is your name? ")
print(f"{name}, in this game, you can travel, hunt, rest, show your status, ask for help, or quit out of the game. \n")

# global variables
MONTHS = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
player_health = 5
food_pounds = 500
miles_to_go = 2000
current_day = 1
current_month = 3

# function defs
def add_day(days):
    global current_day, current_month
    months_31_days = [3, 5, 7, 8, 10, 12]
    current_day += days
    if current_day > 30 and current_month / 2 != str:
        current_day -= 30
        current_month += 1
    elif current_day > 31:
        current_day -= 31
        if current_month in months_31_days:
            current_month += 1

def travel():
    global miles_to_go, current_day
    miles_to_go -= random.randint(30, 61)
    days_travelled = random.randint(3, 8)
    add_day(days_travelled)
    if miles_to_go < 0:
        miles_to_go = 0
    print(f"You have {miles_to_go} miles left. Today is {MONTHS[current_month]} {current_day}. \n")

def hunt():
    global food_pounds
    days_hunted = random.randint(2, 6)
    add_day(days_hunted)
    food += 100
    

def status():
    print(f"Your health: {player_health}. \n"
        f"Your food supply: {food_pounds}. \n"
        f"Miles travelled: {2000 - miles_to_go}. \n"
        f"Current day: {MONTHS[current_month]} {current_day}. \n")

def quit():
    print("See you later!")

def help():
    print("In this game, you can either travel, hunt, rest, show your status, ask for help, or quit out of the game. \n")


def select_action():
    pass

# game loop
while True:
    if miles_to_go <= 0:
        print("Congratulations! You made it to Oregon!")
        break
    elif player_health <= 0:
        print("Oh no! You ran out of health and died!")
        break
    elif current_month > 12:
        print("Oh no! You didn't make it to Oregon on time!")
        break
    else:
        pass

    action = input(f"What would you like to do, {name}? ")
    if action == 'travel':
        travel()
    elif action == 'status':
        status()
    elif action == 'quit':
        quit()
        break
    elif action == 'help':
        help()
    else:
        print("That's not a function. In this game, you can either travel, hunt, rest, show your status, ask for help, or quit out of the game. \n")
    
    
    
    
    
