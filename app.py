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
