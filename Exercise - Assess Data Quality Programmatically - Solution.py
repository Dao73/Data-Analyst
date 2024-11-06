#!/usr/bin/env python
# coding: utf-8

# # Assess Data Quality Programmatically

# In this exercise, you will perform a programatic assessment of U.S. Bureau of Labor Statistics' "Occupational Employment and Wage Statistics (OEWS) Research Estimates by State and Industry". This dataset contains data on manager role occupations and the hourly wage. 
# 
# You will be assessing this data for **completeness** and **consistency**.
# 
# As a supplementary dataset, you are provided with an additional dataset, the 2021 1-year ACS PUMS dataset, to validate the data quality issues against.

# In[1]:


#DO NOT MODIFY - imports
import pandas as pd
import numpy as np


# ## Datasets context
# 
# ### OEWS data (uncleaned)
# 
# The OEWS dataset was gathered manually as a CSV from the U.S. Bureau of Labor Statistics' website. The data was narrowed down to specifically focus on the managerial domain.
# 
# The dataset has a number of variables - there are four variables of significance to us:
# 
# - AREA_TITLE: Area/location name, e.g. Alabama
# - OCC_CODE: The Standard Occupational Classification (SOC) code, e.g. 11-0000
# - OCC_TITLE: The Standard Occupational Classification (SOC) title, e.g. Management Occupations
# - H_MEAN: The mean hourly wage of the worker, e.g. 61.13
# 
# ### PUMS data (cleaned)
# 
# The PUMS dataset was downloaded via the Census Data API from the United Statest Census Bureau, and narrowed down for the Kern County - Bakersfield MSA, California area.
# 
# Dataset variables:
# 
# - WRK: Whether the individual worked last week
#     - 0: N/A (not reported)
#     - 1: Worked
#     - 2: Did not work
# - SEX: Sex (Male / Female) of the individual
#     - 1: Male
#     - 2: Female 
# - SCOP: Standard Occupational Classification (SOC) codes for 2018 and later, based on the 2018 SOC codes

# In[2]:


#DO NOT MODIFY
#Read in the uncleaned excel file (note: will take a few minutes to load)
oews_data = pd.read_excel('oes_research_2021_sec_55-56.xlsx')
#Show the first few rows
oews_data.head()


# In[3]:


#DO NOT MODIFY
#Read the cleaned .json file
cleaned_pums = pd.read_csv('cleaned_pums_2021.csv')
#Show the first few rows
cleaned_pums.head()


# ## 1. Inspect the completeness
# 
# In the first step, take a look at the completeness of the OEWS dataset, and identify any missing or incomplete values.

# ### 1.1 Create a subset of the dataset 
# Create a subset of the dataset to only include the required variables: `AREA_TITLE`, `OCC_CODE`, `OCC_TITLE`, `H_MEAN`. **Use this subset for all the following steps in this exercise.**
# 
# Check if there are any NA values in the data programmatically using `isnull()`.

# In[8]:


#FILL IN - create a subset of the dataset
#oews_data_subset = 
oews_data_subset = oews_data[['AREA_TITLE', 'OCC_CODE', 'OCC_TITLE', 'H_MEAN']]


# In[9]:


#FILL IN - check programmatically if there are NA values using isnull()
print(oews_data_subset.isnull().sum().sum())


# ### 1.2 Check the summary statistics
# Use the `.describe()` and `.info()` function to check the summary statistics for the OEWS dataset, specifically the `H_MEAN` variable. 

# In[10]:


#FILL IN - run the .describe() function
oews_data_subset.describe()


# In[11]:


#FILL IN - run the .info() function
oews_data_subset.info()


# ### 1.3 Look into the dtype of the dataset.
# There are a couple of things to notice.
# 1. The `H_MEAN` variable should be a numerical dtype (i.e., 'float64'), but is instead an object. 
# 2. Using the `.describe()`, we see the `*` sign under `H_MEAN`, which indicates a wage estimate is **not available** - hence, it should be a NaN value, even though it isn't phrased as such. 
# 
# To solve this issue, replace the `*` sign in `H_MEAN` with a `np.NaN` object for the `H_MEAN` variable using `.replace()`.

# In[12]:


#FILL IN - Print the dtypes
print(oews_data_subset.dtypes)


# In[13]:


#DO NOT MODIFY
#Disable chained assignments
#Objective: Silences warnings when operating on slices of dataframes
#for the purposes of this exercise
pd.options.mode.chained_assignment = None 


# In[14]:


#FILL IN
#Replace the * sign with np.nan
oews_data_subset['H_MEAN'] = oews_data_subset['H_MEAN'].replace({'*': np.nan})


# ### 1.4 Check the number of NA values again
# Now, check the NA values in in the OEWS dataset again

# In[15]:


#Check number of NA values in OEWS data
print(oews_data_subset.isnull().sum().sum())


# ## 2. Inspect the consistency

# Check for consistency between the OEWS and PUMS data for the `AREA_TITLE` and `OCC_CODE`/`SOCP` variables, and answer the following questions.

# ### 2.1 Is the Area consistent between the two datasets? 
# **Note**: Recall that the PUMS dataset **only** contains data for the Kern County - Bakersfield MSA, California area.
# 
# Is the Area consistent between the two datasets? Use the `.head()` function, and optionally `.describe()` and `.info()`.

# In[16]:


#FILL IN - inspect the head of the OEWS dataframe
oews_data_subset.head()


# In[17]:


#FILL IN - inspect the head of the PUMS dataframe
cleaned_pums.head()


# *Answer*: 
# 
# The locations are not consistent - the OEWS data is providing data for multiple states within the US.

# ### 2.2. Are the occupation codes consistent?
# 
# Are the occupation codes consistent between the two datasets (`OCC_CODE` and `SOCP`)? Use the `.sample()` function to pull a few random samples from the dataset. What is the difference, if any?

# In[18]:


#FILL IN
#Pull a random sample from the OEWS dataframe, indexed on OCC_CODE
oews_data_subset['OCC_CODE'].sample(4)


# In[19]:


#FILL IN
#Pull a random sample from the cleaned_pums dataframe, indexed on SOCP
cleaned_pums['SOCP'].sample(4)


# *Answer*: 
# 
# We can see inconsistency between the SCOP and OCC_code variables - specifically the format (the lack of a hyphen in the PUMS' SCOP dataset).

# In[ ]:




