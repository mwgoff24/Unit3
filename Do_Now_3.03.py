'''
###############
Do Now 3.03
###############
1.  In script mode
Type the following code
import random
# inputs:  x (int), y (int)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y

def mystery_function(x, y):
    random_number = random.randint(0,1)
    if random_number > 0:
        z = x + y
    else:
        z = x * y
    return z

mystery_function(1, 2)

2.  In your Notebook
Answer the following questions
What happens when your run this code? How do you know what the result was?

Nothing is displayed when the code is ran. 
1 and 2 replace x and y, and if randint is 1, the program will return 3, and if randint is 0 it will return 2.

Keeping the function the same, rewrite the code to print out the value that the function returns.
'''
import random
# inputs:  x (int), y (int)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y

def mystery_function(x, y):
    random_number = random.randint(0,1)
    if random_number > 0:
        z = x + y
    else:
        z = x * y
    return z

print(mystery_function(1, 2))
# added print function to return z in console
# can also replace return z with print(z)