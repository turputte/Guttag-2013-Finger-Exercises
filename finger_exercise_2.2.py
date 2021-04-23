#!/usr/bin/env python3
# John Guttag - Introduction to computation and programming
# using python
# Chapter 2.2 Finger Exercise
# Finger exercise: Write a program that examines three variables— x , y , and z —
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.

numbers = [input('Enter a value: ') for i in range(10)]
odds = [y for y in numbers if y % 2 != 0]
if odds:
	print(max(odds))
else:
	print('All declared variables have even values.')
