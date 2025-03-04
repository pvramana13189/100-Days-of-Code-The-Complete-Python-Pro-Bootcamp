#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# MY ANSWER

# password = ""
# for letter in range(0, nr_letters):
#     password += letters[random.randint(0, len(letters) - 1)]
# for number in range(0, nr_numbers):
#     password += numbers[random.randint(0, len(numbers) - 1)]
# for symbol in range(0, nr_symbols):
#     password += symbols[random.randint(0, len(symbols) - 1)]
# print(f" Easy password is : {password}")

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# hard_password = ""
# new_array = [letters, numbers, symbols]
# # print(f"letters : {nr_letters}, numbers : {nr_numbers}, symbols : {nr_symbols}")

# while nr_letters != 0 or nr_numbers != 0 or nr_symbols != 0:
#     choice = new_array[random.randint(0,2)]
#     # print(choice)
#     # print(choice)
#     if choice == letters:
#         # print(f"letter {nr_letters}")
#         if nr_letters > 0:
#             hard_password += letters[random.randint(0, len(letters) - 1)]
#             nr_letters -= 1
#     elif choice == numbers:
#         # print(f"number {nr_numbers}")
#         if nr_numbers > 0:
#             hard_password += numbers[random.randint(0, len(numbers) - 1)]
#             nr_numbers -= 1
#     else:
#         # print(f"symbol {nr_symbols}")
#         if nr_symbols > 0:
#             hard_password += symbols[random.randint(0, len(symbols) - 1)]
#             nr_symbols -= 1

# print(f" Hard password is : {hard_password}")



# ANGELA's ANSWER

password1 = ""

for char in range(0, nr_letters):
    password1 += random.choice(letters)

for char in range(0, nr_numbers):
    password1 += random.choice(numbers)

for char in range(0, nr_symbols):
    password1 += random.choice(symbols)

print(f" Easy password1 is : {password1}")


password2 = []

for char in range(0, nr_letters):
    password2.append(random.choice(letters))

for char in range(0, nr_numbers):
    password2.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password2.append(random.choice(symbols))

random.shuffle(password2)

new_password = ""

for char in password2:
    new_password += char

print(f"New Password is : {new_password}")
    