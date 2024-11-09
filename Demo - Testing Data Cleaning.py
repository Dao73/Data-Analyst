#!/usr/bin/env python
# coding: utf-8

# # Demo - Testing Data Cleaning

# In[1]:


#Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

#Read the .json file
orig_pums = pd.read_json('2021-pums.json')
orig_pums.head()


# In[3]:


### Cleaning code for PUMS dataset: Step 1

#Make copies of the dataframes
cleaned_pums = orig_pums.copy()
#Define the 0th row as the header
cleaned_pums.columns = cleaned_pums.iloc[0]
cleaned_pums = cleaned_pums.drop(cleaned_pums.index[0])
cleaned_pums = cleaned_pums.reset_index(drop=True)
#Keep the WRK, SEX, and SCOP variables
cleaned_pums = cleaned_pums[['WRK', 'SEX', 'SOCP']]
#Replace 0 values in WRK column with np.nan
cleaned_pums['WRK'] = cleaned_pums['WRK'].replace({'0': np.nan})


# In[4]:


sns.heatmap(cleaned_pums.isna().transpose(),
            cbar_kws={'label': 'Missing Data'})


# In[5]:


### Cleaning code for PUMS dataset: Step 2
#Drop NA values in PUMS dataset
cleaned_pums = cleaned_pums.dropna()


# In[6]:


sns.heatmap(cleaned_pums.isna().transpose(),
            cbar_kws={'label': 'Missing Data'});


# In[ ]:


#Read in the excel file (note: will take a few minutes to load)
orig_wage_df = pd.read_excel('oes_research_2021_sec_55-56.xlsx')
#Show the first few rows
orig_wage_df.head()


# In[ ]:


#Make copies of the dataframes
cleaned_wage = orig_wage_df.copy()
#Replace alphanumeric characters (missing values + outliers) with NANs
cleaned_wage['H_MEAN'] = cleaned_wage['H_MEAN'].replace({'*': np.nan})
cleaned_wage['H_MEAN'] = cleaned_wage['H_MEAN'].replace({'#': np.nan})
#Filtering the dataframe to specific data elements
cleaned_wage = cleaned_wage[['AREA_TITLE', 'OCC_CODE', 'OCC_TITLE', 'H_MEAN']]
#Filter to only contain values pertaining to California
cleaned_wage = cleaned_wage[cleaned_wage['AREA_TITLE'] == 'California']
#Drop NA Values
cleaned_wage = cleaned_wage.dropna()


# In[ ]:


# Visually assess that the histogram values lie within an expected range
#(no unexpected values)
cleaned_wage['H_MEAN'].plot.hist(bins=12, alpha=0.5);


# ## Programmatic Asserts

# In[ ]:


print(cleaned_pums.info())


# In[ ]:


#For PUMS dataset: Check that column data types are now accurate.
assert cleaned_pums.WRK.dtype == 'object'
assert cleaned_pums.SEX.dtype == 'object'
assert cleaned_pums.SOCP.dtype == 'object'


# In[ ]:


#For OEWS dataset: Check that the column data type is now accurate.
assert cleaned_wage.H_MEAN.dtype == 'float'


# In[ ]:


#For PUMS dataset: Check programmatically that number of NA values is 0
assert cleaned_pums.isnull().sum().sum() == 0


# In[ ]:


#For OEWS dataset: Check programmatically that number of NA values is 0
assert cleaned_wage.isnull().sum().sum() == 0


# In[ ]:


assert (cleaned_wage.H_MEAN <= 150).all()


# In[ ]:





# In[ ]:





# In[ ]:




