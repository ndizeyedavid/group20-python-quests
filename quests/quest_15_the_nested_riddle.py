#!/usr/bin/python3

print("Mellow Surfing adventure\n")
print("You are are at the beach and there are two paths to go to. LEFT or Right?")

user_choice_1 = input("Which path do you choose: ")

if user_choice_1.lower() == "left":
    print("You are now seeing an beautiful blue occean in front of you")
    user_choice_2 = input("Do you want to SWIM in it or WAIT?: ")

    if user_choice_2.lower() == "swim":
        print("Yayyy!!! you have swimmed the blue ocean and found TREASURE🪙")
    else:
        print("You have decided to sit on the beach side and watch the waves...")
else:
    print("Unfortunately, nothing is on the right side. Instead you met a furious shark with legs and it is now chasing you 🏃")
    print("A shark with legs hahahhaa!!!")
