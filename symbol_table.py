

table = [[]]
scope_counter = 0
dependencias = []
def pop_scope():
    table.pop()
    global scope_counter
    scope_counter -= 1

def symbol_lookup(var, line):
    found = False
    for scope in table:
        if var in scope:
            found = True
    if not found:
        print("SemanticError Name '{}' at line #{} is not defined".format(var, line))
    return found

def new_scope():
    table.append([])
    global scope_counter
    scope_counter += 1
def add_symbol_to_dependencies(symbol, line):
    dependencias.append([symbol, line])

def add_symbol_to_scope(var):
    if var in table[scope_counter]:
        print("Multiple definitions of {} at scope level {}".format(var, scope_counter))
    table[scope_counter].append(var)

def check_dependencies():
    for item in dependencias:
        exists = False
        if item[0] not in table[0]:
            print("Class '{}' referenced at line #{} is not defined".format(item[0], item[1]))
            return False
    return True