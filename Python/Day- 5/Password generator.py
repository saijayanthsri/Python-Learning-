import random

char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password=""

for i in range(8):
    password += random.choice(char)

print(f"Your password",password)

