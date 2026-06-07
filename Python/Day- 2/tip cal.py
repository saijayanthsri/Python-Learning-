bill_amount=float(input("Enter bill amount="))

tip_percentage=int(input("Enter tip percentage="))

tip_amount=(bill_amount*(tip_percentage/100))

total_amount=(bill_amount + tip_amount)

people=int(input("Enter number of people="))

print(total_amount/people)

print(round(total_amount/people, 2))
