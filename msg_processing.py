
# coding: utf-8

# In[41]:


# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# In[42]:


df_chat = pd.read_csv('/home/wilson/Downloads/group_chat_content(1).csv')


# In[43]:


list(df_chat)


# In[44]:


df_chat_trim = df_chat.drop(['user_signature','time','region','city'],axis=1)


# In[45]:


list(df_chat_trim)


# In[46]:


df_chat_trim.tail()


# In[47]:


df_chat_trim['content_length'] = df_chat_trim['content'].str.len()


# In[48]:


df_chat_trim.head()


# In[49]:


# save user_info to a sinlge series
json_user = df_chat_trim['user_info']


# In[51]:


# count total messages of all time
df_group_acti = df_chat_trim['group_displayname'].value_counts()
df_group_acti = df_group_acti.to_frame()
df_group_acti.head()


# In[55]:


# count total text messages
df_group_text = df_chat_trim[df_chat_trim['content_type']=='Text']
df_group_text_acti = df_group_text['group_displayname'].value_counts()
df_group_text_acti = df_group_text_acti.to_frame()
df_group_text_acti.head()


# In[56]:


# count short text messages of all groups
df_group_short_text = df_group_text[df_group_text['content_length']<=50]
df_group_short_text_acti = df_group_short_text['group_displayname'].value_counts()
df_group_short_text_acti = df_group_short_text_acti.to_frame()
df_group_short_text_acti.head()


# In[13]:


group_activity = df['group_id'].value_counts()


# In[14]:


# group messages totally counts 
group_activity


# In[22]:


# the total amount of groups
print(len(group_activity))


# In[15]:


group_UN_activity = df['user_nickname'].value_counts()


# In[16]:


# all members' messages totally counts 
group_UN_activity.head(10)


# In[17]:


df_group_mem = df[['group_id','user_nickname']]
df_group_mem.head()


# In[18]:


df_group_mem_ = df_group_mem.groupby(["group_id","user_nickname"])


# In[19]:


df_group_mem_.size()


# In[20]:


# list the amount of messages in different groups of an individual 
df_mem_group_ = df_group_mem.groupby(["user_nickname","group_id"])
df_mem_group_.size()


# In[30]:


df_group = df.groupby(["user_nickname","content","group_id","content_type"])


# In[32]:


df_group = df_group.size()


# In[35]:


df_group = df_group.to_frame()


# In[38]:


df_group.head(10)

