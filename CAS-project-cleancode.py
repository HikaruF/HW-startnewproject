#!/usr/bin/env python
# coding: utf-8

# # CAS HW clean code practice 

# packages

# In[ ]:


# importing packages 

import pandas as pd
import csv


# ### Loading population data. 

# In[2]:


# loading CSV datafile as Panda dataframe 

import pandas as pd 
myFilepop = pd.read_csv('file-population.csv', sep=',')

print(myFilepop)


# In[3]:


# only leaving the information I need (year and population of the world total) and removing all other columns 

dfpop = myFilepop[["Year","WLD"]]
print(dfpop)


# In[4]:


# making dictionary where keys are the years, and values are the world total population 

dictpopWorld = dict(zip(dfpop.Year, dfpop.WLD))
print(dictpopWorld)


# In[5]:


datapoints = dictpopWorld.values()

list1 = []
list2 = []
list3 = []
list4 = []

for i in datapoints:
    if i <4e9:
        list1.append(i) 
    if 4e9 <= i <5e9:
        list2.append(i) 
    if 5e9 <= i <6e9:
        list3.append(i) 
    if i> 6e9: 
        list4.append(i) 
        
print(list1)
print(list2)
print(list3)
print(list4)


# # REWRITING THE CODE for clean code practice

# In[8]:


#Here we classify population data into several dictionaries 

population_level1 = 4e9    # 4 billion population
population_level2 = 5e9    # 5 billiion population 
population_level3  = 6e9   # 6 billionpopulation 


#dictionary where key is year and value is population 
dict_lowpopulation = {}
dict_normalpopulation = {}
dict_highpopulation = {}
dict_growingpopulation = {}

# Checking popuation level in each year and classifying into four different levels 
for key in dictpopWorld.keys():
    if dictpopWorld[key] < population_level1:
        dict_lowpopulation[key] = dictpopWorld[key] 
    if population_level1 <= dictpopWorld[key] < population_level2:
        dict_normalpopulation[key] = dictpopWorld[key] 
    if population_level2 <= dictpopWorld[key] < population_level3:
        dict_highpopulation[key] = dictpopWorld[key] 
    if dictpopWorld[key] > population_level3:
        dict_growingpopulation[key] = dictpopWorld[key] 
        
print(dict_lowpopulation)
print(dict_normalpopulation)
print(dict_highpopulation)
print(dict_growingpopulation)


# Because year and population information are combined as dictionary, we can print when the population reached the next level
print(list(dict_lowpopulation)[0]) 
print(list(dict_normalpopulation)[0])   # year in which population reached 4e9 
print(list(dict_highpopulation)[0])     # year in which population reached 5e9 
print(list(dict_growingpopulation)[0])   # year in which population reached 6e9 


# In[ ]:


import numpy as np


plt.plot(dict_lowpopulation.keys(), dict_lowpopulation.values())
plt.show()


# In[ ]:




