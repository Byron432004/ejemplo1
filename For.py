for count in range(-3,10,3):
    print(count, end="  ")
    
for count in range(0,20,1):
    print(count, end="  ")
    
for count in range(20):
    if count in [5,10,15]:
        continue
    print(count, end="  ")
    
lst1=[4,6,8,2,6,3,4,8,10,12]
for count in lst1:
    if count%2!=0:
        print("\nNumero impar detectado:", count)
        break
    print(count, end="  ")