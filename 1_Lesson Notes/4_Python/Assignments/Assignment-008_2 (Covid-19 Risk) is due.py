#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/2 (Covid-19 Risk) is due
# Task : Estimating the risk of death from coronavirus. 
# Write a program that; Takes "Yes" or "No" from the user as an answer to the following questions :

age = input ("Are you a cigarette addict older than 75 years old? ").capitalize()
chronic = input ("Do you have a severe chronic disease? ").capitalize()
immune = input ("Is your immune system too weak? ").capitalize()
if age == "Yes" and chronic == "Yes" and immune == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")

