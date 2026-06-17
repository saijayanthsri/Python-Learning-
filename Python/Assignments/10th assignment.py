# print odd numbers between 25 to 50 (both loops)
#while
num=25

while num <50:
    if num % 2 != 0:
        print(f"{num} is odd")
    num += 1

#for
for a in range(25,51):
    if a % 2!= 0:
        print(f"{a} is odd")

#divisible by 7 between 23 to 44(both loops)

#while

num=23

while num<=44:
    if num % 7 == 0:
        print(f"{num} is divisible by 7")
    num +=1

#for

for num in range(23,45,1):
    if num % 7 == 0:
        print(f"{num} is divisible by 7")
