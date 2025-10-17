# snake water gun game 
a = int(input("Enter first number"))
b = int(input("Enter second number"))
if( a ==1 & b==1):
    print("Draw")
elif (a ==0 & b == 0):
    print("win")
else:
    print("lose")



# Decorators in python 
def greet(fx):
   def mfx():
     print("good morning")
     fx()
     print("Thanks for using this function")
   return mfx  

@greet        
def hello():
   print("Hello worlld")

hello()


# slove with logics 

import random 
def check(comp,user):
    if comp ==user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 2:
        return -1
    return 1 
comp = random.randint(0,2)    
user = int(input("o for snake, 1 for water and 2 for gun:"))
score = check(comp , user)

print("you",user)
print("comp",comp)
if score == 0:
    print("its a draw")
elif score == -1:
    print("you lose")
else:
    ("you won")  
