# /usr/bin/env python3
# John Guttag - Introduction to computation and programming
# using python
# Chapter 3.1 Finger Exercise
# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6
# and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should
# print a message to that effect.
import time



x = int(input("Enter an integer :"))

startTime = time.time()

# Find out what integer root for integer pwr,  1, 2, 3, 4 or 5, leads to x=root**pwr where x is of type integer.
# x=root**pwr leads to root=x**(1/pwr) 
for pwr in range(1,6):
    root = x**(1/pwr)
    if root == x:
        ans_root=int(root)
        ans_pwr=pwr
        print('root :', ans_root,'  pwr :', ans_pwr)


if ans_root != x:
        print ('No such pair of integers exists!')


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
