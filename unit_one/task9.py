#the first version
print("Enter X, Y, Z")
x = int(input("Enter X:"))
y = int(input("Enter Y:"))
z = int(input("Enter Z:"))
if x > y & x > z:
    max_ = x
elif y > z:
    max_ = y
else:
    max_ = z
print("Maximum = ", max_)

#the second version
m = input("Enter X Y Z").split(" ")
print("Maximum = ", int(max(m)))