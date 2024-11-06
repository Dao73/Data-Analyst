#!/usr/bin/env python
# coding: utf-8

# ## Option 1: use HTTP GET request

# In[1]:


import requests
import json


# In[2]:


book = requests.get("https://archive.org/metadata/cu31924067841738")
print(book)


# In[3]:


book.raise_for_status()


# In[4]:


#Get the JSON
json_data = book.json()
print(json_data)


# In[5]:


with open('book.json', 'w') as f:
    json.dump(json_data, f)


# ## Option 2: use customized developer libraries

# **Note:** `interectarchive` libary is not installed in the workspace so the code below won't run successfully. The code is for demonstration purpose only.

# In[6]:


from internetarchive import get_item 

book = get_item('cu31924067841738')
print(book)


# In[ ]:


for k,v in book.metadata.items():
    print(k,":",v)


# In[ ]:





# In[ ]:





# In[ ]:




