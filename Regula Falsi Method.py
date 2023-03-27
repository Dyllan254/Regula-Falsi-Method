#!/usr/bin/env python
# coding: utf-8

# In[18]:


import math
def f(x):
    return 2 * x**3 - 2 * x - 5

#Initial values are assumed
a=-100
b=200

#maximum iterations
max_iteration = 100000

#tolerance
tol=1e-6

def regulaFalsi(a, b):
    if f(a) * f(b) >= 0:
        print("a and be are not rightly assumed")
        return -1
        
        
    for i in range(max_iteration):
         
        c = (a * f(b) - b * f(a))/ (f(b) - f(a))
        fc = f(c)
        if abs(fc) < tol:
            return c
        
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : " , '%.6f' %c)
    
regulaFalsi(a,b)


# In[ ]:




