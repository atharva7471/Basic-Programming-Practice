while True:
    num = input("Enter a Number = ")

    if num == "exit":
        print("Sucessfully exited!!")
        break

    else:
        num = int(num)

        if num % 2 == 0:
            print("Number is even!!")

        else :
            print("Number is odd!!")