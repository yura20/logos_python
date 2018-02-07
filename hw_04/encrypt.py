text = input('enter some text: ')
arr =[]
text = text.lower()
text = text.replace(' ', '')
print(text)
#print(ord(" "))
for i in text:
    z = bin(ord(i)-97)
    z = str(z[2:])
    while True:
        if len(z)<5:
            z='0'+z
        else:
            arr.append(z)
            break
i = 0
ab_str = ""
while i<len(arr):
    z = 0
    char = ""
    while z<5:
        if arr[i][z] == '0':
            char+='a'
        else:
            char+='b'
        z+=1
    ab_str+=char
    i+=1
print(ab_str)

sentence = input("enter a sentence :")

key = sentence.lower().replace(' ', '')
key = key[0:len(ab_str)]
i=0
while i<len(ab_str):
    if ab_str[i] == 'b':
        key=key[0:i]+key[i].upper()+key[i+1:len(key)]
    i+=1
print(key)
sentence=sentence.lower()
def phrase(sen="", key=""):
    i=0
    while i<len(sen):
        if sen[i]==" ":
            key = key[0:i]+" "+key[i:len(key)]
        i+=1
    return key
encrypt = phrase(sentence, key)
print(encrypt)
    