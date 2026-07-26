#sirva para capturar datos del usaurio variables n datos 

limite=int(input("Ingrese el numero de datos a ingresar: "))
lista= []
for count in range(limite):
    dato=input("Ingrese dato: ")
    lista.append(dato)
print("----------LISTA-------", "\n", lista)
