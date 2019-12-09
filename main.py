from minijavaparse import result
from minijavasemantics import *
from minijavacgen import *

if erros_atuais:
    print("Código não será gerado por possuir erros no programa")
else:
    cgen(result)