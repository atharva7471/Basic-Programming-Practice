while True:
    num = input("Enter a number = ")

    if num == "exit":
        print("Code exitted success!!")
        break

    else:
        num = int(num)
        if num == 0:
            print("Number is zero!")

        elif num > 0:
            print("Number is positive!")

        else:
            print("Number is Negative!")