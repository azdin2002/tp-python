l=[11, 45, 8, 11, 23, 45, 23, 45, 89]
d={} #on declarer un dictionnaire vide
for i in l :
  if i in d:#si l'element i on a deja dans d {}
      d[i]+=1   #d{i:d[i]+1}
  else:
      d[i]=1  #d{i:d[i]}
print (" le dictionnaire :", d)