#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necesary libraries, abbreviate for quick use later
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns


# In[2]:


# Import data
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# In[3]:


# Start exploratory data analysis using head and size
df.head(10)


# In[4]:


df.size


# In[5]:


# Use describe to get quick calculations about the data set.
df.describe()


# In[6]:


# Use info to becoime more familiar with names, quantities, and data types
df.info()


# In[7]:


# Start data viz
# Convert date columns to datetime to get total trip duration efficiently
df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])


# In[8]:


# Boxplot shows interquartile range (IQR) and outliers for trip distance
plt.figure(figsize=(7,2))
plt.title('trip_distance')
sns.boxplot(data=None, x=df['trip_distance'], fliersize=1);


# In[9]:


# Histogram for trip distance
plt.figure(figsize=(10,5))
sns.histplot(df['trip_distance'], bins=range(0,26,1))
plt.title('Trip distance histogram');


# In[10]:


# Boxplot for cost of trips
plt.figure(figsize=(7,2))
plt.title('total_amount')
sns.boxplot(x=df['total_amount'], fliersize=1);


# In[11]:


# Histogram for cost of trips
plt.figure(figsize=(12,6))
ax = sns.histplot(df['total_amount'], bins=range(-10,101,5))
ax.set_xticks(range(-10,101,5))
ax.set_xticklabels(range(-10,101,5))
plt.title('Total amount histogram');


# In[12]:


# Boxplot for tip amount
plt.figure(figsize=(7,2))
plt.title('tip_amount')
sns.boxplot(x=df['tip_amount'], fliersize=1);


# In[13]:


# Histogram for tip amount
plt.figure(figsize=(12,6))
ax = sns.histplot(df['tip_amount'], bins=range(0,21,1))
ax.set_xticks(range(0,21,2))
ax.set_xticklabels(range(0,21,2))
plt.title('Tip amount histogram');


# In[14]:


# Histogram comparing tip amount between vendors
plt.figure(figsize=(12,7))
ax = sns.histplot(data=df, x='tip_amount', bins=range(0,21,1), 
                  hue='VendorID', 
                  multiple='stack',
                  palette='pastel')
ax.set_xticks(range(0,21,1))
ax.set_xticklabels(range(0,21,1))
plt.title('Tip amount by vendor histogram');


# In[15]:


# Histogram comparing tip amounts over 10 between vendors
tips_over_ten = df[df['tip_amount'] > 10]
plt.figure(figsize=(12,7))
ax = sns.histplot(data=tips_over_ten, x='tip_amount', bins=range(10,21,1), 
                  hue='VendorID', 
                  multiple='stack',
                  palette='pastel')
ax.set_xticks(range(10,21,1))
ax.set_xticklabels(range(10,21,1))
plt.title('Tip amount by vendor histogram');


# In[16]:


df_2 = df['trip_distance'].loc[~(df==0).all(axis=1)]


# In[17]:


sns.scatterplot(x=df['total_amount'], y=df_2)

