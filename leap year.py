n = int(input("Enter a year:"))
if (n % 4 != 0):
    print("It is not a leap year")
elif (n % 4 == 0) and (n % 100 != 0):
    print("It is a leap year")
elif (n % 4 == 0) and (n % 100 == 0) and (n % 400 != 0):
    print("It is not a leap year")
elif (n % 4 == 0) and (n % 100 == 0) and (n % 400 == 0):
    print("It is a leap year")


