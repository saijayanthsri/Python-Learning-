height=int(input("Enter your height:"))
bill=0

if height >=120:

    print("allow")

    age=int(input("Enter your age="))

    if age <18:

        bill =100

        print("Your bill is 100")

    elif age >18 and age <25:

        bill =200

        print("Your bill is 200")

    else:

        bill = 300

        print("Your bill is 300")

    photo= input("Do you want photo Y or N")

    if photo == "Y":

        print(f"Your total bill is {bill}")

else:

    print("Dont allow")
