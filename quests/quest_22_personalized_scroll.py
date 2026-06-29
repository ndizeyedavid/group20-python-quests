#!/usr/bin/python3

def personalized_greeting(name, quest):
    """Return a personalized greeting."""
    return f"Hello, {name}! Good luck on your quest to {quest}!"


name = input("Enter your name: ")
quest = input("Enter your quest: ")

print(personalized_greeting(name, quest))
