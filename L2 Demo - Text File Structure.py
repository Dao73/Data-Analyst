#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import pandas as pd


# In[2]:


glob.glob('ebert_reviews_2017/*.txt')


# In[3]:


#Create an empty list
text_list = []
#Iterate through files in directory
for ebert_review in glob.glob('ebert_reviews_2017/*.txt'):
    #Open file with UTF-8 encoding
    with open(ebert_review, encoding='utf-8') as file:
        #Read the 1st line
        title = file.readline()[:-1]
        #Read the 2nd line
        review_url = file.readline()[:-1]
        review_text = file.read()
        # Append to list of dictionaries
        text_list.append({'title': title,
                        'review_url': review_url,
                        'review_text': review_text})
#Convert list of dictionaries to Dataframe
df = pd.DataFrame(text_list, columns = ['title', 'review_url', 'review_text'])


# In[4]:


#Print first few rows of the dataframe
df.head()


# In[ ]:





# In[ ]:





# In[ ]:




