def trouver (a,m):
    for i in range (len (m)):
        for j in range(len (m[i])):
            if m [i][j]==a:
                return (i,j)


m=[[5,4],[7,12],[1,9]]
print  (" la position de 7" ,trouver(7,m))
print(" la position de 1",trouver(1,m))
print (" la position de 9" ,trouver(9,m))
