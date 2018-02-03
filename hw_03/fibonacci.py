fib_num = [0, 1]
i = 2
z = int(input('enter index of fibonacci number: '))
while i<=z:
	fib_num.append(fib_num[i-2] + fib_num[i-1])
	i+=1
print("fibonacci number[{index}] = {fib_num}".format(index = z, fib_num = fib_num[z]))