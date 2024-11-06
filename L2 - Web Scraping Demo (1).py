#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url = 'https://archive.org/details/cu31924067841738'
response = requests.get(url)

# Save HTML to file

with open("language_of_flowers.html", mode='wb') as file:
    file.write(response.content)


# After saving the data to a html file, you should be able to see a language_of_flowers.html in the `lesson2/Demo` directory. Open the html file and see what you get. 

# In[2]:


response.content


# In[ ]:





# In[ ]:




