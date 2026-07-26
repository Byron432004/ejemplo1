#ESTRUCTURA WHILE HORIZONTAL
control=0
while control<=20:
    print(control,end="  ") 
    control+=1 #Se puede asi

#ESTRUCTURA WHILE VERTICAL
control=0
while control<=20:
    print(control,end="\n") 
    control=control+1 # Oh asi tambien
    
#CONTINUE PERMITE SALTAR LA REPETICION A LA SIGUIENTE y brake termina todo

num=0
while num<=20:
    if num==5 or num== 10 or num==15:
        num+=1
        continue
    print(num, end="  ")
    num+=1
else:
    print("Bloque Else")

#REPETIR DE OTRA MANERA
control="repetir"
num=0

while control=="repetir":
    print(num, end="  ")
    if num==15:
        control="detener"
    else:
        control="repetir"
    num+=1

#MENU

while True:
    var1=int(input("\nRepetir: 1. \nDetener: 2.\nOpcion: "))
    if var1==1:
        continue
    elif var1==2:
        break
    else:
        print("NO VALIDO")
        break
    

