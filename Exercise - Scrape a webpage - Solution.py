#!/usr/bin/env python
# coding: utf-8

# # Exercise - Scrape a Webpage

# In this exercise, you'll be scraping the Internet Archive to gather data on an item in the archive.org: The book "Robinson Crusoe". 
# 
# This exercise allows you to practice your skills around scraping, gathering via an API, and filtering important data corresponding to an item in a catalog. Data wranglers apply these skills for many applications including gathering data on product reviews, movie recommendations, etc. 
# 
# Let's get started!

# In[1]:


#Imports - do not modify
import requests
from bs4 import BeautifulSoup


# ## 1. Scrape the HTML

# 1.1 The novel Robison Crusoe is available on archive.org via the following url: https://archive.org/details/cu31924011498676/mode/2up. 
# 
# Create a HTTP GET request via the requests library to get the HTML in Unicode from this page.

# In[2]:


#FILL IN
item = "https://archive.org/details/cu31924011498676/mode/2up"
#Create an HTTP GET request
book_metadata = requests.get(item)
#Raise an exception if we made a request resulting in an error
book_metadata.raise_for_status()
#Access the content of the response in Unicode
archive_text = book_metadata.text
#Check that it worked
print(archive_text)


# 1.2 Use BeautifulSoup to parse the HTML. Optionally, you could prettify the HTML, so you can look through the file. 

# In[3]:


#FILL IN
#Use BeautifulSoup to parse the HTML
soup_archive = BeautifulSoup(archive_text, 'html.parser')
#OPTIONAL - Print a clean (prettier) version to look through
print(soup_archive.prettify())


# Let's now answer a few questions around this item by getting specific tags from the HTML.
# 
# **Note:** You can use a find/search tool (e.g., on Windows, Command F; on Mac, Control F) to identify tags in the HTML or download the prettified version locally to your system to use a Notepad application for searching the tags for the next section.

# 1.3 What is the username of the uploader? Print the username in text **(not in HTML)**. 
# 
# **Hint**: This is the HTML snippet containing the username
# 
# ```
# <a class="item-upload-info__uploader-name" href="/details/@hank_b"> hank_b </a>
# ```

# In[12]:


#FILL IN
#Find the tag
username = soup_archive.find("a", class_="item-upload-info__uploader-name")
print(username)
#Strip the username from the HTML
#Example code: username = username.text.strip()
username = username.text.strip()
print(username)


# 1.4 How many pages does the book have? Print the result in text, **not in HTML**. You may use find() or find_all().
# 
# **Hint**: This is the HTML snippet containing the no. of pages.
# ```
# <dl class="metadata-definition">
#            <dt>
#             Pages
#            </dt>
#            <dd class="">
#             <span itemprop="numberOfPages">
#              418
#             </span>
#            </dd>
#           </dl>
# ...
# ```

# In[5]:


#FILL IN
#Find the tag
no_of_pages = soup_archive.find_all("span", itemprop="numberOfPages")
print(no_of_pages)

#Strip the number from the HTML
no_of_pages = no_of_pages[0].text.strip()
print(no_of_pages)


# Check your work with the below assertions.

# In[6]:


#DO NOT MODIFY
#Ensure these assert statements pass before moving to the next section
assert username == 'hank_b'
assert no_of_pages == '418'


# ## Use the API

# With the Internet Archive, an item’s metadata can be fetched by making an HTTP GET request to its API https://archive.org/metadata/{identifier}. 
# 
# Our item's identifier is cu31924011498676.
# 
# 2.1 Use the requests library to get the metadata in JSON format and print the JSON.

# In[7]:


#FILL IN
#Create an HTTP GET request to the metadata API
#book_metadata = ...
book_metadata = requests.get("https://archive.org/metadata/cu31924011498676")
#Raise an exception if we made a request resulting in an error
book_metadata.raise_for_status()
#Get the JSON
book_text = book_metadata.json()
print(book_text)


# Inspect the hierarchy of attributes and retrieve values from the JSON to answer the following questions:
# 
# 2.2 What camera was used?

# In[8]:


#Get the name of the camera
#camera_name = ...
camera_name = book_text['metadata']['camera']


# 2.3 What is the size of the PDF of the book?
# 
# Hint: The `files` attribute has a list as a value, so you will need to use list indexing to get to the PDF attribute. 

# In[9]:


book_text['files']


# In[10]:


#FILL IN
#Get the name of the PDF
#pdf_size = ...
print(book_text['files'][3])
pdf_size = book_text['files'][3]['size']


# Check your work with the below assertions.

# In[11]:


#DO NOT MODIFY
#Ensure these assert statements pass before moving on
assert camera_name == 'EOS-1DS MARK ll'
assert pdf_size == '8987708'


# In[ ]:





# In[ ]:




