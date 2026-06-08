import random

secret_num=int(input("Enter the number between 1-10:"))

guess= random.randint(1,10)

if secret_num == guess:
    print("Correct!!")

else:
    print("Wrong")
