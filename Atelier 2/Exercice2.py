liste=[5,6,2,1,7,8,9,6,4,5,8,6]
x=len(liste)//3 # on Deviser la liste en 3 morceaux égaux
y=2*len(liste)//3
    

nv_1list=liste[:x]
nv_2list=liste[x:y]
nv_3list=liste[y:]
#et inverser chaque morceau danc la fonction print
print( "Deviser la liste en 3 et inverser : ", nv_1list[::-1],nv_2list[::-1],nv_3list[::-1] ) 
