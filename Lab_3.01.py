'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''
# dice roll
"""
import random

# asking user to roll a dice
roll_prompt = input("Type enter to roll the dice. ")
if roll_prompt == '':
    roll = random.randint(1, 6)

# displays what number the user rolled
    print(f"You rolled a {roll}.")
"""
# magic 8 ball
""" 
import random

# choices for magic 8 ball 
ball_choices = random.choice(['Outlook is good', 'Ask again later', 'Yes', 'No', 
'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good'])

#prompt user to ask a question
ball_prompt = input("Ask the magic 8 ball a yes/no question. ")

# displays one of the choices
print(ball_choices) 
"""