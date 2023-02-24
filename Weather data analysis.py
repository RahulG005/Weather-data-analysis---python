#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\Rahul\OneDrive\Desktop\dataset\1. Weather Data.csv")


# In[3]:


data


# In[4]:


#Shows the top 7 rows
data.head(7)


# In[5]:


#Total number of rows and columns
data.shape


# In[6]:


#Provides index to dataframe
data.index


# In[7]:


#Name of each columns
data.columns


# In[8]:


#shows the datatypes of each column
data.dtypes


# In[9]:


#show unique values present in weather column
data['Weather'].unique()


# In[10]:


#shows total unique values in each column
data.nunique()


# In[11]:


#checking if any column has any null values
data.count()


# In[12]:


#Shows the unique values of windspeed
data['Wind Speed_km/h'].unique()


# In[13]:


#Show the values with Clear weather only
data[data.Weather == 'Clear']


# In[14]:


#show the nummber of times when the wind speed was 4 km/h
data[data['Wind Speed_km/h']  == 4]


# In[15]:


#checking if any column has any null values
data.isnull().sum()


# In[16]:


#Rename the column Weather to weather condition
data.rename(columns = {'Weather':'Weather condition'}, inplace = True)


# In[17]:


data.head()


# In[18]:


#show the mean value of Visibility
data['Visibility_km'].mean()


# In[19]:


#show the standard deviation of Pressure
data['Press_kPa'].std()


# In[20]:


#Show the variance of Relative humidity
data['Rel Hum_%'].var()


# In[30]:


#find all instances when 'snow' was recorded
data[data['Weather condition'] == 'Snow']


# In[39]:


#find all instances when wind speed is above 24 and Visibility is 25
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[40]:


#Show the mean value of each column against each weather condition
data.groupby('Weather condition').mean()


# In[42]:





# In[ ]:




