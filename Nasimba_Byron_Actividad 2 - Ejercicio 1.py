#Parte 1
#Considerando la siguiente tupla codifique un programa que permita separar los números pares
#e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.

Datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
for count in Datos_2021:
    print("\n--------------Menu de Opciones-------------")
    menu1=(int(input("1.Numeros Pares \n2.Numeros Impares \n3.Salir de menu \nEscoger una opcion: ")))
    if menu1==1:
        print("\nNUMEROS PARES")
        for count in Datos_2021:
            if count%2==0:
                print(count, end=" ")
    if menu1==2:
        print("\nNUMEROS INPARES")
        for count in Datos_2021:
            if count%2!=0:
                print(count, end="  ")
    if menu1==3:
        print("\nSALIENDO DEL MENU")
        break
    
                
        
        
             
        
        
    
