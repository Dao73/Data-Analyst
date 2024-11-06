#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('outliers_data.csv')
df.head()


# In[2]:


df.describe()


# In[3]:


df.Age.sort_values()


# ## Identifying outliers when we know the range

# In[4]:


df.loc[(df['Age'] < 11)]


# In[5]:


df.loc[(df['Age'] > 18)]


# ## Identify outliers using standard deviation

# In[6]:


summaries = df.describe().loc[['mean', 'std']]
summaries


# In[7]:


upper_bound = summaries['Age']['mean'] + summaries['Age']['std'] 
lower_bound = summaries['Age']['mean'] - summaries['Age']['std'] 


# In[8]:


upper_bound


# In[9]:


lower_bound


# In[10]:


violating_rows = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
violating_rows


# ## Remove outliers entirely from the dataset

# In[11]:


outliers_index = violating_rows.index
outliers_index


# In[12]:


newdf = df.drop(index=outliers_index)
newdf.describe()


# In[13]:


df.describe()


# ## Drop method with `inplace = True`

# In[14]:


df.drop(index=outliers_index, inplace=True)
df


# In[15]:


df.describe()


# In[ ]:





# In[ ]:




