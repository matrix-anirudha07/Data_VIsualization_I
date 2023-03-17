#!/usr/bin/env python
# coding: utf-8

# Scatter Plot
# Bar Plot
# Histogram
# Boxplot
# Pie Chart

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# pd.options.display.max_columns=None
# pd.options.display.max_rows=None
# pd.options.display.width=None

# In[2]:


a=np.arange(0,10)
b=np.arange(11,21)


# In[3]:


c=np.arange(30,45)
d=np.arange(45,55)


# In[4]:


plt.scatter(a,b,c='b')
plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('2D Graph')
plt.savefig("Graph.jpg")


# In[5]:


b=a*a


# In[6]:


plt.plot(a,b,'b*',linestyle='--',linewidth=2,markersize=13)
plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('2D Graph');


# In[7]:


plt.subplot(3,3,1)
plt.plot(a,b,'b--')
plt.subplot(3,3,2)
plt.plot(a,b,'g-')
plt.subplot(3,3,3)
plt.plot(a,b,'r--*')
plt.subplot(3,3,4)
plt.plot(a,b,'c:<')
plt.subplot(3,3,5)
plt.plot(a,b,'m--v')
plt.subplot(3,3,6)
plt.plot(a,b,'y--h')


# In[8]:


np.pi


# In[9]:


x=np.arange(0,5*np.pi,0.3)
y=np.sin(x)
plt.plot(x,y)
plt.title('Sine wave')


# In[10]:


x=np.arange(0,5*np.pi,0.3)
y_sine=np.sin(x)
y_cosine=np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y_sine,'c--o')
plt.subplot(2,1,2)
plt.plot(x,y_cosine,'m:|')


# In[11]:


x=[1,5,8]
y=[10,18,5]

x2=[2,6,9]
y2=[12,19,17]

plt.bar(x,y)
plt.bar(x2,y2,color='m')
plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('Bar Plotting');


# In[12]:


q=np.array([25,27,28,34,38,45,44,49,65,72,78,85,94])
plt.hist(q)
plt.title('Histogram Plotting')


# In[13]:


data= [np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data,vert=True,patch_artist=True);


# In[15]:


country_size= 'Russia','India','Italy','France','USA'
sizes = [510,350,95,121,420]
colors = ['green','blue','red','yellow','cyan']
explode = (0.085,0.0,0.0,0.0,0.0)

plt.pie(sizes,explode=explode,labels=country_size,colors=colors,autopct='%1.1f%%')
plt.axis('equal');


# In[ ]:





# In[ ]:




