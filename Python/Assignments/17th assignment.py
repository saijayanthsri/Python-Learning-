
subjects={"name": "jayanth", "class":["python","Sql","Java","Excel"]}
print(subjects)
print(type(subjects))

print(subjects.keys())
print(subjects.values())
print(subjects.items())
print(subjects.get("name"))

a={}
n=input("Enter your name:")
age=int(input("Enter your age:"))

a["Name"]=n
a["Age"]=age

print(a)


#string methods

s="python"

print("S:", s)
print(type(s))

print(s[4]) #indexing the element

#methods

a=s.upper()
print("Upper:", a)

b=s.lower()
print("Lower:", b)

c=s.capitalize()
print("Capitalize:", c)

d=s.isalpha()
print("isalpha:",d)

mobile=input("Enter your number:")
e=mobile.isnumeric()
print("isnumeric:", e)


mail="jay123"
f=mail.isalnum()
print("isalnum:",f)
