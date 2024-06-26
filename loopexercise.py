#Getting the user input
usrinp = int(input("Enter a number: "))

#Check to see if the number is positive or negative
if usrinp > 0:
    print("This number is positive")
elif usrinp < 0:
    print("This number is negative")
else:
    print("This number is zero")

#Print all numbers from 1 to the number entered by the user (if positive)
if usrinp > 0:
    for i in range(1, usrinp + 1):
        print(i)