
lst1[1]=3500

lst1
Out[12]: [900, 3500, 98.45, 'test']

lst1.append(True)

lst1
Out[14]: [900, 3500, 98.45, 'test', True]

lst1.append([3,3,3])

lst1
Out[16]: [900, 3500, 98.45, 'test', True, [3, 3, 3]]


lst1.extend("UIO")

lst1
Out[18]: [900, 3500, 98.45, 'test', True, [3, 3, 3], 'U', 'I', 'O']

lst1.extend([3,3,3])

lst1
Out[20]: [900, 3500, 98.45, 'test', True, [3, 3, 3], 'U', 'I', 'O', 3, 3, 3]

lst1.insert(2,"200") ----> en la posicion 2 se remplaza

lst1
Out[22]: [900, 3500, '200', 98.45, 'test', True, [3, 3, 3], 'U', 'I', 'O', 3, 3, 3]

lst3.remove("j")

lst1.reverse

lst6=list("jasjdja434j@*/%ahsdh")

lst6.sort(reverse=True) ORDENA POR BIT

del(lst1[6]) ELIMINA UN ELEMENTO EN ESPECIFICO

lst1
Out[38]: [3, 3, 3, 'O', 'I', 'U', True, 'test', 98.45, '200', 3500, 900]

del(lst1) ELIMINA TODA LA LISTA


TUPLAS

tp1=(4,5,2,"a",[4,5,2],True)

tp1
Out[43]: (4, 5, 2, 'a', [4, 5, 2], True)

type(tp1)
Out[44]: tuple

tpl2=6,4,5,7,8,9

tuple([3,2,3,4,5])+tuple("sdasd32432")

tp1+tpl2
Out[52]: (4, 5, 2, 'a', [4, 5, 2], True, 6, 4, 5, 7, 8, 9)

("y","t",False)*5
Out[53]: 
('y',
 't',
 False,
 'y',
 't',
 False,
 'y',
 't',
 False,
 'y',
 't',
 False,
 'y',
 't',
 False)

lista5.count(2)
Out[63]: 3

lista5.index(2,4)
Out[64]: 4