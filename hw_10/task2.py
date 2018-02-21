from os import listdir
from os import getcwd
from os.path import isfile
from os.path import join as joinpath

def func(directory):
    file = []
    direct = []
    for i in listdir(directory):
        if isfile(joinpath(directory,i)):
            file.append(i)
        else:
            direct.append(i)
    return [directory, file, direct]
        
def gen_files(directory):
    arr = func(directory)
    yield arr
    i = 0
    while i<len(arr[2]):
        for x in gen_files(joinpath(arr[0], arr[2][i])):
            yield x
        i+=1
        
a = gen_files(getcwd());
for i in a:
    print(i)
#можна би було обрізати шлях весь лишній шлях до папки і виводити скорочений варіант шляху, але мені здається, що повний шлях виглядає краще і зрозуміліше

##хіба не простіше дане завдання так зробити?
#import os
#tree = os.walk(os.getcwd())
#for i in tree:
#    print(i)