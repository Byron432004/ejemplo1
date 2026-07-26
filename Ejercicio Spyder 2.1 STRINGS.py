'''
!Saludos!..
    Mi 'nombre' es Byron,
        me "apellido" Nasimba,
        tengo 20 años de edad,
        mi estatura es de 1.70 metros,
Hasta pronto...
'''

#PRIMER ESCENARIO

print("!Saludos!..")
print("    Mi 'nombre' es Byron,")
print('        me "apellido" Nasimba,')
print("         tengo 20 años de edad,")
print("        mi estatura es de 1.70 metros,")
print("Hasta pronto...")

#SEGUNDO ESCENARIO 
#-----> \t es tabulacion y \n salto de linea \ \ es para caracrteres especiales 

print("!Saludos!..\n\tMi 'nombre' es Byron,\n\tme \"apellido\" Nasimba,\n\ttengo 20 años de edad,\n\tmi estatura es de 1.70 metros,\nHasta pronto...") 

#TERCER ESCENARIO

nombre="Byron"
apellido="Nasimba"
edad=21
estatura=170.2 


print("!Saludos!..\n\tMi 'nombre' es ", nombre, ",\n\tme \"apellido\"", apellido, ",\n\ttengo", edad, "años de edad,", "\n\tmi estatura es de", estatura, "metros,\nHasta pronto...")



#CUARTO ESCENARIO

nombre="Byron"
apellido="Nasimba"
edad=21
estatura=170.2

print("!Saludos!..\n\tMi 'nombre' es ", nombre.title(), ",\n\tme \"apellido\"", apellido.capitalize(), ",\n\ttengo", edad, "años de edad,", "\n\tmi estatura es de",(estatura/100), "metros,\nHasta pronto...", sep="",end="\n")


#QUINTO ESCENARIO

nom="Byron"
ape="Nasimba"
ed=21
est=170.2 #esta en cm
rs1="¡Saludos!..\n\tMi 'nombre' es "+nom.title()+",\n\t\tme \"apellido\" "+ape.capitalize()+",\n\t\ttengo "+str(ed)+" años de edad,\n\tmi estatura es de "+str(round(est/100,2))+" metros,\nHasta pronto..."
print(rs1.upper())


#SEXTO ESCENARIO

var1="Primer dato: {1}\nSegundo dato: {1}\nTercer dato: {1}\nCuarto dato: {1}".format(8000,4.5,"Texto",9-1j)
print(var1)

var1="Primer dato: {a1}\nSegundo dato: {b2}\nTercer dato: {c3}\nCuarto dato: {d4}".format(a1=8000,b2=4.5,c3="Texto",d4=9-1j)
print(var1)

#METODO FORMTAR RELLENA LAS LLAVES DE UNA VARIALE CON ALGUN TIPO DE DATOS

nom="Byron"
ape="Nasimba"
ed=21
est=170.2 #esta en cm

var1=" ¡Saludos!..\n\tMi 'nombre' es {}\n\t\tme \"apellido\" {}\n\t\ttengo {} años de edad,\n\tmi estatura es de{}metros,\nHasta pronto...".format(nom,ape,ed,est)
print(var1)


#SEPTIMO ESCENARIO

nom="Byron"
ape="Nasimba"
ed=21
est=170.2 #esta en cm

#STRING F

var1=f" ¡Saludos!..\n\tMi 'nombre' es {nom.title()}\n\t\tme \"apellido\" {ape.capitalize()}\n\t\ttengo {str(ed)} años de edad,\n\tmi estatura es de{str(round(est/100,2))}metros,\nHasta pronto..."
print(var1)


#OCTAVO ESCENARIO
#STRING RPOUND

var1=r" ¡Saludos!..\n\tMi 'nombre' es {nom.title()}\n\t\tme \"apellido\" {ape.capitalize()}\n\t\ttengo {str(ed)} años de edad,\n\tmi estatura es de{str(round(est/100,2))}metros,\nHasta pronto..."
print(var1)


#NOVENO ESCENARIO

print("!Saludos!..\n\tMi 'nombre' es Byron,\n\tme \"apellido\" Nasimba,\n\ttengo 20 años de edad,\n\tmi estatura es de 1.70 metros,\nHasta pronto...") 

