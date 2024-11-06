#!/usr/bin/env python
# coding: utf-8

# # Assessing Data Quality Programmatically

# Context: Dataset is synthetic phase two clinical trial dataset of 350 patients for a new innovative oral insulin called Auralin - a proprietary capsule that can solve a stomach lining problem.

# In[1]:


#Import pandas
import pandas as pd

#Load in datasets
patients = pd.read_csv('patients.csv')
treatments = pd.read_csv('treatments.csv')


# ## Data Quality issues with the treatments table

# In[2]:


#View the first few rows of the treatments dataframe
treatments.head()


# In[3]:


#View the last few rows of the treatments dataframe
treatments.tail()


# In[5]:


#Returns one random entry from the datframe 
#for non-directed programmatic assessment
treatments.sample()


# In[8]:


treatments.sample(5) #returns 5 entries


# In[9]:


#Returns 5 entries with a random state 2
treatments.sample(5, random_state=2) 


# **1. Completeness**

# In[10]:


#Get the information of the treatments dataframe using .info()
treatments.info()


# *Interpretation:* Looking at the summary of the treatments DataFrame returned by .info we can see that there are only 171 hba1c_change entries while there are 280 entries for the other columns.

# **2. Validity**

# In[11]:


#Get the data types of the different variables in the dataframe
treatments.dtypes


# *Interpretation:* For the auralin and novodra columns, their data type is object.  Ideally, the values for these two columns would be formatted as integers or the float64 data type to make it easier to access this information.

# **3. Accuracy**

# In[12]:


#Describe the dataframe using .describe()
treatments.describe()


# *Interpretation*: 0.99 is a big max value for the hba1c_change variable. 
# 
# If we look below at our visual assessment of the treatments table, we'll see that this hba1c_change for this 0.97 entry for Elliot Richardson is calculated incorrectly. 7.56-7.09=0.47, not 0.97, indicating an accuracy issue.

# In[13]:


treatments.head()


# **4. Validity**

# In[14]:


#Identify null values in our dataset
#This value should be not null, 
#since there are hyphens indicating missing data
sum(treatments.auralin.isnull())


# In[15]:


#Identify null values in our dataset
#This value should be not null, 
#since there are hyphens indicating missing data
sum(treatments.novodra.isnull())


# *Interpretation*: The dashes aren't picked up as null or non-values for the `auralin` and `novodra` columns, which can be problematic when doing calculations on the data.  Misrepresenting missing values is a validity issue.

# ## Data quality issues with the patients table

# **5. Consistency**

# In[16]:


#Use the describe() function on the patients dataframe
patients.describe()


# *Interpretation*: The minimum weight is 48 pounds, which is very low. The average weight seems to be about 173 lbs. 

# In[17]:


#Use sort_values() method to sort values
#for the weight column from low to high weight.
patients.weight.sort_values()


# Why is the minimum weight value 48.8? Let's look at the corresponding row.

# In[18]:


#Identify the row where the weight column value is at is min.
patients[patients.weight==patients.weight.min()]


# Let’s check this strange anomaly by making an assumption - maybe for this patient, the unit is incorrect and it is logged in kilograms instead of pounds. Let's test this by doing the calculation ourselves.

# In[19]:


#Conversation factor from kilograms to pounds is 2.20462
#Get the weight of the patient
weight_lbs = patients[patients.surname == 'Zaitseva'].weight * 2.20462
#Get the height of the patient
height_in = patients[patients.surname == 'Zaitseva'].height
#Calculate the BMI using the equation 703 * weight/(height^2)
bmi_check = 703  *weight_lbs / ( height_in*  height_in )
bmi_check


# In[20]:


#Get the patients' reported BMI
patients[patients.surname == 'Zaitseva'].bmi


# *Interpretation:* The BMI we calculated comes up to 19.055, which is equivalent to the BMI reported in the data. This means this anomaly of the patient’s weight was actually recorded in kilograms whereas the rest of the dataset is indicating weight in pounds. This is a consistency issue with the unit measurement of the data. 

# **6. Uniqueness + Validity**

# In[21]:


#Get the number of unique values in our surname column
patients.surname.value_counts()


# In[22]:


#Get the number of unique values in our address column
patients.address.value_counts()


# In[23]:


#Use .duplicated() on the surname and address columns to get the rows
patients[patients.duplicated(subset=['surname','address'])]


# *Interpretation:* We find that there are several John Doe's that live at 123 Main Street New York, New York, ZIP Code 12345 with the email johndoe@email.com. 
# 
# This is a uniqueness issue, because we have multiple duplicated rows in the dataset, and a validity issue because this data doesn't conform to the defined schema of one record per patient.

# In[ ]:





# In[ ]:




