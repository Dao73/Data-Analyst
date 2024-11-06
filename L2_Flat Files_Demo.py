#!/usr/bin/env python
# coding: utf-8

# # Open a .tsv file

# We will use a synthetic dataset on individuals taking intelligence and emotional quotient tests. 
# 
# The data consists of three variables: The rank of a test-taker, their name, and their test type (IQ and EQ).

# In[1]:


import pandas as pd


# ## Using `open`

# In[2]:


tiny_tsv_list = []
with open("tiny_tsv.tsv") as tsv_file:
    for line in tsv_file:
        tiny_tsv_list.append(line.rstrip('\n').split('\t'))

tiny_tsv_list


# ## Using `pandas`

# In[3]:


import pandas as pd

df_tsv = pd.read_csv('tiny_tsv.tsv', sep='\t')
df_tsv


# # Open a .csv file from a zipped archive

# Now let's open the same data stored in a zipped .csv file.

# ## OPTION 1 using `pandas`

# In[4]:


#OPTION 1
direct_df = pd.read_csv('tiny_csv.zip')
direct_df


# In[5]:


#OPTION 1
#Fail to unzip multiple files
pd.read_csv('multi_tiny.zip')


# ## OPTION 2 using `zipfile`

# In[ ]:


#OPTION 2
import zipfile

with zipfile.ZipFile("tiny_csv.zip","r") as zip_ref:
    zip_ref.extractall("tiny_csv/")
    
indirect_df = pd.read_csv('tiny_csv/tiny_csv.csv')
indirect_df


# In[ ]:


#Proceed with Option 2
#Now, do the following in one command:
#1. Define the seperator or delimiter as semicolon
#2. Defining the header as the first (0th) row of the .csv
#3. Specifying the data types of the individual columns
#4. Denoting the rank column as the index.
#5. Marketing the 'No Test Taken' values as NaNs 
    
indirect_df = pd.read_csv('tiny_csv/tiny_csv.csv', 
                        sep=';', 
                        header=0,                        
                        dtype={'rank':'int',
                              'name':'string',
                             'test_type':'string'},
                        index_col='rank',
                        na_values='No Test Taken')
indirect_df


# In[ ]:





# In[ ]:





# In[ ]:




