#!/usr/bin/env python
# coding: utf-8

# In[43]:


#dictionary
l=[]
for i in range(2):
    s1={
        'username':input("enter username:"),
        'password':input("enter password:")
    }
    l.append(s1)
print(l)


# In[44]:


#item is used for accessing dictionary objects
a=[
    {'vineela@gmail.com':'vineela'},
    {'alkeya@gmail.com':'alkeya'},
    {'buuna@gmail.com':'buuna'},
    {'vani@gmail.com':'vani'},
    {'sujana@gmail.com':'sujana'}
]
print(a)
username=input("enter username:")
password=input("enter password:")
temp={username:password}

if temp in a:
    print("found")
else:
    print("not found")
    


# In[45]:


#arrays
#1.single dimension array
#2.multi dimension array(2D,3D.......)
row=2
col=2
arr=[]
for i in range(row):
    element=[]
    for j in range(col):
        element.append((int(input("enter element:"))))
    arr.append(element)
print(arr)


# In[46]:


arr=[[1,2],[3,4]]
ar2=[[2,3],[3,5]]
result=[[0,0],[0,0]]
for i in range(len(arr)):
    element=[]
    for j in range(len(ar2)):
        
        result[i][j]=arr[i][j]+ar2[i][j]
print(result)   


# In[1]:


rows=int(input("enter number of rows:"))
col=int(input("enter number of columns:"))
print("enter the elements of first matrix:")
matrix_a=[[int(input()) for i in range(col)] for i in range(rows)]
print("First matrix is: ")
for n in matrix_a:
    print(n)

print("enter the elements of second matrix:")
matrix_b=[[int(input()) for i in range(col)] for i in range(rows)]
print("Second matrix is: ")
for n in matrix_b:
    print(n)
    
result=[[0 for i in range(col)] for i in range(rows)]

for i in range(rows):
    for j in range(col):
        result[i][j]=matrix_a[i][j]+matrix_b[i][j]
        
print("the sum of two matrices is:")
for r in result:
    print(r)


# In[34]:


row=2
col=2
arr1=[]
arr2=[]
for i in range(row):
    temp=input("enter elements in row:").split(' ')
    ele=list(map(int,temp))
    arr1.append(ele)
print(arr1)
for i in range(row):
    temp=input("enter elements in row:").split(' ')
    ele=list(map(int,temp))
    arr2.append(ele)
print(arr2)
res=[[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        res[i][j]=arr1[i][j]+arr2[i][j]
print(res)


# In[18]:


#ACCESSING ELEMENTS MATRIX
arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
temp=[]
b=list(map(int,input("enter elements").split(' ')))
print(b)


# In[21]:


#this code has errors like we have given row 4 but given more row elements
row=4
col=5
new_arr=[]
for i in range(row):
    b=list(map(int,input("enter elements").split(' ')))
    new_arr.append((b))
print(new_arr)


# In[27]:


#slicing [start:end:stepsize]
col=4
l=[1,2,3,4,5,6,7]
print(l)
print(l[0:10:2])


# In[28]:


#slicing for reverse order
col=4
l=[1,2,3,4,5,6,7]
print(l)
print(l[::-1])


# In[42]:


#fibonnaci series
n=int(input())
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(0,n):
    sum=a+b
    print(sum,end=' ')
    a=b
    b=sum


# In[15]:


#string methods
#split
s="vineela,anaparthi bhu"
print(s)
res=s.split(',')
print(res)


# In[16]:


#join
s="vineela anaparthi"
print(s)
res=s.split(" ")
print(res)
print('&'.join(res))


# In[22]:


#upper and lower
s1="hello"
s2="THIS IS VINEELA"
print(s1.upper())
print(s2.lower())


# In[24]:


#swapcase
s1="helLO"
s2="THIS iS VINeela"
res=s1.swapcase()
res2=s2.swapcase()
print(res,res2)


# In[27]:


#capitalize
s1="helLO"
s2="THIS iS VINeela"
s1.capitalize()


# In[28]:


#count
s1="vineela"
s1.count('e')


# In[40]:


first="vineela is "
age=  20
last=" years old"
print(first + str(age) + last)


# In[38]:


#formatting strings
num=5
print("the square of {} is {}".format(num,num*num))


# In[49]:


num=5.776
print("the square of {:10}#it gives 10 spaces is {:.8f}".format(num,num*num))


# In[50]:


num=5.776
print(f"the square of {num} is {num*num:.3f}")


# In[54]:


#exception handling
a=int(input())
b=int(input())
try:
    print(a/b)
except:
    print("b cannot be 0")
    print("after the error")


# In[1]:


a=int(input())
b=int(input())

try:
    print(a/b)
    print(a+b)
    print(a-b)
    print(a*b)
except:
    print("b cannot be 0 in division")


# In[8]:


try:
    a=list(map(int,input().split(' ')))
    print(a)
except:
    print("a is not an integer")


# In[11]:


print(eval("1+5*7//10/9"))


# # Functions

# In[9]:


#functions
#it is used to reduce the code
#it is used for better readability


# In[10]:


#there are four types of functions in python
#1.regular functions
#2.default value functions
#3.key argument function
#4.variable lenght functions


# In[14]:


#regular functions
#example
def addition(number1,number2):
    result=number1+number2
    return result
print(addition(10,20))
    


# In[57]:


#prime program using function
def prime(n):
    count=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            count+=1
    if count==2:
         print("prime")
    else:
        print("not prime")   
            
print(prime(23))


# # ways to check prime number

# In[ ]:


#num=23
#method-1
#for i in range(1,num+1):#23 iterations
    #pass
#method-2
#for i in range(2,num):#21 iterations
    #pass
#method-3
#for i in range(2,num//2):#10 iterations
    #pass
#method 4
#for i in range(2,int(num**0.5)+1):#only 3 iterations(most efficient way)
    #pass


# In[50]:


#default value functions
def add(n1,n2):
    return n1+n2
a=10
b=20
res=add(a,b)
print(res)


# In[41]:


#key argument function
def add(n1,n2):
    print("n1: ",n1)
    print("n2: ",n2)
add(n2=10,n1=20)


# In[1]:


#variable lenght function
def add(*abc):
    print(abc)
add(10,11,20,21,"hello")
    
        


# In[18]:


n=input()
a1=[]
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            if arr[i] in a1:
                break
            
            print(arr[j],end=" ")
            break
else:
    print("NO")
            
     


# In[ ]:




