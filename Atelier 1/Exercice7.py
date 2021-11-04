def inverse(ch):
    nv_ch=" "
    i=len(ch)-1
    while i>=0:
        nv_ch +=ch[i]
        i-=1
    return nv_ch
ch=str(input("entrer une chaîne de caractères:"))
print(" l'inverse de cette chaîne de caractères est : " ,inverse(ch))