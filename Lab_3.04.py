'''
###############
Lab 3.04
###############
In Your Notebook
----------------
Aliasing
--------
1.  Will updating b affect a? Explain why or why not?
a = [1, 2, 4]
b = a

2.  Predict what my_list list will print out when this code is run. If you are not sure check the code by copying and running it.
# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)

Prediction:
Actual: 

Scope
-----
Draw a stack diagram for the following:

 var_1 = "kittens"
 var_2 = "cookies"

 # input: a string
 # output: a string
 def my_function(my_favorite_things):
     song_lyrics = "rain drops on roses,"
     combined_song = song_lyrics + my_favorite_things
     return combined_song

 # input: a string
 # output: a string
 def my_function_2(item, item2):
     full_lyrics = item + "on " + item2
     full_song = my_function(full_lyrics)
     return full_song

my_song = my_function_2(var_1, var_2)

##########
START HERE
##########

Complete the following on your own:
-----------------------------------
Write down what (if anything) is wrong with the following code.

If there was an issue write out how to fix it.

If you are unsure copy and run the code and fix it

Problem 1
---------
var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
    var_2 = "cat"

print_out_my_favorite(var_1)
print(var_2)

#######################################################################################################
In the function print_out_my_favorite, var_2 is "cat", but it is assigned as 'dog' out of the function.
For the code to not run an error, delete var_2 = "cat", and the code will run the function and print
var_2.
#######################################################################################################

Problem 2
---------
var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    var_1 = 'dog'
    var_2 = 'cat'
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")

print_out_my_favorite(var_1)
print(var_1 + " " + var_2)

#######################################################################################################
Nothing is wrong with this code. The function is called on with var_1 as its parameter. var_1 gets 
reassigned as 'dog', which is var_2 outside of the function, so var_1 in the function = var_2 outside
the function. This results in the second if statement running. The print statement uses the variables.
#######################################################################################################

Problem 3
---------
var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")

print_out_my_favorite(var_1)
print(var_2)

#######################################################################################################
Nothing is wrong with this code.
#######################################################################################################

In script mode
---------------------
Write a program using the following specifications
That has a global variable, my_num.

Create three functions that update my_num

add2: this function adds 2 to my_num

multiply_num: this function takes in a parameter, multiplier, and multiplies my_num by that parameter

add2_and_multiply: this function takes in a parameter, multiplier, and calls add2, then calls multiply_num.


Complete the program
--------------------
Write the following code in the main part of the program.

sets my_num to some initial value you choose

prints my_num

calls add2_and_multiply() with some argument you choose

prints the final value of my_num

Confirm that the printed values match what you expected.
'''

# my number code
my_num = 4
print("My number:") # here for clarity when script runs
print(my_num)

# adds 2 to my_num
def add2(my_num):
    my_num += 2
    print(my_num)

print("add2:") # here for clarity when script runs
add2(my_num)

# multiplies my_num by a parameter
def multiply_num(multiplier):
    print(my_num * multiplier)

print("multiply_num:") # here for clarity when script runs
multiply_num(2)

# calls on add2 and multiply_num
def add2_and_multiply(num):
    add2(my_num)
    multiply_num(num)

print("add2_and_multiply:") # here for clarity when script runs
add2_and_multiply(2)

# complete the script
my_num = 4
print("completing the script:") # here for clarity when script runs
print(my_num)

add2_and_multiply(2)