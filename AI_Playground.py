# Programmer - Cade Smith
# Date - 2.29.2024
# Program - AI Playground

print("This will be a place for me to play with programming using Python programming using AI Technology.")

def start_game():
    print("Welcome to 'The Lost Expedition'!")
    print("You find yourself amidst a dense jungle, the air thick with humidity and the sound of exotic creatures echoing through the trees.")
    print("Ahead lies an ancient temple rumored to hold a treasure of immeasurable value.")
    print("As you venture deeper into the jungle, you come across an old map left behind by a previous explorer.")
    print("Upon examining the map, you notice a warning scribbled hastily in the corner: 'Beware the Guardians of the Temple.'")

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() == 'yes':
        explore_jungle()
    else:
        print("Game over. Come back when you're ready to embark on the adventure!")

def explore_jungle():
    print("You press on, determined to uncover the secrets hidden within the temple's walls.")
    print("You encounter a fork in the path.")

    choice = input("Do you choose to enter the cave or explore the garden? (cave/garden): ")
    if choice.lower() == 'cave':
        explore_cave()
    elif choice.lower() == 'garden':
        explore_garden()
    else:
        print("Invalid choice. Please try again.")
        explore_jungle()

def explore_cave():
    print("You steel yourself and enter the cave, the darkness swallowing you whole.")
    print("As you navigate the twisting passages, you come face to face with a ferocious beast guarding the entrance to the temple.")

    choice = input("Do you want to fight the beast or retreat? (fight/retreat): ")
    if choice.lower() == 'fight':
        print("You try to fight the beast...")
        print("But you are overpowered and meet a tragic end.")
        print("GAME OVER.")
    elif choice.lower() == 'retreat':
        print("You retreat back into the jungle.")
        explore_jungle()
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

def explore_garden():
    print("You cautiously make your way past the lush foliage.")
    print("Suddenly, you stumble upon a hidden trap, narrowly avoiding a deadly fall.")

    choice = input("Do you want to continue forward cautiously or charge in boldly? (cautiously/boldly): ")
    if choice.lower() == 'cautiously':
        enter_temple()
    elif choice.lower() == 'boldly':
        print("Your boldness proves to be your undoing as you trigger a series of traps.")
        print("You are trapped inside the temple. GAME OVER.")
    else:
        print("Invalid choice. Please try again.")
        explore_garden()

def enter_temple():
    print("You enter the temple cautiously.")
    print("Inside, you encounter a series of intricate puzzles and traps.")

    choice = input("Do you choose to investigate further or take the treasure and leave? (investigate/leave): ")
    if choice.lower() == 'investigate':
        print("Your exploration awakens the guardians of the temple.")
        negotiate_with_guardians()
    elif choice.lower() == 'leave':
        print("You take the treasure and leave the temple.")
        print("CONGRATULATIONS! You have successfully completed your quest and claimed the treasure.")
    else:
        print("Invalid choice. Please try again.")
        enter_temple()

def negotiate_with_guardians():
    print("The guardians of the temple awaken, determined to protect their treasure.")
    print("You attempt to reason with them.")

    choice = input("Do you choose to fight or negotiate? (fight/negotiate): ")
    if choice.lower() == 'fight':
        print("You engage the guardians in a fierce battle...")
        print("But you are overpowered and meet a tragic end. GAME OVER.")
    elif choice.lower() == 'negotiate':
        print("With diplomacy and cunning, you convince the guardians to let you leave peacefully.")
        print("CONGRATULATIONS! You have successfully navigated the dangers of the temple and emerged victorious.")
    else:
        print("Invalid choice. Please try again.")
        negotiate_with_guardians()

start_game()