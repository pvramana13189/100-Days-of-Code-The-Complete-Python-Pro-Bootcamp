firstNumber = int(input("Give the first number: "))
secondNumber = int(input("Give the second number: "))

difference = abs(firstNumber - secondNumber)
result = 0

if (firstNumber > secondNumber):
    print(1)
else:
    for i in range(difference+1):
        result += (firstNumber + i) ** 3

print(result)