#multiple if

pizza_size=input("Select pizza size S,M and L=")
pepperoni=input("Do you want pepperoni Y or N=")
cheese=input("Do you want cheese Y or N=")
bill=0

if pizza_size == "S":

    bill=15

    if cheese == "Y":

        bill += 1

    if pepperoni == "Y":

        bill += 2

if pizza_size == "M":

    bill=20

    if cheese == "Y":

        bill += 1

    if pepperoni == "Y":

        bill += 3

if pizza_size == "L":

    bill= 25

    if cheese == "Y":

        bill += 1

    if pepperoni =="Y":

        bill += 3

print(f"Your total bill is {bill}")
    


