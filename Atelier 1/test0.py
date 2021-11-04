#ex_1
def fact(i):
    if i==0:
        return 1
    else:
        return(i*(fact(i-1)))

nbr_termes=int(input("enter number of terms "))   
sum=0
for i in range(1,nbr_termes+1):
 sum=sum+fact(i)/i
print("la somme de la serie est :",sum)
#ex_2

def decimal_to_binary(n):
     resultat= ""       
     while(n !=0):
        r=int(n%2)
        n= int (n/2)
        resultat=str(r)+resultat
     return resultat
n= int( input("entrer le nombre en decimal: "))
print("le nombre on binaire est :" ,decimal_to_binary(n))


#ex_3

def som(x):
    if x==1:
     return 1
    elif x <=0:
         print(" entrer un nombre positive")
         
         
        
    else:
        return(x+som(x-1))
x=int(input("enter un nombre positif :"))
print(som(x))

 #ex_4  
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
    print(fibonacci(i))
    #ex_5
def  nbr_chiffres(n):   
        if( n < 10):
            return 1
        elif(n==0):
            return 10
        else:
            return 1 + nbr_chiffres(n/10)
n=int(input("entrer le nombre "))
print("le nomber des  chiffres est :" ,nbr_chiffres(n) ) 


#tri a bulle

def tri_a_bull(T):
    l=len(T)
    j=0
    permut=True
    while permut:

     permut=False
     j=j+1
     for i in range (0,l-j):
            print(T)
            if T[i]>T[i+1]:
                tmp=T[i]
                T[i]=T[i+1]
                t[i+1]=tmp
                permut=True 
    return T         
t=[5,12,8,4,14]
tri_a_bull(t)
#tri par sélection 
def tri_selection(T) :
    n=len(T)
    for i in range(0,n-1):
        MIN=T[i]
        indice=i
        for j in range(i+1,n):
            if T[j]<MIN:
                MIN=T[j]
                indice=j
        tmp =T[i]
        T[i]=T[indice]
        T[indice]=tmp
    return T
t=[5,12,8,4,14,0]
print(tri_selection(t))
# tri par insertion.
def tri_insertion(T):
    for i in range (len(T)):
        cle=T[i]
        j=i-1 # jest la position de l`element a inserer 
        while j>=0 and cle <T[j]:
            T[j],T[j+1]=T[j+1],T[j]
            j-=1
        
         
     
t=[5,12,8,4,14,0]
tri_insertion(t)
print(t)

#ex 7 
def inverse(ch):
    nv_ch=" "
    i=len(ch)-1
    while i>=0:
        nv_ch +=ch[i]
        i-=1
    return nv_ch
ch=str(input("entrer une chaîne de caractères:"))
print(inverse(ch))

#ex 8 
def frequence (ch):
    nbr=ch.count(n)
    return nbr
ch=str(input("entrer une chaîne de caractères. :"))
n=str (input("entrer le  caractère  n :"))
print(frequence(ch))
#ex 9
def trouver (a,m):
    for i in range (len (m)):
        for j in range(len (m[i])):
            if m [i][j]==a:
                return (i,j)


m=[[5,4],[7,12],[1,4]]
print (trouver(7,m))

#ex  1
def extract (l,g):
    h= []
    for i in range(0,len(g)):
        if i%2!=0:
            h.append(l[i])
    for i in  range(0,len(g)) :
     if i%2==0:
      h.append(g[i])
    return h     
     
l=[3, 6, 9, 12, 15, 18, 21]
g=[4, 8, 12, 16, 20, 24, 28]

print(extract(l,g))
#ex 2 
liste=[5,6,2,1,7,8,9,6,4,5,8,6]
x=len(liste)//3
y=2*len(liste)//3
    

nv_1list=liste[:x]
nv_2list=liste[x:y]
nv_3list=liste[y:]

print(nv_1list[::-1],nv_2list[::-1],nv_3list[::-1] ) 
#ex 3
l=[11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for i in l :
  if i in d:
      d[i]+=1
  else:
      d[i]=1
print (d)
#ex 4

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 ={57, 83, 29, 67, 73, 43, 48}

intersection = { x for x in set2 if x in set1}

print(intersection)
set1= {x for x in set1 if x not  in set2}
print(set1)
#ex 5
l=[47, 64, 69, 37, 76, 83, 95, 97,]
d={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
h=[]
for i  in l :
    if i   in  d.values ():
        h.append(i)

print(h)




    
     






 

        

