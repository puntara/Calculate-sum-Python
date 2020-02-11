#!/usr/bin/env python
# coding: utf-8

# In[1]:


def summer(n):
    sum=0
    for i in range (n+1):
        if (i%3==0 or i%5==0):
            sum=sum+i
    return sum
x=summer(10)
y=summer(150)
z=summer(975)
print(x)
print(y)
print(z)

