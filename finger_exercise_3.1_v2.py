# /usr/bin/env python3
# John Guttag - Introduction to computation and programming
# using python
# Chapter 3.1 Finger Exercise
# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6
# and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should
# print a message to that effect.
x = int(input("Enter an integer :"))

for pwr in range(1,6):
    root = x**(1/pwr)
    if root == x:
        ans_root=int(root)
        ans_pwr=pwr
        print('root :', ans_root,'  pwr :', ans_pwr)
        
if ans_root != x:
        print ('No such pair of integers exists!')
