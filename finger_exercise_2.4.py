#!/usr/bin/python
# John Guttag - Introduction to computation and programming
# using python
# Chapter 2.4 Finger Exercise
# Write a program that asks the user to input 10 integers
# and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.

numbers = [int(input('Enter an integer: ')) for i in range(10)]
odds = [y for y in numbers if y % 2 != 0]
if odds:
    print('The largest odd value is ', max(odds))
else:
    print('All declared variables are even.')

# With input control
# numbers = []  # Declare an input list
# odds = []  # Declare a list for odd numbers
# sequence = range(10)
# for i in sequence:
#    while True:
#        try:
#            x = int(input('{} Enter an integer '.format(sequence[i] + 1)))
#            break
#        except ValueError:
#            print('Only integers. (1,2,3,4,5,...)')
#    numbers.append(x)
#
# odds = [y for y in numbers if y % 2 != 0]
# if odds:
#    print('The largest odd value is ', max(odds))
# else:
#    print('All declared variables have even values.')
