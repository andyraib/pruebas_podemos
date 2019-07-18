#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


# In[2]:


## Programa del 1 al 100
# Multiplos de 3 == 'Humpty'
# Multiplos de 5 == 'Dumpty'
# Multiplos de 3 y 5 'HumptyDumpty'

for i in range (1,100+1):
    if i%3 == 0 and i%5 == 0:
        print('HumptyDumpty: ', i)
    elif i%3 == 0:
        print('Humpty:', i)
    elif i%5 == 0:
        print('Dumpty:', i)
    else:
        print(i)


# In[3]:


## Suma de numeros naturales debajo del 1000
# MUltiplos de 3 o 5 

print(sum(int(v) for v in range(1,1000) if v%3 == 0 or v%5 == 0))

