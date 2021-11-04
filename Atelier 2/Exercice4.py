set1 = {23, 42, 65, 57, 78, 83, 29}
set2 ={57, 83, 29, 67, 73, 43, 48}

intersection = { x for x in set2 if x in set1}

print(" intersection de deux sites est :" ,intersection)
set1= {x for x in set1 if x not  in set2}
print("Set 1 après suppression : ",set1)