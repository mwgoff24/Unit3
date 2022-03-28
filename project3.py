# oregon trail game
import random

# introduction to game
print("Welcome to the Oregon Trail! \n"
"You are in Independence, Missouri, and you have 500 pounds of food and 5 health. \n"
"It is March 1. You must travel 2000 miles to Oregon by December 31. \n")

# asks for name
name = input("What is your name? ")
print(f"{name}, in this game, you can either travel, hunt, rest, show your status, ask for help, or quit out of the game. \n")

# global variables
MONTHS = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
player_health = 5
food_pounds = 500
miles_to_go = 2000
current_day = 1
current_month = 3

# function defs
def add_day(days):
    global current_day, current_month, food_pounds, player_health
    months_31_days = [3, 5, 7, 8, 10, 12]
    current_day += days
    food_pounds -= days * 5
    if current_day > 30 and current_month / 2 != str:
        current_day -= 30
        current_month += 1
        player_health -= 2 # couldn't figure out an efficient way to make a player's health decrease
        if player_health <= -1:
            player_health = 0
    elif current_day > 31:
        current_day -= 31
        if current_month in months_31_days:
            current_month += 1
            player_health -= 2 # this also interferes with rest() if one rests at the end of a month, and I can't figure out a workaround
            if player_health <=-1:
                player_health = 0

def travel():
    global miles_to_go, current_day, food_pounds, player_health
    miles_to_go -= random.randint(30, 61)
    days_travelled = random.randint(3, 8)
    add_day(days_travelled)
    if miles_to_go < 0:
        miles_to_go = 0
    elif food_pounds < 0:
        food_pounds = 0
    print(f"You have {miles_to_go} miles left. Today is {MONTHS[current_month]} {current_day}. You have {food_pounds} pounds of food left. Your health is at {player_health}. \n")

def hunt():
    global food_pounds
    days_hunted = random.randint(2, 6)
    add_day(days_hunted)
    food_pounds += 100
    print(f"Nice! You now have 100 more pounds of food. It is now {MONTHS[current_month]} {current_day}. \n")

def rest():
    global player_health
    days_rested = random.randint(2, 6)
    add_day(days_rested)
    player_health += 1
    print(f"Your health is now at {player_health}.")
    if player_health > 5:
        print(f"What are you resting for, you lazy person? It is now {MONTHS[current_month]} {current_day}! You're wasting time! \n")
        player_health -=1

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
    elif food_pounds == 0:
        print("Oops! You ran out of food!")
        break
    else:
        pass

    action = input(f"What would you like to do, {name}? ")
    if action == 'travel':
        travel()
    elif action == 'hunt':
        hunt()
    elif action == 'rest':
        rest()
    elif action == 'status':
        status()
    elif action == 'quit':
        quit()
        break
    elif action == 'help':
        help()
    else:
        print("That's not a function. In this game, you can either travel, hunt, rest, show your status, ask for help, or quit out of the game. \n")