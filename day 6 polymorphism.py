#!/usr/bin/env python
# coding: utf-8

# In[1]:


#method overriding
class animal:
    def speak(self):
        print("amimals speak")
class dog(animal):
    def speak(self):
        print("alkeya bark")
class cat(animal):
    def speak(self):
        print("bunna meow")
class pig(animal):
    def speak(self):
        print("suzana oooohhooo")
obj=cat()
obj.speak()


# # Abstract Method

# In[2]:


#Abstract has a package called abc(abstract base class)
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod   #annotations are started with @ to define what a method is doing
    def calculate_area(self):
         pass #in abstract class the method body is not written in the abstract class
class Square(Area):
    def calculate_area(self):
        print("in square method")
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()


    


# In[3]:


#shift operations
print(16>>2)#16/2=8/2=4


# In[4]:


print(7<<3)#left shift 7*2=14*2=28*2=56


# In[5]:


print(11<<3)#11*2=22*2=44*2=88


# In[6]:


print(12>>2)#12/2=6/2=3


# # tic tac toe
# 

# In[7]:


board = [['', '', ''],['', '', ''],['', '', '']]

def print_board(board):
    print(*board[0], sep=" | ")
    print("---------")
    print(*board[1], sep=" | ")
    print("---------")
    print(*board[2], sep=" | ")
def get_markers():
    marker1 = input("Player 1 choice(X or O): ").upper()
    marker2 = ""
    if marker1 == "X":
        marker2 = 'O'
        return ['X', 'O']
    elif marker1 == 'O':
        marker2 = 'X'
        return ['O', 'X']
    else:
        print("Invalid Input")
        return get_markers()

def get_coordinates():
    x,y = list(map(int, input("Enter the coordinates: ").split()))
    if x in [0,1,2] and y in [0,1,2]:
        return [x,y]
    else:
        print("Invalid Input")
        return get_coordinates()

def check_for_win(board):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[1] != "":
            return True
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != "":
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != "":
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "":
        return True
    return False


def update_board(board, chance, marker, x,y):
    if chance == True:
        board[x][y] = marker
        if check_for_win(board):
            print("Player 1 wins")
            return "game over"
        return False
    else:
        board[x][y] = marker
        if check_for_win(board):
            print("Player 2 wins")
            return "game over"
        return True

def play_game():
    player1 = 0
    player2 = 0
    m1, m2 = get_markers()
    print(f"player 1: {m1}, player 2: {m2}")
    chance = True
    while True:
        print_board(board)
        x, y = get_coordinates()
        if chance:
            chance = update_board(board, chance, m1, x,y)
            if chance == "game over":
                break
        else:
            chance = update_board(board, chance, m2, x, y)
            if chance == "game over":
                break

play_game()





# In[ ]:




