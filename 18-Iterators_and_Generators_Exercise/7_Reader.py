def read_next(*args):
    for i in args:
        for el in i:
            yield el


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)