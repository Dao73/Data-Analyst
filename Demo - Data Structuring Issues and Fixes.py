#!/usr/bin/env python
# coding: utf-8

# # Demo - Data Structuring Issues and Fixes

# In[1]:


#Import pandas as pd
import pandas as pd


# In[2]:


#Read all sheets in the Excel file
example_data = pd.read_excel('data_structuring_demo.xlsx', sheet_name=None)


# ## Unpivoting/Melting

# In[3]:


example1_data = example_data['Unpivot Example']
cleaned_example1 = example1_data.copy()
cleaned_example1


# In[4]:


cleaned_example1 = cleaned_example1.melt(id_vars=['Name'], 
                                         var_name='Binned Score',
                                         value_name='Frequency')
cleaned_example1


# ## Pivoting

# In[5]:


example2_data = example_data['Pivot Example']
example2_data


# In[6]:


example2_data.pivot(index=["Product Classification",
                           "Product"], 
                    columns="Year",
                    values="Revenue")


# ## Transpose

# In[7]:


transpose_ex = example_data['Tranpose Example']
transpose_ex


# In[8]:


transpose_ex.T


# In[9]:


transposed_df = transpose_ex.set_index('ID').T
transposed_df


# ## Merging

# In[10]:


merging_ex_1 = example_data['Merge Example 1']
merging_ex_1


# In[11]:


merging_ex_2 = example_data['Merge Example 2']
merging_ex_2


# In[12]:


merged = pd.merge(merging_ex_1, merging_ex_2)
merged


# ## Appending

# In[13]:


append_ex_1 = example_data['Appending Example 1']
append_ex_1


# In[14]:


append_ex_2 = example_data['Appending Example 2']
append_ex_2


# In[15]:


appended_df = pd.concat([append_ex_1, append_ex_2], ignore_index=True)
appended_df


# In[16]:


#Jumbled up index
pd.concat([append_ex_1, append_ex_2])


# ## Group-by and Aggregation

# In[17]:


groupby_ex = example_data['Groupby-Agg Example']
groupby_ex


# In[18]:


groupby_ex.groupby('date', sort=False)['score'].agg(['sum','mean'])


# ## Bonus: Advanced merging

# In[19]:


import pandas as pd

#Read all sheets in the Excel file
advanced_merge = pd.read_excel('advanced_merge_example.xlsx', sheet_name=None)
adv_merge_1 = advanced_merge['Sheet1']
adv_merge_2 = advanced_merge['Sheet2']


# In[20]:


adv_merge_1


# In[21]:


adv_merge_2


# In[22]:


#Merge the two dataframes using only keys from the right frame
advm_ex = pd.merge(adv_merge_1, adv_merge_2, on=['Movie ID'], how='right')
advm_ex.head()


# In[23]:


#Merge the two dataframes using only keys from the left frame
advm_ex2 = pd.merge(adv_merge_1, adv_merge_2, on=['Movie ID'], how='left')
advm_ex2.head()


# In[24]:


#Merge the two dataframes using the intersection of keys from both frames,
advm_ex3 = pd.merge(adv_merge_1, adv_merge_2, on=['Movie ID'], how='inner')
advm_ex3.head()


# In[ ]:





# In[ ]:





# In[ ]:




