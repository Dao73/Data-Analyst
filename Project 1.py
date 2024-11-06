#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - FBI Gun Data
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > **Dataset 1** : nics-firearm-background-checks.csv : https://github.com/BuzzFeedNews/nics-firearm-background-checks/blob/master/data/nics-firearm-background-checks.csv
# 
# > **Dataset 2** : u.s.-census-data :https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a0a554c_u.s.-census-data/u.s.-census-data.csv
# 
# > The data comes from the FBI's National Instant Criminal Background Check System. The NICS is used by to determine whether a prospective buyer is eligible to buy firearms or explosives.
# Gun shops call into this system to ensure that each customer does not have a criminal record or isn’t otherwise ineligible to make a purchase.
# The data has been supplemented with state level data from census.gov(opens in a new tab).
# The NICS data contains the number of firearm checks by month, state, and type.
# The U.S. census data contains several variables at the state level. Most variables just have one data point per state (2016), but a few have data for more than one year.
# 
# 
# ### Questions for Analysis
# >**Question 1**: What census data is most associated with high gun per capita?
# 
# >**Question 2**: Which states have had the highest growth in gun registrations?
# 
# >**Question 3**: What is the overall trend of gun purchases?

# In[47]:


#Import statements for all of the packages
   
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# <a id='wrangling'></a>
# ## Data Wrangling

# In[78]:


# Loading datasets
census_df = pd.read_csv(r"C:\Users\quent\Downloads\u.s.-census-data.csv")
nics_df = pd.read_csv(r"C:\Users\quent\Downloads\nics-firearm-background-checks.csv")



# In[79]:


census_df.shape


# In[80]:


nics_df.shape


# In[81]:


census_df.info()


# In[82]:


nics_df.info()


# <a id='wrangling'></a>
# ## Cleaning census_df

# In[97]:


# ------------------ Cleaning the census dataset ------------------ #
# 1. Delete columns with more than 50% missing values
threshold = 0.5 * len(census_df)
census_df = census_df.dropna(thresh=threshold, axis=1)


# In[98]:


#2. Delete rows with more than 50% missing values
census_df = census_df.dropna(thresh=0.5 * len(census_df.columns), axis=0)


# In[99]:


#3. Convert numeric columns (with commas and percentages) to number format
def convert_to_numeric(value):
    if isinstance(value, str):
        value = value.replace(',', '').replace('%', '')
        return pd.to_numeric(value, errors='coerce')
    return value


# In[100]:


# Apply the conversion to all report columns
for column in census_df.columns[2:]:
    census_df[column] = census_df[column].apply(convert_to_numeric)


# <a id='wrangling'></a>
# ## Cleaning ncis_df

# In[101]:


# ------------------ Cleaning the background check dataset ------------------ #
# 1. Replace missing values with 0 in numeric columns
nics_df.fillna(0, inplace=True)


# In[102]:


#2. Convert "month" column to datetime format for temporal analysis
nics_df['month'] = pd.to_datetime(nics_df['month'], errors='coerce')


# In[103]:


# Résults
print("Dataset de census clean :")
print(census_df.head())
print("\nDataset ncis clean :")
print(nics_df.head())


# ## Exploratory Data Analysis

# <a id='wrangling'></a>
# ## Descriptive statistics for census 

# In[104]:


census_df.describe()


# <a id='wrangling'></a>
# ## Descriptive statistics for nics_df

# In[105]:


nics_df.describe()


# ### Research Question 1: What census data is most associated with high gun per capital ?

# In[134]:


# ------------------ Data Preparation and Cleaning ------------------ #

# 1. Calculate the average monthly firearm checks per state as a proxy for gun ownership rate
firearm_rate_df = nics_df.groupby("state")["totals"].mean().reset_index()
firearm_rate_df.rename(columns={"totals": "average_monthly_firearm_checks"}, inplace=True)


# In[135]:


# 2. Extract 2016 population estimates by filtering the "Fact" column
population_2016_row = census_df[census_df["Fact"] == "Population estimates, July 1, 2016,  (V2016)"]
population_2016_df = population_2016_row.T
population_2016_df.columns = ["population_estimate_2016"]
population_2016_df = population_2016_df.drop(index="Fact").reset_index()
population_2016_df.columns = ["state", "population_estimate_2016"]


