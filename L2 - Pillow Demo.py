#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image

im = Image.open("goldfish.jpg")
im.show()


# In[4]:


im.size


# In[5]:


flipped_im = im.transpose(Image.FLIP_TOP_BOTTOM)
flipped_im.show()


# In[4]:


# save a image using extension
flipped_im = flipped_im.save("flipped_goldfish.jpg")


# In[ ]:




