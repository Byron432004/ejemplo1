# FUNCIONES

# def nombre(parametros):
#     ins 1
#     ins 2
#     ins 3
#     return

#PRIMER ESCENARIO: NO recive datos NO entrega datos

def funcion1():
    """
    NO recibe datos No entrega datos
    """
    for c1 in range(4):
        for c2 in range(20):
            print("*",end="")
        print("\n",end="")
    return
    
#SEGUNDO ESCENARIO: SI recibe datos, NO entrega datos

def funcion2(base,altura):
    '''
    SI recibe datos NO entrega datos.
    "par1" - largo (int)
    "par2" - ancho (int)
    '''
    
    if type(base) == int and type(altura) == int:
        for v2 in range(base):
            for v1 in range(altura):
                print("@",end="")
            print("\n",end="")
    elif type(base) != int:
        print("La base es incorrecta, es un", {type(base)})
    elif type(altura) != int:
        print("La altura es incorrecta, es un ", {type(altura)})
    return

#TERCER ESCENARIO: NO recibe datos, SI entrega datos

def funcion3():
    """
    NO recibe datos, SI entrega datos

    """
    l1=list=["aeiou"]       
    l2=list=["áéióú"]    
    l3=list=["àèìòù"]    
    l4=list=["äëïöü"] 
    
    dic1=dict({0:l1,1:l2,2:l3,3:l4})
    return dic1

def funcion4():
    """
    NO recibe datos, SI entrega datos

    """
    l1=list=["aeiou"]       
    l2=list=["áéióú"]    
    l3=list=["àèìòù"]    
    l4=list=["äëïöü"] 
    
    dic1=dict(zip(range(10),(l1,l2,l3,l4)))
    return dic1

#CUARTO ESCENARIO: SI recibe datos, SI entrega datos
#Se hace operaciones y se guarda en el diccionario
def funcion5(n1,n2,n3,n4):
    """
    SI recibe datos, SI entrega datos

    """
    if type(n1) == int and type(n2) == int and type(n3) == int and type(n4) == int:
        suma=n1+n2+n3+n4
        resta=n1-n2-n3-n4
        multi=n1*n2*n3*n4
        if n2!=0 and n3!=0 and n4!=0:
            divi=n1/n2/n3/n4
        else:
            divi="ERROR div/0"
        dic1=dict({"suma":suma,"resta":resta,"multiplicacion":multi,"division":divi})
        return dic1
    elif type(n1) != int:
        print("Numero 1 incorrecto, es un", {type(n1)})
    elif type(n2) != int:
        print("Numero 2 incorrecto, es un ", {type(n2)})
    elif type(n3) != int:
        print("Numero 3 incorrecto, es un ", {type(n3)})
    elif type(n4) != int:
        print("Numero 4 incorrecto, es un ", {type(n4)})
    return 0
        
#QUINTO ESCENARIO ARGUMENTOS VARIABLES --- TRABAJA CON TUPLAS

def funcion6(*ndatos):
    """
    Argumentos variables
    
    """
    print(ndatos)
    print(type(ndatos))
    
    return

#SEXTO ESCENARIO ARGUMENTOS POR DEFECTO

def funcion7(p1,p2,p3=850000,p4="Defecto4"): #----->Se da valor en caso de no usarse se llena con ese valor dado
    return f"Primero: {p1}\nSegundo: {p2}\nTercero: {p3}\nCuarto: {p4}"

    
# print(funcion7(50,"Hola k ace",p4="Chespirito")) #------> si se quiere cambiar uno en especifico

#SEPTIMO ESCENARIO

def funcion8(n1,n2):
    suma=n1+n2
    resta=n1-n2
    multi=n1*n2
    return suma,resta,multi