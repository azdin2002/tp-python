def decimal_to_binary(n):
     resultat= ""       
     while(n !=0): #tante que le nombre on decimale  different 0
        r=int(n%2) #r est le reste de la division de n par 2 de tupe entier 
        n= int (n/2) #n on diviser n par 2 tante que ndifferent 0
        resultat=str(r)+resultat 
     return resultat
n= int( input("entrer le nombre en decimal: "))
print("le nombre on binaire est :" ,decimal_to_binary(n))