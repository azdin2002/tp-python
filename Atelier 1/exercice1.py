def fact(i):
    if i==0:
        return 1
    else:
        return(i*(fact(i-1)))

nbr_termes=int(input("enter number of terms : "))   
sum=0
for i in range(1,nbr_termes+1):
 sum=sum+fact(i)/i
print("la somme de la serie est :",sum)