
#upright star pattern
a= 1
while a<=4:
    b=1
    while b<=a:
        print("*", end=" ")
        b+=1
    print("\n")
    a+=1


for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print("\n")

# upside down
num= 5
while num >=0:
    j=1
    while j<=num:
        print("*", end= " ")
        j+=1
    print("\n")
    num-=1

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("\n")

#numbers

for i in range(1,6):
    for j in range(1,5):
        print(i, end=" ")
    print("\n")

a= 1
while a<=5:
    b=1
    while b<=4:
        print(a, end=" ")
        b+=1
    print("\n")
    a+=1
