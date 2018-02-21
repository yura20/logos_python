from sys import argv

filename = argv[-1]

def gen_lines(filename):
    f = open(filename, "r", encoding = "utf-8")
    for line in f:
        if len(line) > 40:
            yield line
    f.close()

for line in gen_lines(filename):
    print(line)
