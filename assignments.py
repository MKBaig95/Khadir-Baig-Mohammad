
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


import numpy as np


# In[ ]:


data=np.array([0, (10)])


# In[ ]:


data


# In[ ]:


data=np.zeros((4))


# In[ ]:


data


# In[ ]:


data=np.zeros(10)
data[2]=5


# In[ ]:


data


# In[ ]:


data


# In[ ]:


a=np.arange(10)*3


# In[ ]:


a


# In[ ]:


data[::-1]


# In[ ]:


a=np.array([0,1,2,3,4,5,6,7,8,])
a=size(3,3)


# In[ ]:


a=np.random.randint(0,9, size=(3,3))


# In[ ]:


a


# In[ ]:


a=np.arange(0,9)


# In[ ]:


a


# In[ ]:


nz=np.nonzero([1,2,0,0,4,0])


# In[ ]:


[nz]


# In[ ]:


a


# In[ ]:


a[1]


# In[ ]:


a[0]


# In[ ]:


a[(0)]


# In[ ]:


a.[1]


# In[ ]:


data=np.random.random((3,3,3))


# In[ ]:


data


# In[ ]:


data=np.random.random(10,10)


# In[ ]:


import numpy as np


# In[ ]:


data=np.random.random((10,10))


# In[ ]:


data


# In[ ]:


data.max(),data.min()


# In[ ]:


[data.min()]


# In[ ]:


data[2]=0


# In[ ]:


data=np.random.random(30)


# In[ ]:


data


# In[ ]:


a=data.mean()


# In[ ]:


a


# In[ ]:


mean(data)


# In[ ]:


a=np.array([1,0,1])


# In[ ]:


a.reshape(size=(3,3))


# In[ ]:


a=np.arange(0,1,0,0).reshape((3,3))


# In[ ]:


a


# In[ ]:


a=np.ones((10,10))


# In[ ]:


a[1:-1,1:-1]=0


# In[ ]:


a


# In[ ]:


a=np.arange(1,1,1).reshape(6,7,8)


# In[ ]:


a=np.random.randint(10,size=(6,7,8))


# In[ ]:


a


# In[ ]:


a[6,7,1]


# In[ ]:


a.unravel_index(100,(6,7,8))


# In[ ]:


np.zeros(10)


# In[ ]:


data=np.zeros(10)
data[5]=1


# In[ ]:


data


# In[ ]:


a=np.unravel_index(100,(7,5,4))


# In[ ]:


a


# In[ ]:


a=np.random.random((3,3))


# In[ ]:


a


# In[ ]:


a.unravel_index(100,(6,7,8))


# In[ ]:


a=np.arange(15).reshape(5,3)


# In[ ]:


b=np.arange(6).reshape(3,2)


# In[ ]:


a.reshape(1,5,3)*b.reshape(2,1,3)


# In[ ]:


Z = np.dot(np.ones((5,3)), np.ones((3,2)))


# In[ ]:


Z


# In[ ]:


a=(range(5),-1)
from numpy import *
sum(range(5),-1)


# In[ ]:


a


# In[ ]:


b=np.ones((10,10))


# In[ ]:


b


# In[ ]:


b[1:-1,1:-1]=0


# In[ ]:


b


# In[ ]:


a


# In[ ]:


import numpy as np


# In[ ]:


a=np.zeros((10,10))


# In[ ]:


a[0,0]=1


# In[ ]:


a


# In[ ]:


a=np.zeros((10,10))


# In[ ]:


a[0,0]


# In[ ]:


a[0:-1,0:-1]=1


# In[ ]:


a


# In[ ]:


import numpy as np


# In[ ]:


a=np.random.random((10,10))


# In[ ]:


a


# In[ ]:


a.max()


# In[ ]:


z=np.random.uniform(2,10,10)


# In[ ]:


z


# In[ ]:


a=z-z%1


# In[ ]:


a


# In[ ]:


(np.floor(z))


# In[ ]:


b=np.random.randint(0,20, size=(5,5))


# In[ ]:


b


# In[ ]:


z=np.zeros((5,5))


# In[ ]:


# z+=np.arange(3)


# In[ ]:


# z


# In[ ]:


z


# In[ ]:


z


# In[ ]:


a=np.random.random(10)


# In[ ]:


a.sort()


# In[ ]:


a


# In[ ]:


A=np.array([1,2,3,4,5])


# In[ ]:


B=np.array([1,2,3,4,5])


# In[ ]:


a=A==B


# In[ ]:


equal=np.allclose(A,B)


# In[ ]:


equal


# In[ ]:


Z = np.random.randint(0,2,size=(2,10))
(Z.any(axis=0)).any()


# In[ ]:


z


# In[ ]:


z


# In[ ]:


a=np.random.randint(0,10,(2,3,4,3))


# In[ ]:


a


# In[ ]:


sum = a.reshape(a.shape[:-2] + (-1,)).sum(axis=-1)


# In[ ]:


sum


# In[ ]:


a=np.arange(75).reshape(5,5,3)


# In[ ]:


b=np.arange(25).reshape(5,5,1)


# In[ ]:


a.reshape(5,5,3)*b.reshape(5,5,1)


# In[ ]:


Z = np.random.randint(0,5)


# In[ ]:


z


# In[ ]:


z


# In[ ]:


i = 1 + (Z.shape[0]-3)


# In[ ]:


Z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (Z.shape[0]-3)
j = 1 + (Z.shape[1]-3)
C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)


# In[2]:


ser1=(data=[1,2,3,45], index=["a","b","c","d"])


# In[3]:


import pandas as pd


# In[8]:


ser1=pd.Series([1,2,3,45], ["a","b","c","d"])


# In[9]:


ser1

