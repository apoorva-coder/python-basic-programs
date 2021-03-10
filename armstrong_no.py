#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input("enter a number:"))
temp=n
s=0
while temp>0:
    digit = temp % 10
    print(digit)
    s+= digit ** 3
    temp //= 10
if n==s:
    print("armstrong number")
else:
    print("not armstrong number")
print(s)
 


# In[ ]:




