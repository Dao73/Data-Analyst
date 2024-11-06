#!/usr/bin/env python
# coding: utf-8

# We'll connect to a SQLite database using SQLAlchemy, a database toolkit for Python.

# In[1]:


import pandas as pd
from sqlalchemy import create_engine, text


# In[2]:


df = pd.read_csv('bestofrt_master.csv')


# In[3]:


df.head(3)


# ### 1. Connect to a database

# In[4]:


# Create SQLAlchemy Engine and empty bestofrt database
# bestofrt.db will not show up in the Jupyter Notebook dashboard yet
engine = create_engine('sqlite:///bestofrt.db')


# ### 2. Store pandas DataFrame in database
# Store the data in the cleaned master dataset (bestofrt_master) in that database.

# In[5]:


# Store cleaned master DataFrame ('df') in a table called rt_table in bestofrt.db
# bestofrt.db will be visible now in the Jupyter Notebook dashboard
df.to_sql('rt_table', engine, index=False, if_exists='replace')


# ### 3. Read database data into a pandas DataFrame
# Read the brand new data in that database back into a pandas DataFrame.

# In[6]:


df_gather = pd.read_sql(sql=text('SELECT * FROM rt_table'), con=engine.connect())


# In[7]:


df_gather.head(3)


# In[ ]:





# In[ ]:




