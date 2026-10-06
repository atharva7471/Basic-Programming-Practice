num = int(input("Enter a Number = "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    cube = digit**3
    sum = sum + cube
    temp = temp // 10

if sum == num:
    print("The given number",num," is Armstrong number!!")
else:
    print("The given number",num," is not an Armstrong number!!")
