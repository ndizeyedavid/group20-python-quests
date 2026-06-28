#!/usr/bin/python3

def personalized_greeting(name, quest):
    print(f"Hello, {name}! Good luck on your quest to {quest}!")

name = input("Enter your name: ")
quest = input("Enter your quest: ")

personalized_greeting(name, quest)
