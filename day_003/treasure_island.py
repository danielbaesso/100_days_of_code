print("Welcome to Treasue Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? "
                "Type 'Left' or 'Right' ").lower()

if choice1 == 'left':
    pass

else:
    print("You fell into a hole. GAME OVER! 💀💀💀")

choice2 = input("You've come to a lake. "
                "There is an island in the middle of the lake. "
                "Type 'wait' to wait for a boat. "
                "Type 'swim' to swim across. ").lower()

if choice2 == 'wait':
    pass

else:
    print("You were attacked by trout. GAME OVER 💀💀💀")

choice3 = input("You arrive at the island unharmed. "
                "There is house with 3 doors. One red, "
                "onde yellow, one blue. "
                "Wich colour do you choose?").lower()

if choice3 == 'red':
    print("You were burned by fire. GAME OVER 💀💀💀")

if choice3 == 'blue':
    print("You were eaten by beasts. GAME OVER 💀💀💀")

if choice3 == 'yellow':
    print("YOU WIN!🏆🏆")

else:
    print("GAME OVER 💀💀💀")
