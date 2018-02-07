text = input('enter encrypt text: ')

text = text.replace(' ', '')
l = len(text)-len(text)%5
text = text[0:l]
print(text)
ab_text = ""
for i in text:
    if i.islower():
        ab_text+='a'
    else:
        ab_text+='b'
print(ab_text)

ab_list = list(ab_text)

print(ab_list)

ab = []

list_01=[]
for i in ab_list:
    if i == 'a':
        list_01.append("0")
    else:
        list_01.append("1")
print(list_01)
i=0      
while i<l:
    ab.append(int(list_01[i]+list_01[i+1]+list_01[i+2]+list_01[i+3]+list_01[i+4], 2)+97)
    
    i+=5
    
print(ab)
decrypt=""
for i in ab:
    decrypt+=chr(i)
    
print("decrypt word = "decrypt)

    


