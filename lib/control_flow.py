#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.upper() == 'ADMIN' and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

print(admin_login("ADMIN", "12345"))
# "Access denied"
print(admin_login("admin", "12345"))
# "Access granted"
print(admin_login("Edith", "12345"))
# "Access granted"


def hows_the_weather(temperature):
    # your code here
    if temperature<40:
        return "It's brisk out there!"
    if temperature >=40 and temperature <=65:
        return "It's a little chilly out there!"
    if temperature>85:
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"

    pass
print(hows_the_weather(33))
 # "Brisk!"
print(hows_the_weather(99))
# "Too dang hot"
print(hows_the_weather(75))
# "Perfect!"
    

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
