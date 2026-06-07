weight=float(input("Enter your weight="))

height=float(input("Enter your height="))

bmi_cal=weight/(height**2)

print(bmi_cal)

if bmi_cal <18.5:

    print("Underweight")

elif bmi_cal >18.5 and bmi_cal <25:

    print("Normal weight")

else:

    print("Overweight")
