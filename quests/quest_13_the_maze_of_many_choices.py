#!/usr/bin/python3
score = int(input("Enter the score(0-100): "))

if score >=90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
else:
    result = "Needs Improvement"

print(result)
