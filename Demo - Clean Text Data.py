#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

txt_data = pd.read_csv('text_data.csv')


# ## Normalize data

# In[2]:


txt_data.head()


# In[3]:


txt_data['post'] = txt_data['post'].str.capitalize()
txt_data['post']


# In[4]:


txt_data["post"] = txt_data['post'].str.replace('[^\w\s]','')
txt_data["post"]


# In[5]:


txt_data.loc[txt_data['post'].str.contains('data science'), 
             'Topic'] = 'data science'
txt_data.head()


# ## Tokenize data
# Note: nltk is not installed in the workspace so the following code won't excute successfully

# In[6]:


import nltk
txt_data["token"] = txt_data["post"].apply(nltk.word_tokenize)
txt_data


# ## Vectorize data

# In[7]:


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

words_matrix = vectorizer.fit_transform(txt_data["post"].values)
words_matrix.toarray()


# In[8]:


counts = pd.DataFrame(words_matrix.toarray(),
                      columns=vectorizer.get_feature_names_out())
counts


# In[9]:


print(vectorizer.vocabulary_)


# In[ ]:





# In[ ]:





# In[ ]:




