
# coding: utf-8

# In[1]:


user='Tom'
password='123'


# In[3]:


user_user=input("please input your username:")
pass_password=input("please input your password:")
if user==user_user and password==pass_password:
    print("success")
else:
    print("fail")


# In[15]:


score_sort=[2,13,4,5,6,9,1.3,3.4]
for i in range(len(score_sort)):
    for j in range(i+1):
        if score_sort[i]<=score_sort[j]:
            score_sort[i],score_sort[j]=score_sort[j],score_sort[i]
print(score_sort)   


# In[17]:


import random
number=random.randint(1,100)
number


# In[13]:


import numpy as np 
num=np.zeros(shape=(3,3))
num


# In[15]:


for i in range(0,3):
    for j in range(0,3):
            num[i,j]=i*j
print(num)


# In[24]:


numbers=[2,3,5,7,3,4,6,3,2,5,2,4,3]
for i in range(len(numbers)):
    for j in range(i+1):
        if(numbers[i]<=numbers[j]):
            numbers[j],numbers[i]=numbers[i],numbers[j]
print(numbers)


# In[43]:


import random
chance=5
number=input("请输入你猜测的数：")
num_random=random.randint(1,20)
for i in range(len(chance)):
    if number>num_random:
        print("您输入的数字大了！")
        chance=chance-1
        print("您还有%d"%(chance))
        continue
    if number<num_random:
        print("你输入的数字小了:")
        chance=chance-1
        print("您还有%d"%(chance))
        continue
    else:
        print("你猜对了！！！")
        break
        
    


# In[51]:


import random
number=input("请输入你猜测的数：")
num_random=random.randint(1,20)
if number>int(num_random):
    print("您输入的数字大了！")
    break
elif number<int(num_random):
    print("你输入的数字小了:")
    break
else:
    print("你猜对了！！！")
    break
        
    

