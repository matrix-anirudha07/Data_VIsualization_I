#!/usr/bin/env python
# coding: utf-8

# Distplot ** Joinplot ** Pairplot

# In[25]:


import seaborn as sns
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


pd.options.display.max_columns=None
pd.options.display.max_rows=None
pd.options.display.width=None


# In[27]:


df=sns.load_dataset('tips')
df.head()


# In[28]:


df.corr()


# In[29]:


df['day'].unique()


# In[30]:


sns.heatmap(df.corr());


# In[31]:


sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')


# In[32]:


sns.pairplot(df,hue='sex')


# In[33]:


sns.distplot(df['tip']);


# In[34]:


sns.distplot(df['tip'],kde=False,bins=10);
#kde=kernel density estimation


# Countplot ** Violinplot ** Boxplot ** Barplot

# In[35]:


df.head()


# In[36]:


sns.countplot(x='sex',data=df) 


# In[37]:


sns.countplot(x='smoker',data=df)


# In[39]:


sns.countplot(y='day',data=df)


# In[41]:


sns.barplot(x='total_bill',y='tip',data=df)


# In[42]:


sns.barplot(x='total_bill',y='smoker',data=df)


# In[43]:


sns.boxplot(x='sex',y='total_bill',data=df)


# In[45]:


sns.boxplot(x='smoker',y='total_bill',data=df,palette='rainbow')


# In[48]:


sns.boxplot(data=df,orient='h')


# In[52]:


sns.boxplot(x='total_bill',y='day',hue='smoker',data=df,palette='rainbow',orient='h')


# In[54]:


sns.violinplot(x='total_bill',y='smoker',data=df,palette='rainbow')


# In[55]:


sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow')


# In[ ]:




