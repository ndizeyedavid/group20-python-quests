#!/usr/bin/python3
# Quest 28: The Adventure Begins
# Concept: Text-based Choose Your Own Adventure game
# Uses functions for locations, has 2 different endings

def show_intro():
    print("=" * 50)
    print("      THE LOST KINGDOM OF KIGALI HILLS")
    print("=" * 50)
    print("\nYou wake up at the edge of a dense forest.")
    print("Your mission: find the legendary ForgeHub Scroll")
    print("that holds the secrets to building the future.\n")

def get_choice(options):
    while True:
        for key, label in options.items():
            print(f"  [{key}] {label}")
        choice = input("\nYour choice: ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Try again.\n")

def location_forest_edge():
    print("\n--- FOREST EDGE ---")
    print("Two paths stretch before you:")
    print("  A winding trail leads north into dark woods.")
    print("  A cobblestone road heads east toward a village.\n")

    options = {"n": "Take the dark woods trail", "e": "Head to the village"}
    choice = get_choice(options)

    if choice == "n":
        location_dark_woods()
    else:
        location_village()

def location_dark_woods():
    print("\n--- DARK WOODS ---")
    print("Twisted trees loom overhead. It is eerily quiet.")
    print("You spot a faint glow deeper in the forest.")
    print("A rustling behind you makes you hesitate.\n")

    options = {
        "f": "Follow the glow deeper in",
        "b": "Back away carefully toward the forest edge"
    }
    choice = get_choice(options)

    if choice == "f":
        location_ancient_shrine()
    else:
        print("\nYou retreat safely and find yourself back at the forest edge.\n")
        location_forest_edge()

def location_ancient_shrine():
    print("\n--- ANCIENT SHRINE ---")
    print("A glowing stone altar stands in a clearing.")
    print("On it rests a scroll sealed with golden light.")
    print("An inscription reads: Only those who build for others may take this.")
    print("\nYou think of ForgeHub and the youth you hope to empower.")
    print("The seal breaks on its own. The scroll is yours.\n")

    options = {
        "t": "Take the scroll and leave",
        "s": "Study it here at the shrine"
    }
    choice = get_choice(options)
    ending_a(choice)

def location_village():
    print("\n--- KIGALI HILLS VILLAGE ---")
    print("A bustling village of innovators and craftspeople.")
    print("An elder waves you over. The scroll is in the tower north of here,")
    print("she says. But the bridge is guarded by a riddle-keeper.\n")

    options = {
        "t": "Head to the tower",
        "r": "Rest and learn from the villagers first"
    }
    choice = get_choice(options)

    if choice == "r":
        print("\nThe villagers teach you ancient problem-solving techniques.")
        print("You feel sharper and more prepared. (+Wisdom)\n")
    location_riddle_bridge()

def location_riddle_bridge():
    print("\n--- RIDDLE BRIDGE ---")
    print("A keeper in a grey cloak blocks the bridge.")
    print("Answer my riddle to pass, he says.\n")
    print("RIDDLE: I have cities, but no houses live there.")
    print("        I have mountains, but no trees grow there.")
    print("        I have water, but no fish swim there.")
    print("        What am I?\n")

    answer = input("Your answer: ").strip().lower()

    if "map" in answer:
        print("\nCorrect! the keeper says, stepping aside.")
        print("You cross the bridge and reach the tower.\n")
        ending_b(won_riddle=True)
    else:
        print("\nIncorrect, he says. The answer is a MAP.")
        print("But your boldness earns you a second chance.")
        print("He hands you a worn map and lets you pass anyway.\n")
        ending_b(won_riddle=False)

def ending_a(study_choice):
    print("\n" + "=" * 50)
    print("         ENDING A: THE ENLIGHTENED BUILDER")
    print("=" * 50)
    if study_choice == "s":
        print("\nYou spend hours at the shrine reading the scroll.")
        print("Its wisdom fills you with clarity and purpose.")
        print("You return to the world not just with the scroll,")
        print("but with deep understanding of what it means.")
        print("\nForgeHub rises from your vision - a beacon for")
        print("African youth, built on ancient wisdom and modern tech.")
    else:
        print("\nYou carry the scroll back to civilization.")
        print("Its contents inspire a generation of builders.")
        print("ForgeHub is born. The scroll's legacy lives on.")
    print("\nTHE END - You have unlocked: The Enlightened Builder")
    print("=" * 50)

def ending_b(won_riddle):
    print("\n" + "=" * 50)
    print("         ENDING B: THE PERSISTENT PIONEER")
    print("=" * 50)
    if won_riddle:
        print("\nYou climb the tower and claim the ForgeHub Scroll.")
        print("Your sharp mind and village wisdom guided you perfectly.")
        print("You return triumphant, scroll in hand.")
    else:
        print("\nThe keeper's mercy lets you reach the tower.")
        print("You find the scroll and realize something important:")
        print("the journey and the people you meet matter as much")
        print("as the destination.")
        print("You return humbled - and stronger for it.")
    print("\nEither way, ForgeHub is built. Africa's youth have")
    print("a place to create, learn, and lead.")
    print("\nTHE END - You have unlocked: The Persistent Pioneer")
    print("=" * 50)

def play_again():
    print("\nWould you like to play again?")
    options = {"y": "Yes, start a new adventure!", "n": "No, exit the game."}
    choice = get_choice(options)
    return choice == "y"

def main():
    show_intro()
    playing = True
    while playing:
        location_forest_edge()
        playing = play_again()
    print("\nThank you for playing. Go build something great!\n")

if __name__ == "__main__":
    main()
