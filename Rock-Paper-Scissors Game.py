
import random 
option=("rock","paper","scissors")
comp=random.choice(option)
player=input("Enter a choice:")
print(f"player:{player}")
print(f"computer:{comp}")
if player==comp:
    print("Draw ")
elif player=="scisorrs" and comp=="paper":
    print("you win:)")       
elif player=="paper" and comp=="rock":
    print("you win:)") 
elif player=="rock" and comp=="scisorrs":
    print("you win:)") 

else:
    print("you lose! :(")
