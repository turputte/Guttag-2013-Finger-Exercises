#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# John Guttag - Introduction to computation and programming
# using python
# Chapter 2.2 Finger Exercise
# Finger exercise: Write a program that examines three variables— x , y , and z —
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.
while True:
    try:
        x = int(input('Write an integer x='))
        break
    except ValueError:
        print('Only integers')
while True:
    try:
        y = int(input('Write an integer y='))
        break
    except ValueError:
        print('Only integers')
while True:
    try:
        z = int(input('Write an integer z='))
        break
    except ValueError:
        print('Only integers')
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('Non are odd numbers')
elif x % 2 == 0 and y % 2 == 0:
    print(z, ' is the only and largest odd number')
elif y % 2 == 0 and z % 2 == 0:
    print(x, ' is the only and largest odd number')
elif x % 2 == 0 and z % 2 == 0:
    print(y, ' is the only and largest odd number')
elif x % 2 == 0:
    if y > z:
        print(y, ' is the largest odd number')
    elif y == z:
        print(y, z, ' are equal and are the largest odd numbers')
    else:
        print(z, ' is the largest odd number')
elif y % 2 == 0:
    if x > z:
        print(x, ' is the largest odd number')
    elif x == z:
        print(x, z, ' are equal and are the largest odd numbers')
    else:
        print(z, ' is the largest odd number')
elif z % 2 == 0:
    if x > y:
        print(x, ' is the largest odd number')
    elif x == y:
        print(x, y, ' are equal and are the largest odd numbers')
    else:
        print(z, ' is the largest odd number')

