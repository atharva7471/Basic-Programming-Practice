x = int(input("Emter a number to obtain a fibonacci Series = "))

if x == 1:
    print(x)
else:
    print("Series :")

    for i in range(0, x+1):
        a = i
        b = i+1
        c = a+b
        print(c)
