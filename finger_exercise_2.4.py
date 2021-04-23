#!/usr/bin/python
# John Guttag - Introduction to computation and programming
# using python
# Chapter 2.4 Finger Exercise
# Write a program that asks the user to input 10 integers
# and then prints the largest odd number that was entered. 
# If no odd number was entered, it should print a message to that effect.

# Shortest solution with "List Comprehension":
# numbers = [input('Enter a value: ') for i in range(10)]
# odds = [y for y in numbers if y % 2 != 0]
# if odds:
#    print(max(odds))
# else:
#    print('All declared variables have even values.')

# Without "List Comprehension" but "input control"
numbers = []  # Declare a list numbers input
odds = []  # Declare a list for odd numbers
sequence = range(10)
for i in sequence:
    while True:
        try:
            x = int(input('{} Enter an integer '.format(sequence[i] + 1)))
            break
        except ValueError:
            print('Only integers. (1,2,3,4,5,...)')
    numbers.append(x)
print('The ten integers are ', numbers)

for y in numbers:
    if y % 2 != 0:
        odds.append(y)

print('The odd numbers are ', odds)

if odds:
    print('The largest odd value is ', max(odds))
else:
    print('All declared variables have even values.')
