#!/usr/bin/env python
# coding: utf-8

# In[2]:


#repition operator
t=[1,2,3]*3
print(t)


# In[3]:


#Bitwise XOR operator
#&,|,^
print(5^10)


# In[5]:


#packages
#from [filename] import [function name]#it works on company laptop other than the online compiler


# # Object Oriented Programming(OOP's)

# In[6]:


#class=blueprint(declare variables in class)
#self keyword is used in python as that of the this keyword in java,c++
#self and this uses same methodology


# In[11]:


""""class student:
    name="vineela"
    roll_number="2"
    branch="aiml"
    marks=0
    attendance=0.0
    is_using_transport=False
    def viw_attendance(self):
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass
    
        


# In[12]:


#constructors are used to provide default values or initial values for variable object
class student:
    name=""
    def __init__(self,name):
        print("object created")
        print(name)

s1=student("vineela")


# In[14]:


class student:
    student_name="no_name"
    name=""
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)

s1=student("vineela")


# In[19]:


class student:
    student_name="no_name"
    def __init__(self,name):
        self.student_name=name
s1=student("vineela")
s2=student("vine")
s3=student("vinni")
print(s2.student_name)


# In[21]:


class student:
    student_name="no_name"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        self.student_name=new_name
s1=student("vineela")
s2=student("vine")
s3=student("vinni")
print(s3.student_name)
s3.update_name("vineela anaparthi")
print(s3.student_name)


# In[1]:


#if we give two __ means it is private and we cannot access the private variables outside the class when  we use objects
#ascii value for 0 is 48,A is 65,a is 122


# In[ ]:


#syntax for login system
class user:
    full_name=""
    email=""
    __password="" #private password
    mobile_number=""
    def update_name(self,new_name):
        self.full_name= new_name
    def get_name(self):
        return self.full_name
    #setter method for private variable password
    def update_password(self,new_password):
        pass
    def update_mobile_number(self,new_number):
        pass
    #setter method for private variable password
    def get_user_password(self):
        return self.__password
        


# In[ ]:


#using login system
class userclass:
    full_name=""
    email=""
    __password="" #private password
    mobile_number=""
    def __init__(self,name,email,password):
        self.full_name=full_name
        self.email=email
        self.__password=password
    def update_name(self,new_name):
        self.full_name= new_name
    def get_name(self):
        return self.full_name
    #setter method for private variable password
    def update_password(self,new_password):
        pass
    def update_mobile_number(self,new_number):
        pass
    #setter method for private variable password
    def get_user_password(self):
        return self.__password


# In[ ]:


#from User import userclass
class login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
    def create_user(self,name,email,password):
        new_user=User(name,email,password)
        self.__db.append(new_user)
    def valiadte_user(self,email,password):
        pass
    
obj=login()
while True:
    option=input("enter your choice")
    if option == '1':
        name=input("Enter your full name:")
        email=input("enter your email:")
        password=input("create a new password:")
        res=obj.create_user(name,email,password)
        if res==True:
            print("user object created")
            
    elif option == '2':
        pass
    elif option == '3':
        break
    else:
        print("Invalid Input")


# In[ ]:




