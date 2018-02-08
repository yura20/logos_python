num_1 = int(input('enter first number :'))
num_2 = int(input('enter second number :'))

def cross_nums(num1="", num2=""):
    num1=str(num1)
    num2=str(num2)
    k=0
    i=0
    while i<len(num1):
        j=0
        while j<len(num2):
            if num1[i] == num2[j]:
                k+=1
            j+=1
        i+=1
        
    return k

print(cross_nums(num_1, num_2))