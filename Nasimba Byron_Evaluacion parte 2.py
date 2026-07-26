from paquetedeber import mod1
from paquetedeber import mod2
from paquetedeber import mod3

while True:

    try:

        print("\nMENU")
        print("1 Ejecutar módulo 1")
        print("2 Ejecutar módulo 2")
        print("3 Ejecutar módulo 3")
        print("4 Salir")

        opcion=int(input("Seleccione una opción: "))

        if opcion==1:
            mod1.funcion1()

        elif opcion==2:
            mod2.funcion2()

        elif opcion==3:
            mod3.funcion5()

        elif opcion==4:
            break

        else:
            print("Opción no válida")

    except:
        print("Error: debe ingresar un número")

    else:
        print("Programa ejecutado correctamente")

    finally:
        print("Regresando al menú...")


