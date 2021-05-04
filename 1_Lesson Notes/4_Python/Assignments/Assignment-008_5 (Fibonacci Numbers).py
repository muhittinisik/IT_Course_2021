#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment-008/5 (Fibonacci Numbers)

fibonacci = []
sayı1 = int(input("Enter the first number of fibonacci series: "))
sayı2 = int(input("Enter the second number of fibonacci series: "))
fibonacci.append(sayı1)
fibonacci.append(sayı2)
toplam = 0
i = 2
while not max(fibonacci)>= 55:
    toplam = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(toplam)       
    i += 1
print(fibonacci) 

