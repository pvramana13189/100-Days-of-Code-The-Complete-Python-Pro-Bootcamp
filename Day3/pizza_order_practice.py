print("Thank you for choosing Pythom Pizza Deliveries")
size = str(input())
add_pepparioni = str(input())
extra_cheese = str(input())

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid Size")

if add_pepparioni == "Y" and size == "S":
    bill += 2
elif add_pepparioni == "Y" and (size == "M" or size == "L"):
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")