#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports - do not modify
from bs4 import BeautifulSoup


# In[2]:


with open("language_of_flowers.html") as fp:
    flower_soup = BeautifulSoup(fp, 'html.parser')


# In[3]:


flower_soup


# In[4]:


#Print a clean (prettier) version to look through
print(flower_soup.prettify())


# In[5]:


book_title = flower_soup.find("title")
print(book_title)


# In[6]:


book_title = book_title.text.strip()
print(book_title)


# In[7]:


uploader_name = flower_soup.find("a", class_="item-upload-info__uploader-name")
print(uploader_name.text.strip())


# In[8]:


#Find the tag
collection_items = flower_soup.find_all("a", class_="collection-item")
print(collection_items)


# In[9]:


for item in collection_items:
    print(item.text.strip())


# In[10]:


#Find the tag
print(flower_soup.find("a", class_="collection-item").text.strip())


# In[ ]:




