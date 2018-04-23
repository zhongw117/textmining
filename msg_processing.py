
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import numpy as np


# In[2]:


# open mysql
db_conn = pymysql.connect("192.168.89.38", "test", "test", "mq_admin", charset='utf8' )


# In[3]:


my_sql = "select group_id, user_nickname, content, content_type from group_chat_content"
df = pd.read_sql(my_sql, db_conn)

db_conn.close()


# In[4]:


df.head(10)


# In[5]:


# pd.notnull(df)


# In[6]:


df['content_length'] = df['content'].str.len()


# In[7]:


# df.head()


# In[8]:


df_ceshiqun = df[df['group_id']=='Wilson_我的测试群']
# df_测试群.tail()


# In[9]:


df_youpintuangou = df[df['group_id']=='Wilson_优品团购']
df_Wordpress = df[df['group_id']=='Wilson_Wordpress']
df_lunchbreak = df[df['group_id']=='Wilson_lunchbreak']
df_wenshawuyou4 = df[df['group_id']=='Wilson_温莎无忧4']
df_wenshawuyou1 = df[df['group_id']=='Wilson_温莎无忧1']
df_javascript = df[df['group_id']=='Wilson_javascript']
df_xianyou = df[df['group_id']=='Wilson_鲜优']
df_yiminjiangzuo = df[df['group_id']=='Wilson_移民讲座']
df_nvshijie = df[df['group_id']=='Wilson_女世界']
df_jubenzhijia = df[df['group_id']=='Wilson_剧本之家']


# In[10]:


df_jubenzhijia


# In[11]:


jubenzhijia_chat_count = df_jubenzhijia['user_nickname'].value_counts()
youpintuangou_chat_count = df_jubenzhijia['user_nickname'].value_counts()
Wordpress_chat_count = df_Wordpress['user_nickname'].value_counts()
lunchbreak_chat_count = df_lunchbreak['user_nickname'].value_counts()
wenshawuyou4_chat_count = df_wenshawuyou4['user_nickname'].value_counts()
wenshawuyou1_chat_count = df_wenshawuyou1['user_nickname'].value_counts()
javascript_chat_count = df_javascript['user_nickname'].value_counts()
xianyou_chat_count = df_xianyou['user_nickname'].value_counts()
nvshijie_chat_count = df_nvshijie['user_nickname'].value_counts()


# In[12]:


xianyou_chat_count


# In[13]:


group_activity = df['group_id'].value_counts()


# In[14]:


# group messages totally counts 
group_activity


# In[15]:


group_UN_activity = df['user_nickname'].value_counts()


# In[16]:


# all members' messages totally counts 
group_UN_activity.head(10)


# In[39]:


df_group_mem = df[['group_id','user_nickname']]
df_group_mem.head()


# In[40]:


df_group_mem_ = df_group_mem.groupby(["group_id","user_nickname"])


# In[41]:


df_group_mem_.size()


# In[43]:


df_mem_group_ = df_group_mem.groupby(["user_nickname","group_id"])
df_mem_group_.size()

