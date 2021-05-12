#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/8 (Leap Years)

year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

