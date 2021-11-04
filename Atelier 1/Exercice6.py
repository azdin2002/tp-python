"""#tri a bulle

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
t=[5,12,8,4,14,10]
print(tri_selection(t))"""
# tri par insertion.
def tri_insertion(T):
    for i in range (len(T)):
        cle=T[i]
        j=i-1 # j est la position de l`element a inserer 
        while j>=0 and cle <T[j]:
            T[j],T[j+1]=T[j+1],T[j]
            j-=1
        
         
     
t=[5,12,8,4,14,19]
tri_insertion(t)
print(t)