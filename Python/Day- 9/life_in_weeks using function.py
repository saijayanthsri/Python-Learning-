def life_in_weeks(age):
    left = 90 -age
    weeks = left*52
    return weeks
    
age = int(input("Enter your age:"))
print(f"{life_in_weeks(age)} Weeks left")


        
