#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[2]:


path= r"C:/Users/soubh/OneDrive/Documents/file sorter/"


# In[3]:


file_name = os.listdir(path)


# In[4]:


folder_names= ['csv files','image files','text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


# In[5]:


for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("There are files in this path that are not moved!")


# In[ ]:





# In[ ]:





# In[ ]:




