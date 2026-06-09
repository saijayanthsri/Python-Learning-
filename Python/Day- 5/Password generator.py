import random

char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']

numbers=['0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9']

symbols=['!', '@', '#', '$', '%',
    '^', '&', '*', '(', ')']

a=int(input("No of char:"))
b=int(input("No of numbers:"))
c=int(input("No of symbols:"))

password=[]

for i in range(a):
    password.append(char[random.randint(0, 25)])

for i in range(b):
    password.append(numbers[random.randint(0, len(numbers)-1)])

for i in range(c):
    password.append(symbols[random.randint(0, 9)])

random.shuffle(password)

word= ''.join(password)

print(f"Your password is{word}")
                
