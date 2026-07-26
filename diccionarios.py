# dic5=dict(ar1=9000,ar2=[3,54,2,1],ar3=(1,2,3,4),ar4={3:"A",90:"B"})

# dic2={9000: 'Hola', 'Key34': 8500, 8.45: (5, 6, 7, 8), (6-10j): [1, 1, 1, 1]}

# Out[29]: 
# {'ar1': 9000,
#  'ar2': [3, 54, 2, 1],
#  'ar3': (1, 2, 3, 4),
#  'ar4': {3: 'A', 90: 'B'}}

# dic6=dict(((20,900),("A",False)))

# FUNCION ZIP
# zip((0,5,6,7),"THY6")
# <zip at 0x1891f95ef40>

# PARA VISUALIZAR ZIP O RANGE SE HACE TYPECASTING CON LISTA O TUPLAS

# list(zip((0,5,6,7),"THY6"))
# [(0, 'T'), (5, 'H'), (6, 'Y'), (7, '6')]

# list(zip((0,5,6,7,4,5,6,2,3),"TasdHY6",list("324235232"),range(50)))

# [(0, 'T', '3', 0), ------> TUPLAS SEGUN CADA POSICION 0,0,0,0 o 1,1,1,1 etc segun elementos
#  (5, 'a', '2', 1),
#  (6, 's', '4', 2),
#  (7, 'd', '2', 3),
#  (4, 'H', '3', 4),
#  (5, 'Y', '5', 5),
#  (6, '6', '2', 6)]

# list(zip(range(100),"dasmdkaskdmasg334GG"))

# [(0, 'd'), ----------------> en este caso par
#  (1, 'a'),
#  (2, 's'),
#  (3, 'm'),
#  (4, 'd'),
#  (5, 'k'),
#  (6, 'a'),
#  (7, 's'),
#  (8, 'k'),
#  (9, 'd'),
#  (10, 'm'),
#  (11, 'a'),
#  (12, 's'),
#  (13, 'g'),
#  (14, '3'),
#  (15, '3'),
#  (16, '4'),
#  (17, 'G'),
#  (18, 'G')]

# dic7=dict(zip(range(100),"dasmdkaskdmasg334GG")) GUARDADO EN DICCIONARIO

# {0: 'd',
#  1: 'a',
#  2: 's',
#  3: 'm',
#  4: 'd',
#  5: 'k',
#  6: 'a',
#  7: 's',
#  8: 'k',
#  9: 'd',
#  10: 'm',
#  11: 'a',
#  12: 's',
#  13: 'g',
#  14: '3',
#  15: '3',
#  16: '4',
#  17: 'G',
#  18: 'G'}

# dic7.items() ------> Visualizar diccionario (No es lista, lo que esta dentro si, si se quiere lista hacer typecasting)

# dic7.keys() -----> Visualizar las keys del diccionario

# dic7.values() -----> Visualizar valores del diccionario sin la key

# dic7.get(15) ------> Visualizar valor del diccionario en base a la llaves

# dic1.update({0:333,2:"REEMPLAZO","k1":"valorR",(5,6):[1,1,1]}) ------> Actuliazcion de valor segun la key o agregacion de key mas elemento

# del(dic[9000]) ------> Eliminar un elemento asociado alguna llaves del diccionario

# dic2.clear() ------> Dejar el diccionario vacio o limpio

# dic4=dic2.copy() ------> Copiar elementos de un diccionario a otro en dic4 copiar lo de dic2 



