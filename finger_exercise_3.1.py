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
startTime = time.time()

x=40

#x = int(input("Enter an integer :"))
for pwr in range(1,6):
    root = x**(1/pwr)
    if x == 0:
        if root == x:
            print ('root =:',int(root),'pwr =',pwr)
    elif x < 0:
        if root == x:
            print ('root =:',int(root),'pwr =',pwr)
    else:
        if root == x:
            print ('root =:',int(root),'pwr =',pwr)
            
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
    
