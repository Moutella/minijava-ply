from minijavaparse import result

print(result)
def uniqueprint(entrada):
    if type(entrada) == tuple:
        for item in entrada:
            uniqueprint(item)
    else:
        print(entrada)


uniqueprint(result)

def cgen(entrada):
    if type(entrada) == tuple:
        for item in entrada:
            cgen(item)
    else:
        if type(entrada) == str:
            cgenstring(entrada)
        else:
            cgenint(entrada)


def cgenstring(entrada):
    pass
def cgenint(entrada):
    print("li $a0 {}".format(entrada))
cgen(result) 