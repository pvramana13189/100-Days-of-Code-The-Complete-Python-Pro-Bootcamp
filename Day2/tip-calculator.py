print("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tipamount = 0.12 * bill
totalamount = tipamount + bill
share = totalamount/people
print(f"Each person should pay: {round(share,2)}")