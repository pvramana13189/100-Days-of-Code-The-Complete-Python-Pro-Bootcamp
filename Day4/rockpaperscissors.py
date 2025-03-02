import random

game = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''
    _______
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
,
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissor? \n"))
system = random.randint(0,2)

# print(choice)
print(game[choice])

print("System chose:")
print(game[system])

if choice == system:
    print("Match Draw.")
elif choice == 0 and system == 1:
    print("You lose.")
elif choice == 0 and system == 2:
    print("You win.")
elif choice == 1 and system == 0:
    print("You win.")
elif choice == 1 and system == 2:
    print("You lose.")
elif choice == 2 and system == 0:
    print("You lose.")
elif choice == 2 and system == 1:
    print("You win.")
else:
    print("Invalid case.")