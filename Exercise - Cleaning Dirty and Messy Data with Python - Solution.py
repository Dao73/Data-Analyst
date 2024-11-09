#!/usr/bin/env python
# coding: utf-8

# # Cleaning Dirty and Messy Data with Python

# In this exercise, you will solve a few problems applying the methods you learned to clean dirty and messy data with Python. 
# 
# We will be considering a small hypothetical dataset of time series data being reported from pressure sensors on a manufacturing floor (that was post-processed) below.

# In[1]:


#Imports - DO NOT MODIFY
import pandas as pd
import numpy as np


# ## Dataset Context
# 
# Details of the data:
# 
# - The sensor location indicates the location where the sensor is placed and the system (A, B) it corresponds to (e.g. Entry A).
# - The dates indicates the days where data was collected from the sensors (e.g. 1/5/2023).
# - The numeric values indicate the pressure sensors' measurements (ranging from 0-25 bar)

# In[2]:


#FILL IN - Read in pressure_sensor_data.tsv into a pandas dataframe
df = pd.read_csv('pressure_sensor_data.tsv', sep='\t')


# In[3]:


df.head()


# ## 1.  Tidiness Issue:  Column Headers are values, not variable names
# 
# Use `pd.melt()` to ensure the column headers are no longer values and are instead variable names. Ensure the columns are named informatively when calling `pd.melt()` based on the values they represent.
# 
# Your result should have three variables (columns): `Sensor Location`, `Date`, `Pressure`.

# In[5]:


##FILL IN  - use .melt() to solve the tidiness issue
updated_df = df.melt(id_vars='Sensor Location', var_name='Date', value_name='Pressure')
#Show the first few rows of the dataframe
updated_df.head()


# ## 2. Tidiness Issue: Multiple variables stored in one column
# 
# The `Sensor Location` column violates one of the guidelines of tidiness - multiple variables being stored in column. Use the updated data from step 1 to identify why and resolve thie issue.
# 
# *Hint:* Consider using the `str.split(expand=True)` functionality since the sensor location and system data is separated by a space (e.g., "Entry A")

# *FILL IN - how are multiple variables being stored in the `Sensor Location` column?*
# 
# The column includes both the sensor location and the system it corresponds to. This information can be seperated into two columns.

# In[6]:


# FILL IN - split the variables in the Sensor Location into multiple variables/columns
updated_df[['Sensor Location', 'System']] = updated_df['Sensor Location'].str.split(expand=True)
updated_df.head()


# ## 3. Quality Issue: Validity and Accuracy
# 
# 3.1 Between Jan 5th to Jan 6th, some of sensors' data for both Systems A and B were found to be corruputed due to a sudden, very high increase in temperature. 
# 
# Filter out rows where the sensors' reported data is **greater than 25 bar** into a seperate dataframe, and drop these rows from the original dataframe. 
# 
# *Hint:* Specify the invalid rows' index to drop these rows from the original dataframe.

# In[8]:


# FILL IN - get the rows where the data is greater than 25 bar in a seperate dataframe
invalid_data = updated_df[updated_df['Pressure'] > 25]
#Print the index of the new dataframe with invalid rows
invalid_data.index


# In[12]:


#FILL IN - drop the invalid rows from the original dataframe using .drop(...)
updated_df = updated_df.drop(invalid_data.index)
#Reset the index
updated_df = updated_df.reset_index()
#Display the first few rows
updated_df.head()


# 3.2 Use the `describe` function to check that the fix was successful. Are the `min` and `max` of the `Pressure` variable in the right range?

# In[13]:


#FILL IN - validate the range using .describe()
updated_df.describe()


# *FILL IN - is the range correct (Yes/No)*: ...
# 
# The `Pressure` variable's range is correct, within 0-25 bar.

# In[ ]:




