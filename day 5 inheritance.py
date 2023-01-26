#!/usr/bin/env python
# coding: utf-8

# # Inheritance

# In[6]:


class A:
    name="Mukesh"
    age=20
class B(A):
    age=10
obj=B()
print(obj.age)
print(obj.name)
    


# In[7]:


class A:
    name="Mukesh"
    age=20
class B(A):
    age=10
obj=B()
obj.name="vinni"
print(obj.age)
print(obj.name)


# In[9]:


class A:
    name="Mukesh"
    age=20
class B(A):
    age=10
class C(B):
    pass
class D(C):
    pass
obj=D()
obj.name="vinni"
print(obj.age)
print(obj.name)


# In[14]:


#example for multi level inheritance
#single parent-->child(this will act as parent for next child)-->child
class college:
    name="pragati"
    years="21"
class principal(college):
    name="satyanarayana"
    branch="EEE"
class hod(principal):
    name="radhakrishna"
    branch="AIML"
class aiml(hod):
    pass
obj=principal()
obj.name="h.babu"
obj.branch="ECE"
obj1=hod()
obj1.name="vinni"
print(obj.name)
print(obj.branch)
print(obj1.name)
print(obj1.years)


# In[21]:


#Hierarchial Inheritance
#single parent with two children
class laptops:
    brand=""
    displaysize=""
class dell(laptops):
    storage=""
    core=""
class hp(laptops):
    chargingcapability=""
    displaysize=""
obj=laptops()
obj.core="operating system"
print(obj.brand)
    


# In[31]:


#multiple inheritance
#two parent class and one child class
class reptile:
    def landliving(self):
        print("it lives on land")
class waterreptile:
    def waterliving(self):
        print("it lives on water")
class frog(reptile,waterreptile):
    def frogs(self):
        print("lives in both")
obj1=frog()
obj1.frogs()


# In[32]:


#hybrid inheritance is cobination of two inheritances
#hierarchial and multiple
class restaurant:
    food_items=""
    drinks=""
class veg(restaurant):
    def veg_info(self):
        print("veg starters and veg biriyani")
class nonveg(restaurant):
    def nonveg_info(self):
        print("chicken biriyani and mutton biriyani")
class customer(veg,nonveg):
    def customer_info(self):
        print("eat and pay")
obj=customer()
obj.customer_info()


# In[20]:


#random function
from random import random ,randint  
a=randint(1,10)
id=random()*1000
print(id)
print(a)


# In[ ]:


#rock,paper,scissors
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]


# In[ ]:


from random import randint
choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=5
while p_score!=limit and c_score!=limit:
    print(f"enter among the following",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice: {sys_ch}")
    if my_ch==sys_ch:
        print("Draw")
        continue
    if my_ch=="rock" and sys_ch=="scissor":
        p_score+=1
    elif my_ch=="paper" and sys_ch=="rock":
        p_score+=1
    elif my_ch=="scissor" and sys_ch=="paper":  
        p_score+=1
    else:
        c_score+=1
    print(f"your score: {p_score},system score: {c_score}")
   
   
if p_score>c_score:
    print("you win the match")
else:
    print("system wins the match")


# In[1]:


#polymorphism
#function overloading
class A:
    def method(self,a,b):
        print("sum of 2 numbers",a+b)
class B(A):
    def method_1(self,a,b):
        print("mul of 2 numbers",a*b)
    def method_1(self,abc):
        print("value is",abc)
        
ob=B()
ob.method_1(10)


# In[2]:


#the method stores in the latest memiry storage
#overriding
class A:
    def method(self,a,b):
        print("sum of 2 numbers",a+b)
class B(A):
    def method_1(self,a,b):
        print("mul of 2 numbers",a*b)
ob=B()
ob.method_1(10,20)


# In[12]:


def invert(string):
    res=""
    for i in string:
        if i=='0':
            res+='1'
        else:
            res+= '0'
    return res
a=int(input())
b=int(input())
op=input()
new_a=bin(a)[2:]
new_b=bin(b)[2:]
new_a=invert(new_a)
new_b=invert(new_b)
print(new_a,new_b)
x=int(new_a,2)
y=int(new_b,2)
print(x^y)


# In[ ]:




