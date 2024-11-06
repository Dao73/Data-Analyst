#!/usr/bin/env python
# coding: utf-8

# # Demo - JSON Files in Python

# ## Option 1: built-in `json` module
# 
# Using the Python built-in `json` module to extract JSON data from a request.

# In[1]:


#import libraries
import requests
import json

#Make an HTTP GET Request to book on Archive.org
book = requests.get("https://archive.org/metadata/cu31924067841738")


# In[2]:


book.text


# In[3]:


json_book_text = json.loads(book.text)
json_book_text


# In[4]:


json_book_content = json.loads(book.content)
json_book_content


# ## Option 2  `.json()`
# 
# Use the `.json()` method of a response object from the requests library to extract JSON data

# In[5]:


#Make an HTTP GET Request to book on Archive.org
book = requests.get("https://archive.org/metadata/cu31924067841738")

#Get the JSON
requests_json_data = book.json()
requests_json_data


# ## Navigate JSON files

# In[6]:


json_book_text['dir']


# In[7]:


json_book_text['metadata']


# In[8]:


json_book_text['metadata']['title']


# In[9]:


json_book_text['reviews']


# In[10]:


json_book_text['reviews'][0]


# In[11]:


json_book_text['reviews'][0]['reviewbody']


# In[12]:


json_book_text['files']


# In[13]:


json_book_text['files'][6]


# In[14]:


json_book_text['files'][6]['size']


# ## JSON vs. Dictionaries

# In[15]:


dictionary = {1: 'Hello', 2: 'World'}
dictionary


# In[16]:


dictionary[1]


# In[17]:


json_book_text['dir']


# In[18]:


json.dumps(dictionary)


# In[ ]:





# In[ ]:




