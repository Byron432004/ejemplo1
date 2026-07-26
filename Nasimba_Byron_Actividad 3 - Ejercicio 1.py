
def calcular(valores, altos, bajos):

    valores_ordenados = sorted(valores)

    valores_bajos = valores_ordenados[:bajos]

    valores_altos = sorted(valores, reverse=True)[:altos]

    resultado = valores_altos + valores_bajos

    return resultado


dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}

dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}

dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}

dic4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56],"lst3":[12,31,87,1,0,4,-11]}


while True:

    opcion=int(input("\nMenu de Opciones \n1. Demostración del cálculo de valores altos y bajos en diccionarios. \n2.Salir. \nEscoja una opción: "))

    if opcion==1:

        while True:

            diccionarios=int(input("\n1.{Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37} \n2.{tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)} \n3.{val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92} \n4.{lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56],lst3:[12,31,87,1,0,4,-11]} \nElija un diccionario para la demostración:"))

            if diccionarios == 1:
                dic = dic1
                break

            elif diccionarios == 2:
                dic = dic2
                break

            elif diccionarios == 3:
                dic = dic3
                break

            elif diccionarios == 4:
                dic = dic4
                break

            else:
                print("Diccionario no existente")

        valores=[]

        for v in dic.values():

            if type(v)==tuple or type(v)==list:
                for n in v:
                    valores.append(n)

            else:
                valores.append(v)

        while True:

            altos=int(input("Digite el número de valores altos que desea mostrar: "))
            bajos=int(input("Digite el número de valores bajos que desea mostrar: "))

            if altos + bajos > len(valores):
                print("Error: cantidad mayor al número de datos")

            else:
                break

        resultado = calcular(valores,altos,bajos)

        print("Valores calculados en formato LISTA:",resultado)

        print("Valores calculados en formato TUPLA:",tuple(resultado))


    elif opcion==2:
        break

    else:
        print("OPCIÓN NO VALIDA")