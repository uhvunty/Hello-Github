a = int(input("Enter the number of digits of fibonacci sequence: "))
firstDigit = 0
secondDigit = 1
for i in range(a):
    print(firstDigit)
    zerothDigit = firstDigit
    firstDigit = secondDigit
    secondDigit = zerothDigit + firstDigit