#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent('aabbbc'))


# In[ ]:




