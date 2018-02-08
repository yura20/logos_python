list_1 = [1, 2, 3, 1, 4, 4.0, 5, 4, 5.1, "1", "1.0", True, False, True]

def del_repetition(arr=[]):
    i=0
    while i<len(arr):
        j=0
        while j<len(arr):
            if j != i:
                if arr[i] is arr[j]:
                    del list_1[j]
            j+=1
        i+=1
    return arr

print(del_repetition(list_1))

