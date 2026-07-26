# Parte 2

# Desarrollar un programa que permita validar la contraseña introducida por un usuario con las
# siguientes comprobaciones:
    
#Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
#Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
#Debe contener al menos un número entre 0 y 9.
#Debe contener un símbolo especial entre: $,%,*,@
#Tamaño mínimo de 5 caracteres y máximo de 15.

print("----------EJERCICIO 2-------------")
minus=["a","b","c","d","e","f","g","h","i","j"]
mayus=["K","L","M","N","O","P","Q","R","S","T"]
numeros=["0","1","2","3","4","5","6","7","8","9"]
simbolo=["$","%","*","@"]

while True:
    password=input("\nIngrese contraseña: ")

    check_minus = False
    check_mayus = False
    check_num = False
    check_simbolo = False

    for letra in password:
        if letra in minus:
            check_minus = True
        elif letra in mayus:
            check_mayus = True
        elif letra in numeros:
            check_num = True
        elif letra in simbolo:
            check_simbolo = True
            
    
    if check_minus == False:
        print("\nContraseña Incorrecta: Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
    
    if check_mayus == False:
        print("\nContraseña Incorrecta: Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T")
        
    if check_num == False:
        print("\nContraseña Incorrecta: Debe contener al menos un número entre 0 y 9.")
        
    if check_simbolo == False:
        print("\nContraseña Incorrecta: Debe contener un símbolo especial entre: $,%,*,@")
    
    if len(password) < 5 or len(password) > 15:
        print("\nContraseña Incorrecta: Tamaño mínimo de 5 caracteres y máximo de 15")
        
    if check_minus == True and check_mayus == True and check_num == True and check_simbolo == True and len(password) >= 5 and len(password) <= 15:
        print("Contraseña registrada correctamente")
        break
    
        
        