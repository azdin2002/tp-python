def som(x): #en utiliser la recurrence 
    if x==1:
     return 1
    elif x <=0:
         print(" entrer un nombre positive")    
    else:
        return(x+som(x-1))
x=int(input("enter un nombre positif :"))
print("la somme des nombres de 1 à n est :", som(x))
