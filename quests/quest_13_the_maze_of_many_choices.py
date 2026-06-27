#!/usr/bin/python3
score = input("Enter the score(0-100): ")

if not score.isdigit():
    print("Enter a valid number")
else:
    score = int(score)
    
    if score >=90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    else:
        result = "Needs Improvement"

    print(result)
