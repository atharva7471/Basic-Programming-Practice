num1 = int(input("Enter first Number = "))
num2 = int(input("Enter second Number = "))
num3 = int(input("Enter third Number = "))

if num1 > num2 > num3:
    print("Number ",num1, "is bigger than other two.")

elif num2 > num1 > num3:
    print("Number 2 is greater")

else:
    print("Number 3 is greater")