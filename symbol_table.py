

table = []
scope_counter = 0
def new_scope(s):
    table.append(s)
    scope_counter+=1

def pop_scope():
    table.pop()
    scope_counter -= 1

def symbol_lookup(var):
    found = False
    for scope in table:
        if var in scope:
            found = True
    if not found:
        print("SemanticError Name '{}' is not defined".format(var))
    return found

def add_symbol_to_scope(var):
    table[-1].append(var)
