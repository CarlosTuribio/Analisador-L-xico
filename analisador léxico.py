# Carlos Turibio
def inArray(idenfity, simbolos):
    for i in simbolos:
        if idenfity == i[1]:
            return True
    return False

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def findToken(identify, simbolos):
    for i in simbolos:
        if i[1] == identify:
            return i[0]

def symbol(identify, simbolos):
    if len(simbolos) == 0:
        simbolos.append([len(simbolos)+1, identify ])
        return simbolos[-1][0]
    else:
        if inArray(identify, simbolos):
            return findToken(identify, simbolos)

        else:
            simbolos.append([len(simbolos)+1, identify ])
            return simbolos[-1][0]
            

def compile(entrada):
    
    cLen = 0
    tokens = []
    simbolos = []
    indentifiers = ["i","j"]
    operadores = ["<","=","+"]
    reservedW = ["while","do"]
    entrada = entrada[:-1].split(" ")
    print("--------------Tokens--------------------")
    print("Token, Identificação, Tamanho, Posição, ")
    for i,token in enumerate(entrada):
        tokensi = []
        if token in reservedW:
            tokensi.append(token)
            tokensi.append("Palavra Reservada")
        elif isnumber(token):
            tokensi.append(token)
            tokensi.append(["Identificador",symbol(token,simbolos)])
        elif token in operadores:
            tokensi.append(token)
            tokensi.append("Operador")
        elif token in indentifiers:
            tokensi.append(token)
            tokensi.append(["Identificador",symbol(token,simbolos)])


        tokensi.append(len(token))
        tokensi.append("(0,"+str(cLen)+")")

        tokens.append(tokensi)
        cLen += len(token) + 1
    tokens.append([";", "Terminador", "1", "(0,"+str(cLen-1)+")"])
    for i in tokens:    
        print(i)
    print("----------------------------------------\n")
    print("-------------Símbolos-------------------")
    for i in simbolos:
        print(i)


compile("while i < 100 do i = i + j;")
