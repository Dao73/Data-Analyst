#!/usr/bin/env python
# coding: utf-8

# # Scikit-learn Pre-processing

# In[1]:


import sklearn
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer

from sklearn import set_config

#Sets output of transform and fit_transform to pandas dataframe output.
set_config(transform_output = "pandas")


# ## Scaling

# In[2]:


tiny_data = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])

scaler = StandardScaler().fit(tiny_data)
scaler


# In[3]:


scaler.mean_


# In[4]:


scaler.scale_


# In[5]:


X_scaled = scaler.transform(tiny_data)


# In[6]:


X_scaled.mean()


# In[7]:


X_scaled.std()


# ## Ordinal Encoding

# In[8]:


# example of a ordinal encoding
from numpy import asarray


# In[9]:


# define data
data = asarray([['data'], ['wrangling'], ['rocks']])
print(data)


# In[10]:


# define ordinal encoding
encoder = OrdinalEncoder()
# transform data
encoder.fit_transform(data)


# ## One Hot Encoding

# In[11]:


# define one hot encoding
encoder = OneHotEncoder(sparse_output=False)
# transform data
encoder.fit_transform(data)


# ## Imputing missing values

# In[12]:


from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True, parser='auto')

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)


# In[13]:


X.head()


# In[14]:


y_train.head()


# In[15]:


X.info()


# In[16]:


missing = X_test.isnull().sum()
missing = missing[missing > 0].sort_values(ascending = False)


# In[17]:


missing


# In[18]:


simple_imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
simple_imputed = simple_imp.fit_transform(X_test[['age', 'body']])


# In[19]:


#Replace the age and body columns in the original X_Test dataframe
#with the imputed values
X_test[['age', 'body']] = simple_imputed

#Repeat the above code to get number of NA values- note how the 'age' and 
#'body' columns disappear
missing = X_test.isnull().sum()
missing = missing[missing > 0].sort_values(ascending = False)
missing


# ## Putting it all together

# In[20]:


X_train.head()


# In[21]:


from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# Here we use `StandardScaler` for continuous variables; 
# then we impute for missing data (check the documentation for the imputation method)
# We use `OneHotEncoder` for categorical variables
# NOTE: we are using a subset of the features (not all the columns)

ct = make_column_transformer((make_pipeline(SimpleImputer(),
                                            StandardScaler()), ["age", "fare"]),
                             (OneHotEncoder(sparse_output=False), ["embarked", "sex", "pclass"]), 
                             verbose_feature_names_out=False)

# Note: click on pipeline elements to see more details
clf = make_pipeline(ct, LogisticRegression())
clf


# In[22]:


clf.fit(X_train, y_train)
clf.score(X_train, y_train)


# In[23]:


# Let's remove the last step in the pipeline (which is LogisticRegression()) & transform the X_test data
clf[:-1].transform(X_test)


# In[ ]:





# In[ ]:





# In[ ]:




