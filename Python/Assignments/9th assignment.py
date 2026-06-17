#even or odd

number=int(input("Enter a number:"))

if number % 2 == 0:
    print(number,"is even")

else:
    print(number,"is odd")

#positive, negative and zero

number=int(input("Enter a number:"))

if number <0:
    print("Negative")

elif number == 0:
    print("Zero")

else:
    print("Positive")

#greatest of two number

n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

if n1 >  n2:
    print(n1,"is greatest of two")

elif n1 < n2:
    print(n2,"is greatest of two")

#pass or fail

marks=int(input("Enter marks:"))

if marks <= 35:
    print("Fail")

else:
    print("Pass")

#grade system

marks=int(input("Enter your marks:"))

if marks>=90:
    print("Grade is A")

elif marks>=75 and marks<=89:
    print("Grade is B")

elif marks>=50 and marks<=74:
    print("Grade is c")

elif marks <50:
    print("Fail")

#smallest of three numbers

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if a>b and a>c:
    if b>c:
        print(c,"is smallest")

    elif c>b:
        print(b,"is smallest")

elif b>a and b>c:
    if a>c:
        print(c,"is smallest")

    elif c>a:
        print(a,"is smallest")

elif c>a and c>b:
    if a>b:
        print(b,"is smallest")

    elif b>a:
        print(a,"is smallest")
        

#check character

alpha=input("Enter a alphabet:")

vowels="aeiouAEIOU"
if alpha in vowels:
    print("Character is vowels")

else:
    print("Character is consonants")

#Divisible by 5 and 11

num=int(input("Enter a number:"))

if num % 5 == 0 and num % 11 == 0:
    print("can divisible by")

else:
    print("Can't divisible")










         
    
