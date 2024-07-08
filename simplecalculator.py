from typing import DefaultDict
name= input("please enter your name ")
print("Hi", name, "welcome to the cows and bulls game")

def instructions():
  print("1.",name,"you have to choose any three digit number" )
  print("2.when the game starts you will have 8 chances to guess the number")
  print("""3.if the number you guesed first is matches with given number then you have one cows
         eg:given num:123
            first guesed num:421
            (you have two cows) """)
  print("""4.if the number you guesed first is matches with the place then you have three bulls
         eg:given num:123
            first guesed num:124
             (you have two bulls)""")
              
           

def startgame():
  print("you have 8 chances to guess the number")
  
from random import randint
def random():
  while True:
    n = str(randint(100,999))
    if not(n[0]==n[1] or n[0]==n[2] or n[1]==n[2]):
      return n
   

     

#let the user pick the choice
print("enter choices(1/2):")
print("1.instructions")
print("2.ready to start game")

while True:

        # Take input from the user
        choice = input("Enter choice(1/2): ")

        # Check if choice is one of the four options
        if choice in ['1', '2']:
            
            if choice == '1':
                print({instructions()})
            
            elif choice == '2':
                  print({startgame()})
                  break
        else:
            print("Invalid input. Please enter 1 or 2.")