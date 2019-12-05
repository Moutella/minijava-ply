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
        else:
            for item in entrada:
                cgen(item)
    else:
        if type(entrada) == str:
            cgenstring(entrada)
        else:
            cgenint(entrada)
def cgenexp(entrada):
    if len(entrada) == 4:
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
    if len(entrada) == 4:
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
            print("beq $a0 $t1 {}".format(label))
            print("li $a0 0")
            print("j {}".format(labelend))
            print("{}:".format(labeltrue))
            print("li $a0 1")
            add_branch_counter()
        else:
            current_branch = branchcounter
            label = "branch_{}".format(current_branch)
            label_end = "branch_end_{}".format(current_branch)
            print("beq $a0 $t1 {}".format(label))
            print("li $a0 1")
            print("j {}".format(labelend))
            print("{}:".format(labeltrue))
            print("li $a0 0")
            add_branch_counter()
        print("addiu $sp $sp 4")
    else:
        cgen(entrada[1])
def cgenaexp(entrada):
    if len(entrada) == 4:
        cgen(entrada[1])
        print("sw $a0 0($sp)")
        print("addiu $sp $sp -4")
        cgen(entrada[3])
        print("lw $t1 4($sp)")
        print("{} $a0 $t1 $a0".format("add" if entrada[2] == "+" else "sub"))
        print("addiu $sp $sp 4")
    else:
        cgen(entrada[1])

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
    if len(entrada) == 3:
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
    else:
        cgen(entrada[1])

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

branchcounter = 0
cgen(result) 
