#Realice una aplicación que le solicite a un usuario su color favorito, 
#su prenda de ropa favorita, un hobby, el año de su nacimiento, su peso 
#en kilogramos con dos números decimales, se debe almacenar el string 
#resultante y debe mostrarse el siguiente mensaje en pantalla:
#Finalmente guarde el string como una cadena sin formato RAW, 
#realice el ejercicio construyendo el string con al menos 3 métodos.

#STRING SIN METODOS 
    
print("Ejercicio Deber")
color=str(input("Ingrese su color favorito: "))
ropa=str(input("Ingrese su prenda de ropa favorita: "))
hobby=str(input("Ingrese su hobby: "))
fecha=int(input("Ingrese su año de nacimiento: "))
peso=float(input("Ingrese su peso en kilogramos (kg): "))

print("!Saludos!..")
print("Mi color favorito es: ", color, ",")
print("Mi prenda favorita es: ", ropa, ",")
print("Mi hobby: ", hobby,",")
print("Mi peso es: ",peso ,"Kilogramos.")
print("Hasta pronto...")

#STRING CON METODOS

#Primer ejemplo con FORMAT

texto1=("\n!Saludos!..\nMi color favorito es: {},\nMi prenda favorita es: {}\nMi hobby: {}\nNaci en: {} \nMi peso es: {} Kilogramos.\nHasta pronto...").format(color,ropa,hobby,fecha,peso)
print(texto1)

#Segundo ejemplo con "+"

texto2=("\n!Saludos!..\nMi color favorito es: "+color+"\nMi prenda favorita es: "+ropa+"\nMi hobby: "+hobby+"\nNaci en: "+str(fecha)+"\nMi peso es: "+str(peso)+" Kilogramos.\nHasta pronto...")
print(texto2)

#Tercer ejemplo con JOIN

texto3=["\n!Saludos!","\nMi color favorito es: ",str(color),",","\nMi prenda favorita es: ",str(ropa),",","\nMi hobby es: ",str(hobby),",","\nNací en: ",str(fecha),",","\nMi peso es: ",str(peso),",","\n¡Hasta Pronto!"]
resultado=" ".join(texto3)
print(resultado)


