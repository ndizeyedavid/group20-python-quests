#!/usr/bin/python3

user_age = input("What is your age?: ")
user_gold = input("How many gold coins do you have?: ")

if not user_age.isdigit() or not user_gold.isdigit():
    print("Please enter valid digits for age or gold...")
else:
    user_age = int(user_age)
    user_gold = int(user_gold)
    
    if user_age >= 18 and user_gold >= 20:
        result = "You may enter in the club"
    else:
        result = "You are NOT allowed to enter the club. Your age or gold is too low!"

    print(result)
