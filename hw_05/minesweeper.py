x=int(input("enter x :"))
y=int(input("enter y :"))
arr=[]
bomb = int(input("enter amount of bombs :"))
bomb_list=[]
i=0
while i < bomb:
    first = int(input("enter x of bomb :"))
    second = int(input("enter y of bomb :"))
    bomb_list.append([first, second])
    i+=1
ii=0
for i in range(y):
    arr_2=[]
    jj=0
    for j in range(x):
        status = False
        for z in bomb_list:
            if z[0]-1 == ii and z[1]-1==jj:
                status = True
        if status:
            arr_2.append({
                "status": 'X'
            })
        else:
            arr_2.append({
                "status": 0
            })
        jj+=1
    ii+=1
    arr.append(arr_2)
def get_num(i, j):
    k=0
    ii=-1
    if arr[i][j]["status"] != 'X':
        while ii<=1:
            jj=-1
            while jj<=1:
                try:
                    if i+ii != -1 and j+jj !=-1:
                        if arr[i+ii][j+jj]["status"] == "X":
                            k+=1
                except IndexError:
                    k=k
                jj+=1
            ii+=1
    else:
        k="X"
    return k
    
i=0
while i<len(arr):
    j=0
    while j<len(arr[i]):
        arr[i][j]["status"]=str(get_num(i, j))
        j+=1
    i+=1

for i in arr:
    str_n=""
    for j in i:
        str_n+=j["status"]
    print(str_n)