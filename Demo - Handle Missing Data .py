#!/usr/bin/env python
# coding: utf-8

# # How to deal with missing data

# In[1]:


import pandas as pd
import numpy as np


# ## Dealing with missing data in different formats

# In[2]:


# read dataframe
df = pd.read_csv('assessment.csv')


# In[3]:


#Drop a rows
df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.sample(5, random_state = 70)


# In[7]:


df.loc[df['assessment score 2'].isin(['#'])]


# In[8]:


df['assessment score 2'] = df['assessment score 2'].replace({'#': np.nan})
df


# In[9]:


df.loc[df['assessment score 2'].isin(['#'])]


# In[10]:


df.isna().sum()


# ## Option 1: drop rows

# In[11]:


cleaned_df = df.dropna()
cleaned_df.describe()


# In[12]:


cleaned_df.isna().sum()


# ## Option 2: drop columns

# In[13]:


problem_df = pd.read_csv("assessment_problem.csv")
problem_df.head()


# In[14]:


problem_df.isna().sum()


# In[15]:


problem_df_cleaned = problem_df.drop('assessment score 2', axis=1)
problem_df_cleaned.head()


# In[16]:


problem_df_cleaned.isna().sum()


# ## Option 3: impute NANs

# In[17]:


df = pd.read_csv('assessment.csv')
# repace # to nan
df['assessment score 2'] = df['assessment score 2'].replace({'#': np.nan})
# convert 'assessment score 2' data type from object to float
df['assessment score 2'] = df['assessment score 2'].astype(float)


# In[18]:


df.isna().sum()


# In[19]:


cleaned_df = df.fillna(df.mean())


# In[20]:


cleaned_df.isna().sum()


# In[21]:


t_df = df.copy()
t_df['assessment score 2'] = t_df['assessment score 2'].fillna(
        t_df['assessment score 2'].mean())


# In[22]:


t_df.isna().sum()


# In[23]:


# A quick check on the stats after imputing the data
cleaned_df.describe()


# In[24]:


df.describe()


# ## Option 4: create bins

# In[25]:


df['assessment score 1'] = pd.cut(df['assessment score 1'], 4)
df['assessment score 2'] = pd.cut(df['assessment score 2'], 4)


# In[26]:


df['assessment score 2'].value_counts()


# In[27]:


df[df.isnull().any(axis=1)]


# In[ ]:





# In[ ]:





# In[ ]:




