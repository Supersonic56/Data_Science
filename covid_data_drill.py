#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import os
import urllib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data", "covid")


# In[3]:


os.makedirs(file_path,exist_ok=True)
csv_path = os.path.join(file_path, "WHO-COVID-19-global-data.csv")
urllib.request.urlretrieve(url,csv_path)


# In[11]:


df = pd.read_csv(csv_path)


# In[12]:


df


# In[13]:


df_index = df.index
df_index


# In[14]:


df_cols = df.columns
df_cols


# In[15]:


df_index.values


# In[16]:


df.values


# In[18]:


df.dtypes


# In[19]:


df.shape


# In[20]:


df.head()


# In[21]:


df.head(10)


# In[22]:


df.tail()


# In[23]:


df.info()


# In[24]:


df.describe()


# In[26]:


df["Country"]


# In[27]:


df["Country"].unique()


# In[28]:


df.columns = [col.strip() for col in df.columns]
df.columns


# In[29]:


df.Country


# In[30]:


df.loc[1:4, "Country"]


# In[34]:


df.loc[1:4, ["Country", "New_cases"]]


# In[35]:


df.Country == 'United States of America'


# In[36]:


df[df.Country == 'United States of America']


# In[37]:


df[df.New_deaths > 1000]


# In[40]:


df.loc[df.New_deaths > 1000, ['New_deaths', 'Country']]


# In[41]:


df.loc[(df.New_deaths > 1000) & (df.Country_code == 'US'),['Date_reported', 'Country', 'New_cases', 'New_deaths']]


# In[42]:


df.loc[df.Country_code == 'US', ['New_cases']].max()


# In[43]:


df.loc[df.Country_code == 'US', ['New_cases']].min()


# In[44]:


df.loc[df.Country_code == 'US', ['New_cases']].sum()


# In[45]:


df.loc[df.Country_code == 'US', ['New_deaths']].sum()


# In[46]:


df.loc[df.Country_code == 'US', ['Cumulative_cases']].sum()


# In[47]:


df.New_deaths.idxmax()


# In[48]:


df.loc[df.New_deaths.idxmax(),['Date_reported', 'Country', 'New_cases', 'New_deaths']]


# In[49]:


df[df.New_deaths < 0]


# In[51]:


df['pct_cases'] = (df['New_cases'] / df['Cumulative_cases'])*100
df


# In[ ]:




