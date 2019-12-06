

table = [[]]
scope_counter = 0
dependencias = []
def pop_scope():
    table.pop()
    global scope_counter
    scope_counter -= 1

def symbol_lookup(var):
    found = False
    for scope in table:
        if var in scope:
            found = True
    if not found:
        print("SemanticError Name '{}' is not defined".format(var))
    return found

def new_scope():
    table.append([])
    global scope_counter
    scope_counter += 1
def add_symbol_to_dependencies(symbol):
    dependencias.append(symbol)

def add_symbol_to_scope(var):
    table[scope_counter].append(var)

def check_dependencies():
    for item in dependencias:
        if item not in table[0]:
            return False
    return True