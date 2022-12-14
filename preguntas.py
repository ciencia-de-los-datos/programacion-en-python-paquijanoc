"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    resultado=0
    columna2 = [row[1] for row in datos]
    for x in columna2:
        resultado= resultado + int(x)
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return resultado


def pregunta_02():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna1 = [row[0] for row in datos]
    from collections import Counter
    cnt = Counter()
    for word in columna1:
        cnt[word] += 1
    lista=list(cnt.items())
    lista.sort()
    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    return  lista


def pregunta_03():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna1_2 = [row[:2] for row in datos]
    conver = [(row[0], int(row[1])) for row in columna1_2]
    respuesta =[(k, sum([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    respuesta.sort()

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return respuesta


def pregunta_04():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna3 = [row[2] for row in datos]
    fechasep = [line.split("-") for line in columna3]
    meses = [row[1] for row in fechasep]
    from collections import Counter
    cnt = Counter()
    for word in meses:
        cnt[word] += 1
    lista=list(cnt.items())
    lista_or=sorted(lista,reverse=False)

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return lista_or


def pregunta_05():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna1_2 = [row[:2] for row in datos]
    conver = [(row[0], int(row[1])) for row in columna1_2]
    respuesta =[(k, max([y for (x,y) in conver if x == k]), min([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    respuesta.sort()
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return respuesta


def pregunta_06():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t","/") for line in datos]
    datos = [line.split("/") for line in datos]
    columna5 = [row[4] for row in datos]
    columna5 = [line.split(",") for line in columna5]
    lista5 = []
    for item in columna5:
        lista5 += item
    lista5 = [item.split(":") for item in lista5]
    conver = [(row[0], int(row[1])) for row in lista5]
    respuesta =[(k, min([y for (x,y) in conver if x == k]), max([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    respuesta.sort()

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return respuesta


def pregunta_07():
    
    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna1_2 = [row[:2] for row in datos]
    conver = [(int(row[1]),row[0]) for row in columna1_2]
    prueba=[]
    rta=[(k, prueba.append([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    num = [row[0] for row in rta]
    union = zip(num,prueba)
    respuesta=list(union)
    respuesta.sort()
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return respuesta


def pregunta_08():
    
    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t",",") for line in datos]
    datos = [line.split(",") for line in datos]
    columna1_2 = [row[:2] for row in datos]
    conver = [(int(row[1]),row[0]) for row in columna1_2]
    prueba=[]
    rta=[(k, prueba.append([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    num = [row[0] for row in rta]
    prueba2=[]
    for item in prueba:
        x = sorted(list(set(item)))
        prueba2.append(x)
    union = zip(num,prueba2)
    respuesta=list(union)
    respuesta.sort()

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return respuesta


def pregunta_09():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t","/") for line in datos]
    datos = [line.split("/") for line in datos]
    columna5 = [row[4] for row in datos]
    columna5 = [line.split(",") for line in columna5]
    lista5 = []
    for item in columna5:
        lista5 += item
    lista5 = [item.split(":") for item in lista5]
    claves = [row[0] for row in lista5]

    from collections import Counter
    d1 = Counter(claves)
    lista = list(d1.items())
    lista.sort()
    respuesta=dict(lista)

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return respuesta


def pregunta_10():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t","/") for line in datos]
    datos = [line.split("/") for line in datos]
    columna1 = [row[0] for row in datos]
    columna4=[row[3] for row in datos]
    columna4 = [line.split(",") for line in columna4]
    num4=[]
    for item in columna4:
        num4 += str(len(item))
    num4=[int(x) for x in num4]

    columna5=[row[4] for row in datos]
    columna5 = [line.split(",") for line in columna5]
    num5=[]
    for item in columna5:
      num5 += str(len(item))
    num5=[int(x) for x in num5]

    union = zip(columna1,num4,num5)
    respuesta=list(union)

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return respuesta


def pregunta_11():
    
    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t","/") for line in datos]
    datos = [line.split("/") for line in datos]

    columna4 = [row[3] for row in datos]
    columna4= [line.split(",") for line in columna4] 
    letras = []
    for item in columna4:
      letras += item #Separo las letras en una lista simple

    columna2 = [row[1] for row in datos]
    num4=[]
    for item in columna4:
      num4 += str(len(item))
    num4=[int(x) for x in num4] #Obtengo los tamaños de los string en las letras

    numeros = [x  for x,y in zip(columna2,num4)
                 for x in [x]*y]
    numeros=[int(x) for x in numeros] #Multiplico la cant de veces de las letras por los numeros

    conver=[]
    for lista, dato in zip(letras, numeros):
        a=(lista,dato)
        conver.append(a) 

    respuesta =[(k, sum([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    respuesta.sort()
    respuesta=dict(respuesta)   

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return respuesta


def pregunta_12():

    with open('data.csv', "r") as file:
        datos = file.readlines()  #Me devuelve una lista de strings
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.replace("\t","/") for line in datos]
    datos = [line.split("/") for line in datos]
    columna5 = [row[4] for row in datos]
    columna5 = [line.split(",") for line in columna5]
    valores = []
    for item in columna5:
      valores += item #Separo las letras en una lista simple
    valores = [line.split(":") for line in valores]
    valores=[row[1] for row in valores]
    valores=[int(x) for x in valores]


    columna1 = [row[0] for row in datos]
    num5=[]
    for item in columna5:
      num5 += str(len(item))
    num5=[int(x) for x in num5] #Obtengo los tamaños de los string en las letras

    claves = [x  for x,y in zip(columna1,num5)
                 for x in [x]*y] #Multiplico la cant de letras
 
    conver=[]
    for lista, dato in zip(claves,valores):
      a=(lista,dato)
      conver.append(a) #Uno numeros con letras, ya aqui estan con la misma cant de datos

    respuesta =[(k, sum([y for (x,y) in conver if x == k])) for k in dict(conver).keys()]
    respuesta.sort()
    respuesta=dict(respuesta)
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return respuesta
