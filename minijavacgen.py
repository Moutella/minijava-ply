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
        elif entrada[0] == "sexp":
            cgensexp(entrada)
        else:
            for item in entrada:
                cgen(item)
    else:
        if type(entrada) == str:
            pass
        else:
            cgenint(entrada)


def cgenmexp(entrada):
    if len(entrada) == 4:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        print("mul $a0 $t1 $a0")
        print("addiu $sp $sp 4")
    else:
        cgen(entrada[1])

def cgensexp(entrada):
    cgen(entrada[1])

def cgenint(entrada):
    print("li $a0 {}".format(entrada))

cgen(result) 
