# Carlos Turibio

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True


def compile(entrada):
    reservedW = ["while","do"]
    operadores = ["<","=","+"]
    indentifiers =  ["i","j"]

    if (entrada[-1] == ";"):
        ter = entrada.find(";")    
    entrada = entrada[:-1].split(" ")
    print (entrada)
    print("Token, Identificação, Tamanho, Posição, ")
    cLen = 0
    for i,token in enumerate(entrada):
        if token in reservedW:
            print (token, ", Palavra Reservada, ",len(token), ", (0,",cLen, ");")
        elif isnumber(token):
            print (token, ", Constante, ",len(token), ", (0,",cLen, "); ")
        elif token in operadores:
            print (token, ", Operador, ",len(token), ", (0,",cLen, "); ")
            
        elif token in indentifiers:
            print (token, ", Identificador, ",len(token), ", (0,",cLen, "); ")
        cLen += len(token) + 1
    
    print (token, ", Terminador, ",len(token), ", (0,",ter, ");")

compile("while i < 100 do i = i + j;")
