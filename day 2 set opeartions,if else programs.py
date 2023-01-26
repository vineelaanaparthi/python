#!/usr/bin/env python
# coding: utf-8

# In[2]:


#set operations 
a={1,2,3,4,5}
b={3,4,5,6,7}
c=b.difference(a)
c


# In[10]:


a={1,2,3,4}
d=a.add(6)
a


# In[18]:


#conditional statements
#if and else
#print if a number is even or odd
a=int(input("Enter a number:"))
if(a%2==0):
    print("%d is Even number"%(a))
else:
    print("%d is Odd number"%(a))


# In[64]:


#prime or not
a=int(input())
if(a==1):
    print("Neither prime nor composite")
elif(a==2):
    print("prime")
for i in range(2,a):
    if(a%i)==0:
        print("not prime")
        break
    else:
        print("prime")
        break


# In[59]:


#if,elif,else
a=int(input())
if(a==1):
    print("SUNDAY")
elif(a==2):
    print("MONDAY")
elif(a==3):
    print("TUESDAY")
elif(a==4):
    print("WEDNESDAY")
elif(a==5):
    print("THURSDAY")
elif(a==6):
    print("FRIDAY")
elif(a==7):
    print("SATURDAY")
else:
    print("Invalid Input")


# In[68]:


#if in ranges
n=int(input())
if i in range(0,19):
    if(n%2==0):
        print("weird number")
elif i in range(20,30):
    print("normal number")


# In[75]:


#n>0,n<20--if even --weird, odd---normal
#n>=20,n<30--normal 
#n>=30--if even --weird,odd---normal
n=int(input())
if((n>0) and (n<20)):
    if(n%2==0):
        print("weird number")
    else:
        print("Normal number")
        
elif((n>=20) and (n<30)):
    print("Normal number")
else:
    if(n>=30):
        if(n%2!=0):
            print("Normal number")
        else:
            print("weird number")

    


# In[77]:


#dictionary
#in dictionary we use curly braces,key and values are seperated by colon
#db
#{
 #   key1:value1
  #  key2:value2
#}


# In[14]:


d={}
d.update({'key1':'value1'})
d.update({'key2':'value2'})
d.update({'key1':'value3'})
print(d)
print(d.get('key2'))


# In[19]:


#dictionary program
student_details={}
student_details.update({202:'vineela'})
student_details.update({203:'alkeya'})
student_details.update({218:'bhuvana'})
print(student_details)
print(student_details.get(202))


# In[109]:


a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")


# In[110]:


a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        print("*",end=" ")
    print(" ")


# In[122]:


a=int(input())
for i in range(1,a+1):
    for j in range(i-1,a):
        print("*",end=" ")
    print(" ")


# In[24]:


#reverse of a number
n=int(input())
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)


# In[2]:


#add digits of a number
n=int(input())
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)


# # Git hub commands
1)git init
2)git remote add origin link(paste the link)
3)git add .
4)git commit -m "initial commit"
5)git push origin master
6)#to move to another branch
* git branch {branch name}
# In[1]:


lst=[1,2,3,4]
for i in lst:
    print(i**2)


# In[2]:


l=[1,2,3,4,5,6,7,8]
k=int(input())
for i in range(len(l)):
    if(k==l[i]):
        print(i)
        break
   


# In[3]:


l=[]
for i in range(20):
    l.append(i+1)
print(l)


# In[4]:


l=[x**3 for x in range(0,11)]
print(l)


# In[5]:


l=[x for x in range(0,51) if x%2==0]
print(l)


# In[6]:


l=[x for x in range(1,101) if (x%7==0 or x%11==0)]
print(l)


# In[7]:


l=[x for x in range(1,101) if (x%7==0 and x%11==0)]
print(l)


# In[8]:


#for loop can be used when termination is known.
#in while loop we dont know the termination point


# In[9]:


lst=[1,2,3,4]
print(lst[::-1])


# In[6]:


lst=[1,2,3,4,4,5,6]
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")


# In[5]:


l=[1,2,3,-4]
sum=1
for i in range(1,len(l)):
    if(l[i]>0):
        temp=l[i]
        sum=sum+temp
print(sum)
    


# In[ ]:


#Arthimetic operations
a=int(input())
b=int(input())
addition=a+b
print(addition)
sub=a-b
print(sub)
mul=a*b
print(mul)
div=a/b


# In[ ]:




