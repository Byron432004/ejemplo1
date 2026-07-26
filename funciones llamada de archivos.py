try:
    a=90
    b=0
    print(a/b)
    print("Bloque Try")
except:
    print("Bloque Except")
else:
    print("Bloque ELSE")
finally:
    print("Bloque Finally")

txt1=open("C:/Users/Lenovo LOQ/Desktop/Ejercicios Python/archivo1.txt",mode="r")

type(txt1)

txt1.read()

txt1.close()

txt1.readline() -----> Lee una linea

txt1.readlines() ---> LEE TODO EL DOCUMENTO Y DA UNA LISTA

txt1=open("C:/Users/Lenovo LOQ/Desktop/Ejercicios Python/archivo2.txt",mode="w") SE CREA NUEVO TXT y w para escribir

txt1.write("Texto de Ejemplo 1\n")

txt1=open("C:/Users/Lenovo LOQ/Desktop/Ejercicios Python/archivo1.txt",mode="a") AGREGA INFO EN EL MISMO

txt1.write("\n\nTEXTO ADICIONAL")