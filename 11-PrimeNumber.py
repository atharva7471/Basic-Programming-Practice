num = int(input("Enter a Number ="))


for i in range(2,num):
    if num % i == 0:
        print("The Number is not a Prime Number!!")
        break

else :
    print("The Number is a Prime Number!!")