import random

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

from hanman_words import word_list

lives = 0

chosen_word = random.choice(word_list)

# print(chosen_word)

placeholder = ""

for char in chosen_word:
    placeholder += "_"

print(f"{placeholder}\n")

choosen_letters = []

print(f"The length of the choosen word is: {len(chosen_word)}")

game_over = False

while not game_over:

    display = ""

    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
            choosen_letters.append(guess)
        elif letter in choosen_letters:
            display += letter
        else:
            display += "_"
    
    if guess not in display:
        lives += 1
        # print(HANGMAN[lives])

    if lives == 6:
        print("You loose.")
        game_over = True
        print(f"The Chose word is : {chosen_word}")

    print(display)
    print(HANGMAN[lives])
    print(f"You have {6-lives} lives.")

    if "_" not in display:
        print("You Win.")
        game_over = True

