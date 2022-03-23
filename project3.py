# oregon trail game

# introduction to game
print("Welcome to the Oregon Trail! \n"
"You are in Independence, Missouri, and you have 500 pounds of food and 5 health. \n"
"It is 03/01. You must travel 2000 miles to Oregon by 12/31. \n")

# asks for name
name = input("What is your name? ")
print(f"{name}, in this game, you can travel, hunt, rest, show your status, list these commands, or quit out of the game. \n")
import random

# variables
player_health = 5
food_pounds = 500
miles_to_go = 2000
current_day = 1
current_month = 3

# functions
def add_day():
    global current_day
    global current_month
    months_31_days = [3, 5, 7, 8, 10, 12]
    if current_day > 30 and current_month / 2 != str:
        current_day -= 30
        current_month += 1
    elif current_day > 31:
        current_day -= 31
        if current_month == months_31_days[0] or current_month == months_31_days[1] \
            or current_month[2] or current_month[3] or current_month[4] or current_month[5]:
            current_month += 1

def select_action():
    pass

# gameplay
while True:
    if miles_to_go <= 0:
        print("Congratulations! You made it to Oregon!")
        break
    elif player_health == 0:
        print("Oh no! You ran out of health and died!")
        break
    elif current_month > 12:
        print("Oh no! You didn't make it to Oregon on time!")
        break
    else:
        pass

    action = input(f"What would you like to do, {name}? ")
    if action == 'travel':
       # miles_to_go -= random.randint(30, 61)
        current_day += random.randint(3, 8)
        add_day()
        print(f"You have {miles_to_go} miles left, and this is day {current_day} of month {current_month}. \n")
    elif action == 'status':
        print(f"Your health: {player_health}. \n"
        f"Your food supply: {food_pounds}. \n"
        f"Miles travelled: {2000 - miles_to_go}. \n"
        f"Current day: {current_day}. \n")
    elif action == 'help':
        print("{name}, in this game, you can travel, hunt, rest, show your status, list these commands, or quit out of the game. \n")
    elif action == 'quit':
        print("See you later!")
        break
    
    
    
    
    
