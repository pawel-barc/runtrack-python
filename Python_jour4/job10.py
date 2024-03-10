L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
 
paires =sum(x for x in L if x>24 and x<91)
print(paires)