#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/7 (Fizz Buzz Numbers)

for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


# In[ ]:




