height=int(input("Enter your height:"))

bill=0

if height >= 120:

    print("Allow")

    age=int(input("Enter your age:"))

    if age <18:

        bill=100

        print("Your bill is 100")

    elif age >18 and age <25:

        bill=150

        print("Your bill is 150")

    else:

        bill=200

        print("Your bill is 200")

    photo=input("y for photo and N for no photo=")

    if photo == "y":

        bill += 50

        print(f"Your final bill is{bill}")
        
else:

    print("Don't allow")
