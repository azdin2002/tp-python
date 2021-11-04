def extract (l,g):
    h= []
    for i in range(0,len(l)): #des éléments d'index impair dans la première liste.
        if i%2!=0:
            h.append(l[i])
    for i in  range(0,len(g)) :#des éléments d'index pair dans la 2 eme liste .
     if i%2==0:
      h.append(g[i])
    return h     
     
l=[3, 6, 9, 12, 15, 18, 21]
g=[4, 8, 12, 16, 20, 24, 28]

print("la resultat est : " ,extract(l,g))