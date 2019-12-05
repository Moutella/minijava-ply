from minijavaparse import result

print(result)
def uniqueprint(entrada):
    if type(entrada) == tuple:
        for item in entrada:
            uniqueprint(item)
    else:
        print(entrada)

def cgen(entrada):
    if type(entrada) == tuple:
        if entrada[0] == "mexp":
            cgenmexp(entrada)
        if entrada[0] == "sexp":
            cgensexp(entrada)
        for item in entrada:
            cgen(item)
    else:
        if type(entrada) == str:
            pass
        else:
            cgenint(entrada)


def cgenmexp(entrada):
    print("renato {}".format(entrada))
    if len(entrada) == 4:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        print("mul $a0 $t1 $a0")
        print("addiu $sp $sp 4")
    else:
        pass

def cgensexp(entrada):
    pass

def cgenint(entrada):
    print("li $a0 {}".format(entrada))

cgen(result) 
