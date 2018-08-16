
# coding: utf-8

# In[1]:

name ="supergirl"

name  = "wonderwoman"

name = "Superman"


# In[2]:


age = 99


# In[3]:


print(name)


# In[4]:


print(age)


# In[5]:


print("my name is")


# In[6]:


print("my name is",name)


# In[7]:


print("my age is",age)


# In[8]:


print("my name is", name," and my age is", age)


# In[9]:


newage = age - 50


# In[10]:


multipliedage = age * 2


# In[11]:


print("your age is actually", newage)


# In[12]:


print("your multiplied age is",multipliedage)


# In[13]:


NewAge  = 100


# In[14]:


newage = 50


# In[15]:


sequence = "CTAGCTAG"


# In[16]:


print(sequence)


# In[17]:


print(sequence[0])


# In[18]:


print(sequence[3])


# In[19]:


print("my fourth letter is", sequence[3])


# In[20]:


len(sequence)


# In[21]:


print("the length of the sequence",len(sequence))


# In[22]:


COX1 = "CTAG"


# In[23]:


name ="anuj"


# In[24]:


first_name ="anuj"


# In[25]:


sequence[0]


# In[26]:


sequence[1]


# In[27]:


sequence[2]


# In[28]:


sequence[0:2]


# In[29]:


sequence[0:3]


# In[30]:


type(sequence)


# In[31]:


type(age)


# In[32]:


COX2 = "TACG"


# In[33]:


COX1 = "CTAG"


# In[34]:


COX1 - COX2


# In[35]:


COX1 + COX2


# In[36]:


firstname = "anuj"


# In[37]:


lastname = "guru"


# In[38]:


firstname + lastname


# In[39]:


firstname + " " + lastname


# In[40]:


age


# In[41]:


len(age)


# In[42]:


name


# In[43]:


age


# In[44]:


name + age


# In[45]:


5**2


# In[46]:


print(5**2)


# In[47]:


print("5 square is", 5**2)


# In[48]:


5%2


# In[49]:


# this is a comment


# In[ ]:


# adding two sequences because they turned out to be the same gene


# In[50]:


COX1+ COX2


# In[51]:


max(23,2,5)


# In[52]:


max(3,"anuj")


# In[53]:


round(3.14232343434)


# In[54]:


round(3.14243243,2)


# In[55]:


min(2,3,4)


# In[56]:


help(min)


# In[57]:


help(round)


# In[58]:


help(round


# In[59]:


name = "anuj


# In[60]:


print("age is",aege)


# In[61]:


max(21,32,45) 


# In[ ]:


# add the minimum with maximum


# In[62]:


max(21,32,45) + min(21,32,45)


# In[63]:


hundred_C = "c" * 100


# In[64]:


100_C = "C" *100


# In[65]:


print(hundred_C)


# In[66]:


hundred_C + COX1 


# In[67]:


len(hundred_C + COX1)


# In[68]:


import math


# In[69]:


math.cos(180)


# In[70]:


math.sin(180)


# In[71]:


math.sin(3.14)


# In[72]:


print("the sine of 180 is ", math.cos(180))


# In[73]:


math.pi


# In[74]:


math.sin(math.pi)


# In[75]:


math.cos(math.pi)


# In[76]:


help(math)


# In[77]:


import math
math.cos(45)


# In[78]:


import math as m


# In[79]:


m.cos(45)


# In[80]:


from math import cos


# In[81]:


cos(45)


# In[82]:


import pandas


# In[83]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[84]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[85]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[86]:


print(name)


# In[87]:


print(data)


# In[88]:


data = pandas.read_csv("gapminder_gdp_oceania.csv")


# In[89]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv",index_col="country")


# In[90]:


data


# In[91]:


data.info()


# In[92]:


data


# In[93]:


data.T


# In[94]:


data.describe()


# In[95]:


data.T.describe()


# In[96]:


data.columns


# In[97]:


data


# In[98]:


data.iloc[1,2]


# In[99]:


data.iloc[0,0]


# In[100]:


data.loc["Australia","gdpPercap_1952"]


# In[101]:


data.loc["Australia",:]


# In[102]:


data.loc[:,"gdpPercap_1952"]


# In[103]:


data


# In[104]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[105]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"]


# In[106]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"].max()


# In[107]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].max()


# In[108]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].min()


# In[109]:


subset = data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[110]:


print(subset > 11000)


# In[113]:


subset[subset>11000]


# In[114]:


subset[subset>11000].describe()

