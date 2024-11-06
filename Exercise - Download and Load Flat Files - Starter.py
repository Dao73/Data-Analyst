#!/usr/bin/env python
# coding: utf-8

# # Exercise - Download and Load Flat Files - STARTER

# In this exercise, you will apply your skills to programmatically unzip a .zip folder and gather data from a .tsv and .csv file into pandas dataframes.

# In[1]:


#DO NOT MODIFY - imports
import pandas as pd
import zipfile


# ## 1. Unzip .zip file programmatically

# We will load data from the Rotten Tomatoes Top 100 Movies of All Time list along with some short reviews. We've pre-gathered this dataset and stored them in the `reviews.zip` file.
# 
# For the first part of this exercise, unzip the `reviews.zip` in read mode using a context manager.

# In[2]:


import zipfile

# Define the path to the zip file
zip_file_path = 'reviews.zip'

# Unzip the file using a context manager
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()  # This will extract files to the current directory


# ## 2. Load the TSV file
# 
# The `reviews` folder contains a `bestofrt.tsv` file which includes the following columns:
# 
# - `ranking`: Rank of the movie
# - `critic_score`: Rating
# - `title`: Title of the movie
# - `number_of_critic_ratings`: Number of reviews
# 
# The data has 101 rows.
# 
# Now, load the .tsv file into a pandas dataframe while:
# 1. Specifying the data types of the individual columns
# 2. Denoting the `ranking` column as the index.

# In[4]:


import pandas as pd

# Define the file path
file_path = 'reviews/bestofrt.tsv'

# Load the .tsv file into a DataFrame with specified data types
df = pd.read_csv(
    file_path, 
    sep='\t',  # Specify tab separator for .tsv files
    dtype={
        'ranking': 'int',                 # Rank of the movie as integer
        'critic_score': 'float',          # Rating as float
        'title': 'string',                # Title as string
        'number_of_critic_ratings': 'int' # Number of reviews as integer
    },
    index_col='ranking'  # Set the 'ranking' column as the index
)

# Display the first few rows to confirm loading
df.head()


# In[5]:


# Display the first few rows to confirm loading
df.head()


# ## 3. Load the CSV file

# We've also included a review dataset, `reviews.csv`, in the folder, consisting of synthetic data around individual viewers who wrote short reviews and provided ratings corresponding to the movies.
# 
# Now load the .csv file into a dataframe **while** doing the following:
# - Marketing the 'Not Collected' values as NaNs
# - Defining the header as the first (0th) row of the .csv

# In[6]:


import pandas as pd
import numpy as np

# Define the file path
file_path = 'reviews/reviews.csv'

# Load the .csv file into a DataFrame
df_reviews = pd.read_csv(
    file_path,
    header=0,                 # Define the header as the first row (0th row)
    na_values='Not Collected' # Mark 'Not Collected' as NaN
)

# Display the DataFrame
df_reviews


# In[ ]:


#FILL IN - show the dataframe

