'''
############
Lab 3.02
############
Lab Exercise 1
--------------
Create a function, birthday_song, that prints out the happy birthday song to whatever name is input as an argument. The contract should be:

  # Name: birthday_song
  # Purpose: birthday_song prints out a personalized birthday song
  # Arguments: name, string
  # Returns: none
  def birthday_song(name):
     #your code goes here

Lab Exercise 2
---------------
Create a function that randomly picks 5 cards from a deck 

The cards can repeat

Write out the contract for this function using the list.

number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Bonus
Practice passing in lists as an argument to a function.

What is different about passing in a list as an argument?

Read about list aliasing in section 3.4 of the associated reading, and write down what is happening in this case.
Remember, the associated reading is in the "SWBAT" section on moodle!
'''
# Lab 1

'''
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Arguments: name, string
# Returns: none
def birthday_song(name):
  print(f"Happy birthday to you! Happy birthday to you! \n"
  f"Happy birthday dear {name}! Happy birthday to you! \n")

username = input("What is your name? ")
birthday_song(username)
'''

# Lab 2

# list of cards
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# what to display when cards_picked is called upon
def cards_picked(card):
  print(f"You drew a: {card}.")

import random

# picks one of the cards from the list
choice1 = random.choice(number)
cards_picked(choice1)

# picks a second card
choice2 = random.choice(number)
cards_picked(choice2)

# picks a third card
choice3 = random.choice(number)
cards_picked(choice3)

# picks a fourth card
choice4 = random.choice(number)
cards_picked(choice4)

# picks a fifth card
choice5 = random.choice(number)
cards_picked(choice5)