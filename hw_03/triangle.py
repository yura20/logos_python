a = int(input("enter length of first side of triangle :"))
b = int(input("enter length of second side of triangle :"))
c = int(input("enter length of third side of triangle :"))

if a<b+c and b<a+c and c<a+b:
	print("triangle with {a}, {b} and {c} side lengths is VALID".format(a = a, b = b, c = c))
else:
	print("triangle with {a}, {b} and {c} side lengths is INVALID".format(a = a, b = b, c = c))