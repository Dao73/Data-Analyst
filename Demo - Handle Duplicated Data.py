#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import pandas and numpy
import pandas as pd
import numpy as np

#Load small test scores dataframe
test_scores = pd.read_csv('test_scores.csv')

#Make a copy of the dataframe
clean_scores = test_scores.copy()
clean_scores.head()


# In[6]:


if_duplicated = clean_scores.duplicated(['Name', 'Age'])
if_duplicated 


# ## Get duplicated rows

# In[7]:


#Access the duplicated rows for duplicates in the Name and Age column
duplicate_rows = clean_scores.loc[clean_scores.duplicated(['Name', 'Age'])]
duplicate_rows


# In[8]:


# all duplicated rows for Amy Linn
Amy = clean_scores.loc[clean_scores['Name'] == 'Amy Linn']
Amy


# ## Gather information around duplicated rows

# In[9]:


#Get the count of duplicated rows
clean_scores.duplicated(['Name', 'Age']).sum()


# In[10]:


#Visually inspect the dataframe for any trends in the duplicates
#Are we seeing duplicate rows only for students who are 15 years-old?
clean_scores


# ## Determine which duplicated row to remove

# In[11]:


# Duplicated rows with some diffrent values
Amy = clean_scores.loc[clean_scores['Name'] == 'Amy Linn']
Amy


# Steps to potentially remediate:
# 
# 1. Check with data providers to confirm the data accuracy
# 2. Remove duplicated data if it is incorrect or keep the duplicated data if it is correct.

# In[12]:


#Load a dataframe where duplicate scores on Test A are wrong
#But all scores (includng duplicate ones) on Test B are correct.
multi_test_scores = pd.read_csv('multiple_test_scores.csv')
multi_test_scores


# In[13]:


#Access the duplicated rows for duplicates in the Name and Age column
multi_test_scores[multi_test_scores.duplicated(['Name', 'Age'])]


# Steps to potentially remediate:
# 
# 1. Check with data providers, see an example response below:
# - Duplicated students’ data in “Test A score” is incorrect and incorrect rows should be removed 
# - Duplicated students’ data in “Test B score” is correct and should be kept
# 2. Mark the incorrect duplicate values for “Test A score” as NaNs; Or simply data structure by creating a separate table for the repeated values in Test B Score.

# ## Resolve the duplicated rows

# In[14]:


# Remove the values where the duplicates are in the Name and Age columns
#By default, drop_duplicates() keep the first occurrence
remove_dup = clean_scores.drop_duplicates(subset=['Name', 'Age'])
remove_dup


# In[15]:


#The following defines keep=last, keeping the last occurrence
clean_scores.drop_duplicates(subset=['Name', 'Age'], keep='last')


# In[16]:


remove_dup.duplicated(['Name', 'Age']).sum()


# ## How to drop rows that are neither the first or last occurrence

# In[17]:


# Duplicated rows with some diffrent values
Amy = clean_scores.loc[clean_scores['Name'] == 'Amy Linn']
Amy


# In[18]:


row_drop_example = Amy.drop([5])
row_drop_example


# ## How to convert duplicate values to NaNs

# In[19]:


#Access the index of the duplicated rows for duplicates
dupe_index = multi_test_scores[multi_test_scores.duplicated(['Name', 'Age'])].index
dupe_index


# In[20]:


#Set duplicated values in Test A Score column to NANs
multi_test_scores.loc[dupe_index, 'Test A Score'] = np.nan


# In[21]:


#Visually inspect to confirm the operation worked
multi_test_scores


# In[ ]:





# In[ ]:





# In[ ]:




