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

nums = [x, y, z]
odds = [i for i in nums if i % 2 != 0]
if odds:
    print('The largest odd value is ', max(odds))
else:
    print('None of the numbers are odd!')
