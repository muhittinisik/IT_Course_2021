#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/2 (Covid-19 Risk) is due
# Task : Assignment-008/3 (Is it an Armstrong Number?)

sayı = input("Enter a positive integer number: ")

if not sayı.isdigit() or int(sayı)<0 or float(sayı) == True:
    cıktı = "It is an invalid entry. Don't use non-numeric, float, or negative values!"
else:
    toplam = 0
    for i in range (len(sayı)):
        toplam += int(sayı[i])**len(sayı)
    if int(sayı) == toplam:
        cıktı = sayı + " is an Armstrong number"
    else:
        cıktı = sayı + " is not an Armstrong number"
print(cıktı)

