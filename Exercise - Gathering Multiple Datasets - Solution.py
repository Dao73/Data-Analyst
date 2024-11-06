#!/usr/bin/env python
# coding: utf-8

# # Exercise - Gathering Multiple Datasets

# 
# In this excersise, you will gather the hospital building data using three different gathering methods. The data includes information on hospital buildings such as height, number of stories, etc.
# 
# Ensure you programmatically load your dataset(s) into the notebook.

# In[2]:


#Imports - can be modified
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


# ## 1. Extract a dataset via API

# ### 1.1 Extract a dataset via API
# You may use the requests library to do so programmatically, or manually access the dataset via an API:
# 
# https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=d97adf28-ebaf-4204-a29e-bb6bdb7f96b9

# https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=d97adf28-ebaf-4204-a29e-bb6bdb7f96b9

# In[3]:


#FILL IN - extract a dataset via API

#Specify the URL and extract data
url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=d97adf28-ebaf-4204-a29e-bb6bdb7f96b9'  
api_metadata = requests.get(url)

#Raise an exception if we made a request resulting in an error
api_metadata.raise_for_status()

#Get the JSON
api_text = api_metadata.json()


# ### 1.2 Parse the obtained data
# Parse the obtained data to get the **first** relevant data value or record from your JSON file. 
# 
# **Note:** Please ensure the result you obtain is in text and is relevant to hospital building data.

# In[4]:


#Fill in - get the first data record/value from the JSON results
api_text['result']['records'][0]


# Answer: 
# 
# I see data related to a hospital building in Alemeda. The facility name is Alameda Hospital and the building has four stories. The building Nbr is `BLD-01278`.

# ## 2. Extract a dataset via manual download

# ### 2.1 Download a dataset manually
# We provided you a csv file `hospital_building_data.csv`. You can think that we pre-downloaded the data for you.
# 
# Load the dataset into this notebook.

# In[5]:


#FILL IN - load a dataset that was downloaded manually
cal_hhs = pd.read_csv('hospital_building_data.csv', encoding='utf-8')


# ### 2.2 Parse the obtained data
# Parse the obtained data to get the **first** relevant data value or record from your manually downloaded dataset.
# 
# **Note:** Please ensure the result you obtain is relevant to the hospital building data.

# In[6]:


#Fill in - get the first data record/value from the manually downloaded file
cal_hhs.head(1)


# Answer: 
# 
# The output data is the same with the data gathered from API. The facility name is Alameda Hospital and the building has four stories. The building Nbr is `BLD-01278`.

# ## 3. Extract a dataset via scraping

# ### 3.1 Extract your dataset via scraping
# Data webpage url:
# 
# https://data.chhs.ca.gov/datastore/odata3.0/d97adf28-ebaf-4204-a29e-bb6bdb7f96b9
# 
# Extract your dataset via scraping using `requests`, and `BeautifulSoup`.

# In[7]:


##FILL IN - extract a dataset via scraping
url = "https://data.chhs.ca.gov/datastore/odata3.0/d97adf28-ebaf-4204-a29e-bb6bdb7f96b9"
data = requests.get(url)
#Raise an exception if we made a request resulting in an error
data.raise_for_status()
#Access the content of the response in Unicode
data_txt = data.text


# In[8]:


#FILL IN
#Use BeautifulSoup to parse the XML
soup_text = BeautifulSoup(data_txt)
#Print the prettified version
soup_text.prettify()


# ### 3.2 Parse the obtained data 
# Parse the obtained data to get a relevant data value or record from your scraped dataset. Briefly describe the data you are specifically parsing from the gathered data.
# 
# **Note:** Please ensure the result you obtain is in text (not with HTML tags) and is relevant to the hospital buidling data. Hint: you can use the `find_all()` method with tags like `d:buildingname`, `d:buildingcode`, etc.

# In[9]:


#FILL IN - parse specific records from scraped data
[hs.get_text() for hs in soup_text.find_all('d:buildingname')]


# Brief description of specific data parsed:
# 
# I parsed all the hospital buildings in the dataset.

# In[ ]:




