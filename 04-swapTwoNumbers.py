x = 10
y = 20
print("Before Numbers were :")
print("x =", x, "\ny =",y)

temp = x
x = y
y = temp

print("after Numbers are :")
print("x =", x, "\ny =",y)

# In one line only in python
a = 4
b = 2
print("Before Numbers were :")
print("x =", a, "\ny =",b)
a,b = b,a 
print("after Numbers are :")
print("x =", a, "\ny =",b)