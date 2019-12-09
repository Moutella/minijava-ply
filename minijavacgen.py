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
        if entrada[0] == "rexp":
            cgenrexp(entrada)
        elif entrada[0] == "aexp":
            cgenaexp(entrada)
        elif entrada[0] == "mexp":
            cgenmexp(entrada)
        elif entrada[0] == "sexp":
            cgensexp(entrada)
        elif entrada[0] == "cmd":
            cgencmd(entrada)
        elif entrada[0] == "metodo":
            cgenmetodo(entrada)
        elif entrada[0] == "params":
            cgenparams(entrada)
        elif entrada[0] == "var":
            cgenvar(entrada)
        else:
            for item in entrada[:-1]:
                cgen(item)
    else:
        if type(entrada) == str:
            cgenstring(entrada)
        else:
            cgenint(entrada)

def add_param_counter():
    global paramcounter
    paramcounter += 1
def restart_param_counter():
    global paramcounter
    paramcounter = 2

def cgenparams(entrada):
    if(len(entrada) == 4):
        print("lw $a0 4($fp)")
        print("sw $a0 0($sp)")
        print("addi $sp $sp -4")
    elif len(entrada) == 6:
        print("lw $a0 %d($fp)"%(paramcounter*4))
        print("sw $a0 0($sp)")
        print("addi $sp $sp -4")
        add_param_counter()
        cgenparams(entrada[1])

def cgenmetodo(entrada):
    label_func = entrada[3]
    print("{}:".format(label_func))
    print("move $fp $sp")
    print("sw $ra 0($sp)")
    print("addiu $sp $sp -4")
    cgen(entrada[5])
    # cgen(entrada[8])
    print("Print metodo!", entrada[5])
    cgen(entrada[9])
    cgen(entrada[11])

def cgencmd(entrada):
    if len(entrada) == 9 and entrada[1] == "if":
        cgen(entrada[3])
        current_branch = branchcounter
        label_else = "branch_else{}".format(current_branch)
        label_end = "branch_end{}".format(current_branch)
        print("beq $a0 $zero {}".format(label_else))
        cgen(entrada[5])
        print("j {}".format(label_end))
        print("{}:".format(label_else))
        cgen(entrada[7])
        print("{}:".format(label_end))
        add_branch_counter()
    elif len(entrada) == 7 and entrada[1] == "if":
        cgen(entrada[3])
        current_branch = branchcounter
        label_end = "branch_end{}".format(current_branch)
        print("beq $a0 $zero {}".format(label_end))
        cgen(entrada[5])
        print("{}:".format(label_end))
        add_branch_counter()
    elif len(entrada) == 7 and entrada[1] == "while":
        current_branch = branchcounter
        label_while = "branch_while{}".format(current_branch)
        label_end = "branch_end{}".format(current_branch)

        print("{}:".format(label_while))
        cgen(entrada[3])
        print("beq $a0 $zero {}".format(label_end))
        cgen(entrada[5])

        print("j {}".format(label_while))
        print("{}:".format(label_end))
    elif len(entrada) == 7 and entrada[1] == "System.out.println":
        print("li $v0, 1")
        cgen(entrada[3])
        print("syscall")
    elif len(entrada) == 9 and entrada[1] != "if":
        cgen(entrada[3])
        print("sw $a0 0($sp)") #salva a posicao do array
        print("addiu $sp $sp -4")
        cgen(entrada[6])
        print("sw $a0 0($sp)")  #salva o resultado da expressao
        print("addiu $sp $sp -4")
        print("la $a0 {}".format(entrada[1])) #pega o endereco da variavel
        print("lw $t1 4($sp)")        #pega o resultado da expressao em sp
        print("lw $t2 8($sp)")        #pega a posicao do array em sp
        print("muli $t2 $t2 4")        #multiplica a posicao do array por 4(tamanho do inteiro)
        print("add $a0 $a0 $t1")        #pega a memoria do elemento do array
        print("sw $t1 0($a0)")
        print("addiu $sp $sp 8")
    elif len(entrada)==6:
        cgen(entrada[3])
        print("move $t1 $a0")
        print("la $a0 {}".format(entrada[1]))
        print("sw $t1 0($a0)")

    else:
        for item in entrada[:-1]:
            cgen(item)

