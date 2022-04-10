print ("A * x + B = 0 -> Enter A and B, A not 0" )
print ("Enter A")
a = float(input())
print ("Enter B")
b = float (input())

if abs(0 - a) < 10 ** (-6) :
    print ("Wrong A")
else :
    print ("x = ", (-b) / a)