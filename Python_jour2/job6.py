#En utilisant le Crible d'Ératosthène
for x in range(2,1001):
    if x %2 == 0 and x >2:
        continue
    elif x %3 == 0 and x >3:
        continue
    elif x %5 == 0 and x>5:  
        continue
    else:
        print(x)