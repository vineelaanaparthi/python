#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list methods


# In[3]:


lst=[]
lst.append("hii")
lst.append(10)
lst.append(10.0)
lst.append([10,2,3])
print(lst)


# In[4]:


#lenth of list
print(len(lst))


# In[10]:


#remove an element in list using pop and remove
lst.pop()#if we donot specify the index value then it will remove the last element
print(lst)#pop is used to remove the index value


# In[11]:


list=[1,2,3,4,5]
list.remove(3)#remove is used to remove element
print(list)


# In[13]:


#insert method in list
a=[10,22,34,45]
print(a.insert(2,23))
print(a)


# In[14]:


#extend method in list
a=[1,2,3,4,5]
b=[10,20,30,40,50]
a.extend(b)
print(a)


# In[19]:


#count
v=[1,2,3,4,5,1,3,2,3,1,4,2,3]
m=v.count(3)
print(m)


# In[21]:


#copy
a=[10,20,30]
b=a.copy()
print(b)


# In[23]:


#clear
a=[10,20,30]
a.clear()
print(a)


# In[24]:


#reverse
a=[10,20,30]
a.reverse()
print(a)


# In[26]:


#sort
a=[10,30,20]#by default it sort in ascending order
a.sort()
print(a)


# In[28]:


#descending order
a=[3,4,1,2]
a.sort(reverse=True)
print(a)


# In[30]:


a=[3,4,1,2]
b=sorted(a)
print(b)
print(a)


# In[31]:


#descending order
a=[3,4,1,2]
b=sorted(a,reverse=True)
print(b)
print(a)


# In[8]:


#coversion from string to list using map function
a=list('12345')
print(a)
b=list(map(int,a))
print(b)


# In[33]:


#type conversion
#explicit conversion
a=int('2')
b=7
c=a+b
print(c)


# In[36]:


#input from user
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a+b)


# In[22]:


a=int('123')
b=a%10
c=a//10
d=c%10
e=c//10
r=b**2
v=d**2
n=e**2
print(r,v,n)


# In[40]:


a='123'
for i in range(len(a)):
    print(int(a[i])**2)


# In[ ]:


S