# In[136]:


# Convert the population estimates column to numeric (removing commas if any)
population_2016_df["population_estimate_2016"] = (
    population_2016_df["population_estimate_2016"]
    .replace({',': ''}, regex=True)
    .astype(float)
)

# 3. Merge both datasets on the "state" column to match gun check data with population estimates
merged_df = pd.merge(firearm_rate_df, population_2016_df, on="state", how="inner")


# In[137]:


# 4. Calculate firearm checks per capita by dividing the monthly checks by the population estimate for each state
merged_df["firearm_checks_per_capita"] = (
    merged_df["average_monthly_firearm_checks"] / merged_df["population_estimate_2016"]
)


# In[138]:


# ------------------ Correlation Analysis and Visualization ------------------ #

# Select only the numeric columns for correlation analysis
numeric_df = merged_df.select_dtypes(include=[np.number])

# Visualize the relationships between firearm checks per capita and other demographic features
# Correlation heatmap
plt.figure(figsize=(12, 10))
plt.title("Correlation Heatmap between Demographic Characteristics and Firearm Checks per Capita")
plt.imshow(numeric_df.corr(), cmap="coolwarm", interpolation="none")
plt.colorbar(label="Correlation Coefficient")
plt.xticks(range(len(numeric_df.columns)), numeric_df.columns, rotation=90)
plt.yticks(range(len(numeric_df.columns)), numeric_df.columns)
plt.show()


# ### Research Question 2: Which states have had the highest growth in gun registrations?
# 

# In[139]:


# Convert the 'month' column to datetime format
nics_df['month'] = pd.to_datetime(nics_df['month'])


# In[140]:


# Calculate the first and last monthly total checks for each state
# Group by 'state' and get the first and last entry for each state
growth_df = nics_df.groupby('state').agg(
    first_total=('totals', 'first'),
    last_total=('totals', 'last')
).reset_index()


# In[141]:


# Calculate the growth in firearm checks as both absolute and relative changes
growth_df['absolute_growth'] = growth_df['last_total'] - growth_df['first_total']
growth_df['relative_growth'] = (growth_df['absolute_growth'] / growth_df['first_total']) * 100


# In[143]:


# Sort by the highest growth rates
growth_df = growth_df.sort_values(by='relative_growth', ascending=False)


# In[144]:


# Display the top states with the highest growth
print("Top states with the highest growth in firearm checks:")
print(growth_df.head(10))


# ### Research Question 3: What is the overall trend of gun purchases?
# 

# In[146]:


# Convert the 'month' column to datetime format
nics_df['month'] = pd.to_datetime(nics_df['month'])


# In[147]:


# Aggregate data by month to get the total checks for each month
monthly_trend_df = nics_df.groupby('month')['totals'].sum().reset_index()


# In[148]:


# Calculate a 12-month rolling mean to smooth the trend (1-year average)
monthly_trend_df['rolling_mean'] = monthly_trend_df['totals'].rolling(window=12).mean()


# In[149]:


