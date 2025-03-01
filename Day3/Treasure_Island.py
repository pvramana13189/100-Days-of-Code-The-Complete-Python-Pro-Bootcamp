print("Welcome to treasure island. \nYour mission is to find the treasuer.")
print('You\'re at a cross road. Where do you want to go Type "left" or "right"?')

choice = input()

if choice == "left":
    print('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across')

    choice = input()

    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")

        choice = input()

        if choice == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")