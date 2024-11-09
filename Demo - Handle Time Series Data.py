#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#Inspect the first few rows of the dataframe
#This data is a hypothetical stock dataset (not meant to be accurate)

#Note - date is in YYYY-MM-DD ( %Y-%m-%d ) format
df = pd.read_csv('time_series_data.csv')
df.head()


# ## Inspect the data

# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


#Plot the time series with date as the x-axis and volume as the y-axis
df.plot(x='Date', y='Volume (in millions)')


# ## Convert "Date" column to datetime objects

# In[6]:


#Work with dates as pandas datetime objects
df['Date'] = pd.to_datetime(df['Date'])


# In[7]:


#Understand the dataframe
df.info()


# In[8]:


#How much time does the data cover?
df['Date'].max() - df['Date'].min()


# In[9]:


#Create another column called Year
df['Year'] = df['Date'].dt.year


# In[10]:


#Visually inspect the dataframe
df.head()


# ## Set "Date" column to the index
# If we don't set the index as our date variable for this dataframe, we'll have access to relatively limited functionality.

# In[11]:


#Critical step - set the index as our Date column
df = df.set_index('Date')


# In[12]:


df.head()


# In[13]:


df.index


# In[14]:


#Now that we have a Datetime index, we can use .resample()
df.resample("Y")['Volume (in millions)'].mean()


# In[15]:


#Get the yearly mean volume
df.resample("Y")['Volume (in millions)'].mean().plot();


# In[16]:


#Get what day of the week the date falls on 
df['day_of_week'] = df.index.dayofweek
df.head()


# In[17]:


# Get all the rows where the days are a Monday
mondays = df[(df['day_of_week'].isin([0]))]
mondays.head()


# In[18]:


#Calculate the mean volumn for all Mondays
mondays['Volume (in millions)'].mean()


# In[19]:


#Convert our date variable to a specified format
temp_df = df.copy()
temp_df.index = df.index.strftime('%B %d, %Y')
temp_df.head()


# **Note:** If we don't set the index as our date variable, we would be forced to used the `dt` accessor. For example, in order to convert the date variable to a specific format, we would have had to use: 
# 
# `df['Date'].dt.strftime('%B %d, %Y')`

# ## Dealing with missing data

# In[20]:


new_df = pd.read_csv('missing_time_series_data.csv', index_col = 'index')
new_df.head()


# In[21]:


#Work with dates as pandas datetime objects
new_df['Date'] = pd.to_datetime(new_df['Date'])
new_df.head()


# In[22]:


new_df.isna().sum()


# In[23]:


#Fill NA by propogating last valid observation forward to the next valid
new_df = new_df.fillna(method="ffill")


# In[24]:


new_df.isna().sum()


# In[ ]:




