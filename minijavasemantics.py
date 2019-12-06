from minijavaparse import result, table
from symbol_table import *

def semantics_check(node):
    if type(node) == tuple:
        if node[0] == "main":
            add_symbol_to_scope(node[12])
            new_scope()
            semantics_check(node[15])
            pop_scope()
            pop_scope()
        elif node[0] == "classe":
            new_scope()
            if len(node) == 9:
                semantics_check(node[6])
                semantics_check(node[7])
            else:
                semantics_check(node[4])
                semantics_check(node[5])
            pop_scope()

        elif node[0] == "var":
            if type(node[1]) != tuple:
                symbol_lookup(node[1])
            add_symbol_to_scope(node[2])

        else:
            for item in node:
                semantics_check(item)
    else:
        pass
        # if type(entrada) == str:
        #     cgenstring(entrada)
        # else:
        #     cgenint(entrada)



check_dependencies()
new_scope()    
semantics_check(result)