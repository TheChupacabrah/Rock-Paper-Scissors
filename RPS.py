#John Hatch
#January 13, 2022
#Rock Paper Scissors
from random import randint #import randint is importing the radint function from the random library
from time import sleep
from guizero import App, Text, PushButton, Picture
# import random is importing the entire random library



#Deciding Function
def decide_winner(): 
    user_score = 0
    computer_score = 0
    
    
    
    while user_score < 3 and computer_score < 3:
        
        user_choice = input("Choose between Rock, Paper or Scissors: ")
        options = ['Rock', 'Paper', 'Scissors']
        computer_choice = options[randint(0,2)]
        
        print("Computer Selecting...")
        sleep(1)
        print("Computer chose " +computer_choice)
        sleep(2)
        print(computer_choice)
        #Conditional Statements
        if user_choice == computer_choice:
            print("It's a Tie!")
        elif user_choice == "Rock" and computer_choice == "Scissors":
            print("Rock beats Scissors, you won!")
            user_score = user_score+1
        elif user_choice == "Paper" and computer_choice == "Rock":
            print("Paper beats Rock, you won!")
            user_score = user_score +1       
        elif user_choice == "Scissors" and computer_choice == "Paper":
            print("Scissors beats Paper, you won!")
            user_score = user_score +1        
        else:
            print("You lose!")
            computer_score = computer_score +1
        print("User Score: " + str(user_score) + " - " + "Computer Score: " + str(computer_score))

        if user_score == 3:
            print("Congrats dawg, YOU WON!")
        if computer_score == 3:
            print("Too bad, you lost")
decide_winner()
