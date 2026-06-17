'''
#sum of 10 numbers
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total= 0

for num in numbers:
    total += num

print("Sum=", total)

#smallest and greatest

num=[28,90,365,4]
smallest= num[0]
for i in range(4):
    if num[i] < smallest:
        smallest = num[i]
print(f"Smallest number= {smallest}")

greatest =num[0]
for i in range(4):
    if num[i] > greatest:
        greatest =num[i]
print(f"Greatest number= {greatest}")

#reverse a list

list=[10,9,8,7,6,5,4,3,2,1]

reverse=[]

for i in range(9,-1,-1):
    reverse.append(list[i])
print(reverse)


#second largest number

a= [45,98,45,32,88,70]

largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i !=largest:
        second = i

print(f"Second largest= {second}")


# remove duplicate

a= [1,2,2,3,4,4,5]

b= []

for i in a:
    if i not in b:
        b.append(i)
print(b)   
'''

#how many times appear

a= [1,2,3,2,4,2,5,5,3]
n=int(input("Enter element: "))

count =0

for i in a:
    if i == n:
        count += 1
print(count)
