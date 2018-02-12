from sys import argv

file_name = argv[-1]
f = open("doil/"+file_name, "r", encoding="utf-8")
text = f.read()
f.close()
    
words = text.split()

def del_useless_symbols(arr=[]):
    i=0
    while i<len(arr):
        j=0
        while j<2:
#            тут я мушу ловити помилку, бо інколи такі символи як .,? і тд. являються в масиві окремим елементом
            try:
                if arr[i][0] == "!" or arr[i][0] == "?" or arr[i][0] == '"' or arr[i][0] == "'" or arr[i][0] == "," or arr[i][0] == "." or arr[i][0] == "-" or arr[i][0] == "“" or arr[i][0] == "‘" or arr[i][0] == ":" or arr[i][0] == ";":
                    arr[i]=arr[i][1:]
                if arr[i][-1] == "!" or arr[i][-1] == "?" or arr[i][-1] == '"' or arr[i][-1] == "'" or arr[i][-1] == "," or arr[i][-1] == "." or arr[i][-1] == "-" or arr[i][-1] == "”" or arr[i][-1] == "’" or arr[i][-1] == ":" or arr[i][-1] == ";":
                    arr[i]=arr[i][0:-1]
            except IndexError:
                del arr[i]
                i-=1
            j+=1
        i+=1
            
    return arr

def amount_of_w(arr=[]):
    obj = {}
    for i in arr:
        try:
            obj[i.lower()]+=1
        except KeyError:
            obj[i.lower()]=1
    return obj

#очищаємо масив слів від всякого трешу
words = del_useless_symbols(words)


#рахуємо кількість унікальних символів та к-сть всіх символів крім пробілу
symbol_arr = []
num_symbols = 0
for i in text:
    i = i.lower()
    symbol_arr.append(i)
    if i!=" ":
        num_symbols+=1

uniq_symbols = len(set(symbol_arr))
#кількість унікальних слів
uniq_words = len(set(words))
#кількість слів
num_words = len(words)

#формуємо строку для запису в файл
num_words = "Words: {}".format(str(num_words))
num_symbols = "Symbols: {}".format(str(num_symbols))
uniq_words = "Unique words: {}".format(str(uniq_words))
uniq_symbols = "Unique symbols: {}".format(str(uniq_symbols))
ready_to_write = "{} \n{} \n{} \n{} \n\namount of words, which > 30\n".format(num_words, num_symbols, uniq_words, uniq_symbols)

a_of_w = amount_of_w(words)
#додаємо до строки слова і їх кількість
for key in a_of_w:
    if a_of_w[key] >= 30:
        ready_to_write += "\n{} = {}".format(key, str(a_of_w[key]))

file_name = "results/"+file_name[:-4]+"_analytics.txt"
f = open(file_name, "w+", encoding="utf-8")
f.write(ready_to_write)
f.close()

print("Done. File saved!")