def cgenexp(entrada):
    if len(entrada) == 5:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        current_branch = branchcounter
        label = "branch_{}".format(current_branch)
        label_end = "branch_end{}".format(current_branch)
        print("beq $a0 $zero {}".format(label))
        print("beq $t1 $zero {}".format(label))
        print("li $a0 1")
        print("j {}".format(label_end))
        print("{}:".format(label))
        print("li $a0 0")
        print("{}:".format(label_end))
        print("addiu $sp $sp 4")
        add_branch_counter()
    else:
        cgen(entrada[1])


def cgenrexp(entrada):
    if len(entrada) == 5:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        if entrada[2] == "<":
            print("slt $a0 $t1 $a0")
        elif entrada[2] == "==":
            current_branch = branchcounter
            label = "branch_{}".format(current_branch)
            label_end = "branch_end_{}".format(current_branch)
            label_true = "branch_true_{}".format(current_branch)
            print("beq $a0 $t1 {}".format(label))
            print("li $a0 0")
            print("j {}".format(label_end))
            print("{}:".format(label_true))
            print("li $a0 1")
            add_branch_counter()
        else:
            current_branch = branchcounter
            label = "branch_{}".format(current_branch)
            label_end = "branch_end_{}".format(current_branch)
            label_true = "branch_true_{}".format(current_branch)
            print("beq $a0 $t1 {}".format(label))
            print("li $a0 1")
            print("j {}".format(label_end))
            print("{}:".format(label_true))
            print("li $a0 0")
            add_branch_counter()
        print("addiu $sp $sp 4")
    else:
        cgen(entrada[1])
def cgenaexp(entrada):
    if len(entrada) == 5:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        print("{} $a0 $t1 $a0".format("add" if entrada[2] == "+" else "sub"))
        print("addiu $sp $sp 4")
    else:
        cgen(entrada[1])

def cgenvar(entrada):
    if type(entrada[1]) == tuple:
        if entrada[1][1] == "boolean":
            print("{}: .byte 2")
        elif entrada[1][1] == "int":
            if type(entrada[1])==bool:
                print("{}: .word 4".format())
            else:
                print("{}: .word 64")
                
    else:
        pass


def cgenmexp(entrada):
    if len(entrada) == 5:
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
    if len(entrada) == 4:
        cgen(entrada[2])
        if entrada[1] == '!':
            current_branch = branchcounter
            label = "branch_{}".format(current_branch)
            labelend = "branch_end_{}".format(current_branch)
            print("beq $a0 $zero {}".format(label))
            add_branch_counter()
            print("li $a0 0")
            print("j {}".format(labelend))
            #if branch true
            print("{}: ".format(label))
            print("li $a0 1")
            print("{}: ".format(labelend))
        else:
            print("sub $a0 $zero $a0")
    elif len(entrada) == 6:
        if type(entrada[1]) != tuple:
            cgen(entrada[3])
            print("sw $a0 0($sp)")  #salva o resultado da expressao
            print("addiu $sp $sp -4")
            print("la $a0 {}".format(entrada[1])) #pega o endereco da variavel
            print("lw $t1 4($sp)")        #pega a posicao do array em sp
            print("muli $t1 $t1 4")        #multiplica a posicao do array por 4(tamanho do inteiro)
            print("add $a0 $a0 $t1")
            print("lw $a0 0($a0)")
            print("addiu $sp $sp 4")
    elif len(entrada)==3:
        if entrada[1]!="true" and entrada[1]!="false" and type(entrada[1])==str:
            print("la $a0 {}".format(entrada))


def add_branch_counter():
    global branchcounter
    branchcounter += 1

def cgenint(entrada):
    print("li $a0 {}".format(entrada))

def cgenstring(entrada):
    if entrada == "true":
        print("li $a0 1")
    elif entrada == "false":
        print("li $a0 0")


def cgenpexp(entrada):
    if len(entrada) == 8:
        pass


branchcounter = 0
paramcounter = 2
cgen(result)
