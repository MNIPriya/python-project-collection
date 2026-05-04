"""
workflow 
input : rock ,paper,scissor
computer will choose random choice 
result print
logic:
a - rock 
rock-rock = tie 
rock - paper = paper win 
rock - scissor = rock win 
b - paper 
paper- paper = tie
paper- rock = paper win 
paper- scissor = scissor win
c - scissor 
scissor - paper = scissor  win 
scissor-scissor = tie 
scissor - rock = rock win
    """
import random 
item = ["rock","paper","scissor" ]
user_choice = input("enter your move = rock , paper ,scissor ")
comp_choice = random.choice(item)

print(f"user choice = {user_choice},computer choice ={comp_choice}")
if user_choice == comp_choice :
    print("both has choosen same so it's tie")
elif user_choice =="rock":
    if comp_choice == "paper":
        print("you won")
    else:
        print("you loose")
elif user_choice == "paper":
    if comp_choice =="scissor":
        print("you loose")
    else:
        print("you won")
elif user_choice == "scissor":
    if comp_choice == "paper":
        print("you win")
    else :
        print("you loose")
else:
    print("you have entered the wrong choice")