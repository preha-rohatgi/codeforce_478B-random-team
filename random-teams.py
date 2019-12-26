#!/usr/bin/env python
# coding: utf-8

# In[2]:


n,m=map(int,input().split())
count=0
if m==1:
  count=(n*(n-1))/2
  print(str(int(count))+' '+str(int(count)))
elif n%m==0:
  a=int(n/m)
  p=(a*(a-1))/2
  min=int(p*m)  
  a=n-m+1
  max=(a*(a-1))//2
  print(str(min)+' '+str(max))
else:   
  a=int(n/m)
  if a>1:
    count=(a*(a-1))/2
  a=int((n-int(n/m)*(m-(n%m)))/(n%m))
  p=(a*(a-1))/2
  min=int((m-(n%m))*count+(n%m)*p)
  a=n-m+1
  max=((a-1)*a)//2
  print(str(min)+' '+str(max))






