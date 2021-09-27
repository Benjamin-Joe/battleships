from random import randint

password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)
