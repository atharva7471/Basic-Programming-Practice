lower = int(input("Enter Lower value : "))
upper = int(input("Enter higher value : "))

for num in range(lower, upper):
    if num > 1:   
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