# Plot the trend over time
plt.figure(figsize=(12, 6))
plt.plot(monthly_trend_df['month'], monthly_trend_df['totals'], label='Monthly Total Checks', alpha=0.7)
plt.plot(monthly_trend_df['month'], monthly_trend_df['rolling_mean'], label='12-Month Rolling Average', color='orange', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Total Firearm Checks')
plt.title('Trend of Firearm Purchases Over Time')
plt.legend()
plt.show()


# <a id='conclusions'></a>
# ## Conclusions

# **Answer Question 1:**
# 
# Conclusion based on observed correlations: Number of checks and population: There appears to be a strong correlation between the average number of background checks for firearms and the population of a state. This means that more populous states tend to have a higher number of monthly checks, which can be expected given that larger populations potentially generate a higher demand for gun purchases.
# 
# Per capita check rate: The per capita rate of gun checks (checks balanced by population) has a weaker correlation with the total population of the state. This indicates that the per capita check rate is not directly influenced by population size. Other state-specific factors, such as local laws, culture, and safety concerns, may play a more important role.
# 
# Limitations and recommendations: Cautious interpretation: The heatmap only shows correlations without significance tests. These associations do not necessarily demonstrate a causal relationship and may be due to state-specific contextual factors.
# Recommended additional steps: Further statistical testing (such as linear regressions and significance tests) is needed to confirm whether these associations are significant and to explore other factors that may influence background check rates.

# **Answers Question 2:**
# 
# The states with the highest growth in gun registrations are:
# 
# - District of Columbia: No initial checks, increasing to 929 checks – infinite growth (indefinite in percentage).
# - Virgin Islands: No initial checks, increasing to 191 checks – infinite growth.
# - Guam: No initial checks, increasing to 233 checks – infinite growth.
# - Mariana Islands: No initial checks, increasing to 16 checks – infinite growth.
# - Illinois: From 22 to 222,356 checks – relative growth of 1,010,609%.
# - Pennsylvania: From 17 to 82,073 checks – relative growth of 482,682%.
# - South Carolina: From 6 to 26,580 checks – relative growth of 442,900%.
# - Puerto Rico: From 2 to 5,020 checks – 250,900% relative growth.
# - Virginia: From 24 to 39,154 checks – 163,041% relative growth.
# - Georgia: From 62 to 38,783 checks – 62,453% relative growth.
# 
# Limitation: Territories such as the District of Columbia, Virgin Islands, Guam, and Mariana Islands have infinite relative growth because they had no initial checks recorded.

# **Answer Question 3:**
# 
# Gun Purchase Trend Conclusion:
# 
# The line shows a gradual increase in background checks for gun purchases over the years, with several sharp spikes. The most notable spikes appear to occur between 2012 and 2020, with a sharp increase around 2020. This can be attributed to periods of political, social, or major events that pushed individuals to purchase more guns. The 12-month moving average line (in orange) shows the underlying trend by smoothing out seasonal variations and clearly shows this increase followed by a decline after 2020.
# 
# Limitations of the Analysis: Effect of Seasonal Variations: The trend shows seasonal fluctuations (consistent increases around the same periods each year). Further analysis of specific seasons or months may be needed to understand the impact of times of year on gun purchases.
# 
# Influence of specific events: The curve shows sudden spikes that could be associated with specific events (such as elections or social crises). Without identifying these events, it is difficult to interpret the exact reasons for the one-off increases.
# 
# Lack of geographic segmentation: The curve represents checks at the national level. Local or regional trends could reveal additional information.
# 
# Pandemic impact: The period around 2020, marked by a high spike followed by a sharp decline, could be linked to the COVID-19 pandemic, but this hypothesis requires additional analysis to confirm the causes.
# 
# In conclusion, this trend shows a notable growth in background checks for gun purchases, with increases linked to potential events. However, a more detailed analysis would be necessary to directly link specific causes to these fluctuations.

# **Overall Conclusion**
# 
# Analysis of firearm registrations in the United States reveals several important trends and insights:
# 
# Overall growth in firearm registrations: Over time, background checks for firearm purchases have shown an overall increase, with notable spikes during periods of sociopolitical tension and significant events. Growth is not uniform across states, with some territories and states experiencing dramatic increases, in part due to low initial starting points.
# 
# Demographic factors associated with gun rates per capita: Examining correlations between demographic characteristics and gun rates per capita, we observe that certain factors, such as population size and other socioeconomic indicators, may be related to changes in gun rates. However, these associations require further analysis to confirm causal relationships.
# 
# Trend in demand for weapons: The time trend highlights seasonal cycles and irregular peaks related to crises or national events. For example, a sharp increase was observed around 2020, likely influenced by the COVID-19 pandemic and the uncertainty it created.
# 
# **Final conclusion**
# 
# The United States is experiencing a growing trend in arms purchases, driven by both socio-economic factors and specific events. This analysis reveals a fluctuating demand, with a high sensitivity to periods of uncertainty. However, the limitations of the analysis, including the lack of detailed regional segmentation and consideration of specific events, indicate that further study is needed to fully understand the motivations and social impacts of this increase in arms purchases. This trend highlights the complexity of the arms issue and the social and political factors that influence purchasing decisions.
