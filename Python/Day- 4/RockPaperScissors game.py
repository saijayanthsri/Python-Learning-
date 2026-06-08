Sprint("Welcome to the Game")
import random
choose=input("Enter you choice:")
symbol=["Rock","Paper","Scissor"]
game=random.randint(0,2)
computer = symbol[game]
print(symbol[game])

if computer == choose:
    print("It's a draw, Play again!")

elif computer == "Rock" and choose == "Paper":
    print("Paper wins!")

elif computer == "Rock" and choose == "Scissor":
    print("Scissor wins!")

elif computer == "Paper" and choose == "Scissor":
    print("Scissor wins!")