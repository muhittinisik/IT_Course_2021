#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/4 (Is it a Prime Number?)
# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

number = int(input("Please enter a number : "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

