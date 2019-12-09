

table = [[]]
scope_counter = 0
dependencias = []
method_list = {}
classless_methods = []

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

def add_method_queue(method):
    classless_methods.append(method)

def current_class(classe):
    for method in classless_methods:
        add_method(classe, method)

def add_method(classe, method):
    if method in classless_methods:
        if classe in method_list:
            method_list[classe].update(method)
        else:
            method_list[classe] = method
        classless_methods.remove(method)

def search_method(classe, method, linenumber=0):
    if classe in method_list:
        if method in method_list[classe]:
            pass
        else:
            print("Method {} referenced at line {} from class {} is not defined".format(method, linenumber, classe))
    else:
        print("Method {} referenced at line {} from class {} is not defined".format(method, linenumber, classe))

def verify_method_params(num, method, classe, linenumber=0):
    if classe in method_list:
        if method in method_list[classe]:
            if num == method_list[classe][method]['size']:
                return True
            print("Method {} referenced at line {} from class {} is being called with the wrong number of parameters".format( method, linenumber, classe))