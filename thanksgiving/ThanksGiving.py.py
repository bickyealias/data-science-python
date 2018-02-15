
# coding: utf-8

# # Reading our data
# 

# In[20]:


import pandas as pd
data = pd.read_csv("thanksgiving.csv" , encoding = "Latin-1" ) #loading the csv content into a dataframe
print (data.head())   # prints first row of data dataframe


# # list down the columns
# 

# In[24]:


print (data.columns)


# # Values seggregation to find how many celebrate thanks giving

# In[25]:


print (data ['Do you celebrate Thanksgiving?'].value_counts())


# ## Filter out and override the data set with only rows that celebrate thanksgiving

# In[2]:


data = data[data ['Do you celebrate Thanksgiving?'] == 'Yes']


# In[7]:


print (data ['Do you celebrate Thanksgiving?'].value_counts())


# ## See what are the dishes broadly with their counts

# In[8]:


print (data ['What is typically the main dish at your Thanksgiving dinner?'].value_counts())


# ## Display the Do you typically have gravy? column for any rows from data where the What is typically the main dish at your Thanksgiving dinner? column equals Tofurkey.
# 

# In[4]:


data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']['Do you typically have gravy?']


# ## Create a filter that only selects rows from data where What is typically the main dish at your Thanksgiving dinner? equals Tofurkey.

# In[5]:


data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']


# In[6]:


data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']['Do you typically have gravy?']


#  ## figuring out what people eat pie

# In[7]:


apple_isnull = pd.isnull(data ['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])


# In[9]:


pumpkin_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'])


# In[11]:


pecan_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])


# In[12]:


ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull


# In[17]:


print (ate_pies.value_counts())


# ## Converting age to int

# In[29]:


def convert_to_int(column):
    if pd.isnull(column):
        return None
    else:
        age = column.split(" ")[0]
        age = age.replace("+" ,"")
        return int(age)
data['int_age'] = data['Age'].apply(convert_to_int)    # adding new column  
    
        


# In[30]:


data['int_age'].describe()


# ## Converting income to numeric

# In[15]:


def income_to_numeric(column):
    if pd.isnull(column):
        return None
    else:
        income = column.split(" ")[0]
        if income == 'Prefer':
            return None
        else:
            income = income.replace("$" ,"")
            income = income.replace("," ,"")
            income = income.strip()
            print (income)
            income = (int(income))
            return income
        
data['int_income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'] .apply(income_to_numeric)     


# In[16]:


data['int_income'].describe()


# In[20]:


data.columns


# ## See how far people earning under 150000 will travel.

# In[7]:


income_lessthan_15k = data[data['int_income'] <15000]


# In[8]:


income_lessthan_15k['How far will you travel for Thanksgiving?'].value_counts()


# ## Linking Friendship and age

# In[9]:


import numpy as np
data.pivot_table(index =["Have you ever tried to meet up with hometown friends on Thanksgiving night?"] ,columns = ['Have you ever attended a "Friendsgiving?"'] , values = 'int_age' , aggfunc = np.mean )


# In[10]:


data['int_income'].mean()


# ## Linking frienship and income

# In[17]:


data.pivot_table(index =["Have you ever tried to meet up with hometown friends on Thanksgiving night?"] ,columns = ['Have you ever attended a "Friendsgiving?"'] , values = 'int_income' , aggfunc = np.mean )


# ## Findings 
# People who are younger are more likely to attend a Friendsgiving, and try to meet up with friends on Thanksgiving.
# No strong correlation with -Income doesnt decide if you ll meet your friends
