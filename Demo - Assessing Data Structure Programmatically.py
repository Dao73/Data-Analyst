#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import pandas
import pandas as pd

#Load data tables from clinical trial data
patients = pd.read_csv('patients.csv')
treatments = pd.read_csv('treatments.csv')
adverse_reactions = pd.read_csv('adverse_reactions.csv')


# ## Helpful techniques for visual + programmatic assessment

# In[2]:


#Visually inspect the adverse reactions table
adverse_reactions.head()


# In[3]:


#Visually inspect the treatments table
treatments.head()


# In[4]:


#Visually inspect the info() results on treatments
treatments.info()


# In[5]:


#Visually inspect the info() results on adverse_reactions
adverse_reactions.info()


# In[6]:


#Get dimensionality of dataframe
adverse_reactions.shape


# In[7]:


#Get all of the column labels in our dataset programmatically.
adverse_reactions.columns


# In[8]:


#Get the index of the data
adverse_reactions.index


# ## A single observational unit is stored in multiple tables.

# In[9]:


#Revisit adverse reactions table for visual inspection
adverse_reactions.head()


# In[10]:


#Revisit treatments table for visual inspection
treatments.head()


# ## Variables are stored in both rows and columns.

# In[11]:


#We see variables are stored in both rows and columns with auralin and novodra columns
treatments[["auralin","novodra"]]


# In[12]:


#Programmatic assessment: Get rows where BOTH auralin and novodra
#have values at the same time. There should be no rows retured, since a patient
#will not take both drugs at the same time. We can see that's the case below.

treatments[((treatments['auralin'] != '-') & (treatments['novodra'] != '-'))]


# With this confirmation, we could proceed during the cleaning stage to simplify our data structure to solve this issue by creating three columns - for the treatment specifying auralin/novodra, the start dose, and the end dose.

# ## Multiple variables being stored in one column.

# In[13]:


#Look at patients dataframe - visually inspect the first few rows
patients.head()


# In[14]:


#Look at patients dataframe value_counts to inspect validity
#Do the smushed up values all follow the same format?
#304-438-2648SandraCTaylor@dayrep.com confirms this isn't the case.

patients['contact'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:




