print("""
Welcome to Treasure Island!
Your mission is to find the treasure...
""")
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input("You see a tunnel. Do you go through or walk around? Type 'through' or 'around': ").lower()
    if choice2 == "through":
        print("Troll killed you. Game over.")
    elif choice2 == "around":
        choice3 = input("You walked around. Now you're faced with a cliff. Do you go back or climb down? Type 'back' or 'down': ").lower()
        if choice3 == "down":
            print("You fell. You dead.")
        else:
            print("You left. No adventure for you.")
    else:
        print("Wtf are you typing?")
elif choice1 == "right":
    choice3 = input("You approach a draw bridge. Do you cross it or turn back? Type 'cross' or 'turn': ").lower()
    if choice3 == "cross":
        choice4 = input("You see a mighty Queen. Do you bow or wave? Type 'bow' or 'wave': ").lower()
        if choice4 == "bow":
            print("You found the treasure! You win!")
        elif choice4 == "wave":
            print("Dummy. You dead.")
    elif choice3 == "turn":
        print("You've lost the adventurer in you.")

else:
    print("You die")
