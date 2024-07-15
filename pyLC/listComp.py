
# Expression-oriented functions in Python include:
# Expression-oriented functions in Python refer to functions and constructs that are centered around expressions rather than statements. In simpler terms, they focus on producing values and can be used within other expressions. Here’s a breakdown of some key expression-oriented functions and constructs:

arrr = [1,3,5,7,9]

#  --- [1,9,25,49,81]


#-- LIST
#  List Comprehensions

# List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses.


#    ---- List comprehensions
#     Lambda functions
#     Map
#     Filter
#     Reduce

from math import sqrt


#FInd the aquaroot of these numbers = 
first_numbers = 25,64,99,16,9,625

squareroot = [sqrt(item) for item in first_numbers]
print(squareroot)

#Find the square of these numbers from 5 - 15

sqaureNumber = [item**2 for item in range(5,15)]
print(sqaureNumber)


# add mr to each of these Names
menNames = ['dele' , 'bayo' , 'kunle' , 'edebiyi', 'kolawole' , 'wellington']
makeMisters = [f'mr {item}' for item in menNames]
print(makeMisters)


# 2. Lambda Functions

# Lambda functions are small anonymous functions defined using the lambda keyword. They can have any number of arguments but only one expression. The expression is evaluated and returned.

# EXMAPLES
# create aanonymous function that add three numbers
addthreeNumbers = lambda a,b,c: a + b + c

threenum = addthreeNumbers(2,4,6)
print(threenum)


# create an anonmous function that returns a greetings
greetMe = lambda name : 'Good Morning ' + name
print(greetMe("Yusuf"))

# Lambda functions in Python are particularly useful in scenarios where you need a small, anonymous function for a short period of time. They are often used in conjunction with functions that accept other functions as arguments (higher-order functions) like map(), filter(), and sorted() or in scenarios where defining a named function would be overkill or less readable.


# create a function that add any number of numbers as an anonymous function
# eg you put two numbers it adds two of them
# you put three it adds three of them


#  Map Function

# The map() function applies a given function to all items in an input list (or any iterable) and returns a list of the results.


# map(function, iterable)

# function: A function that will be applied to each item in the iterable.
# iterable: An iterable (e.g., list, tuple) that contains the items to be processed.

#iterable
squareNumbers = [2,4,6,8,10]

# function
def square(x):
    return x**2

squareThem = map(square , squareNumbers)
squareee = map(lambda x: x*2 ,squareNumbers )
# although you also have to specify the output format bu specifying it as a list
print(list(squareee))



# let say you want to check any number if it is even or odd return 1 for even return 0 fro odd

def checkEvenOdd(x):
    if x % 2 == 0:
        return f'{x} is even'
    else:
        return f'{x} is odd'

numbersToCheck = [1,2,4,5,6,7,8,9,11,13,15,12]

evenOddCheck = map(checkEvenOdd, numbersToCheck)

print(list(evenOddCheck))


# Filter Function

# The filter() function constructs an iterator from elements of an iterable for which a function returns true. It filters elements based on a function that tests each element.

# We can use it to filter things out
# for exmaple let say we want to filter out nubmber that are divisibel by 5

# filter(function , iterable)


divsibleByFive = [1,2,5,7,8,10,11,15,12,19]

def fivesMultiples(x):
    if(x % 5 == 0):
        return x

filtredFives = filter(fivesMultiples , divsibleByFive)

print(list(filtredFives))

from functools import reduce


#get the maximum values

getMaxvalue = [2,3,5,6,7,8,11,2,4]

def checkMax(a,b):
    if(a > b):
        return a
    else:
        return b

maxValue = reduce(checkMax , getMaxvalue)


# get the minimum value

def checkMin(a,b):
    if(a < b):
        return a
    else:
        return b

print((maxValue))

minValue = reduce(checkMin , getMaxvalue)
print(minValue)


# Addup All Numbers in an Array
def addallNum(a,b):
    return a + b

totalNumber = reduce(addallNum , getMaxvalue )
print(totalNumber)


# List Comprehensions: Create lists based on existing lists in a concise manner.
# Lambda Functions: Define small, anonymous, single-expression functions.
# Map Function: Apply a function to every item in an iterable and return a list of the results.
# Filter Function: Filter elements of an iterable based on a function that tests each element.
# Reduce Function: Reduce an iterable to a single value by applying a function cumulatively to the elements.


# LIST COMPREHENSION ON FILES
# whne you wnat to deal with file check for files not about getting the contenst insode it then you really have to import os

import os

# list all the directories in this path

# list all files in the current path
 # print(os.listdir())


print(os.chdir('../pyfiles'))


