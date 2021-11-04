l=[47, 64, 69, 37, 76, 83, 95, 97,]
d={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
h=[]
for i  in l :
    if i   in  d.values ():#si on trouver i comme valeur du   d{}
        h.append(i)        #on ajouter i dans nouveau liste h[]

print("la liste apres la suppression: " ,h)
