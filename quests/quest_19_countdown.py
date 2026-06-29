#!/usr/bin/python3
# Quest 19: The Countdown
# Concept: range(start, stop, step) - rocket launch countdown

print("=== Quest 19: The Countdown ===")
print("Initiating rocket launch sequence...\n")

for count in range(10, 0, -1):
    print(f"T-minus {count}...")

print("\nBlastoff!")
print("The rocket has launched successfully!")
