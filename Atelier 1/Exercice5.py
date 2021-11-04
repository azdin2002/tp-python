def  nbr_chiffres(n):   
        if( n < 10):
            return 1
        elif(n==0):
            return 10
        else:
            return 1 + nbr_chiffres(n/10)
n=int(input("entrer un nombre: "))
print("le nomber des  chiffres est :" ,nbr_chiffres(n) ) 
