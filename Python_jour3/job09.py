def moyenne(note1,note2,note3):
    return (note1+note2+note3) /3

note1 = float(input("Tape la note1"))
note2 = float(input("Tape la note2"))
note3 = float(input("Tape la note3"))
sum= (note1 + note2 +note3)/3
print (sum)

if sum <=20 and sum >=15:
    print ("Très bon élève")
elif sum <15 and sum >=11:
    print("Bon élève")  
elif sum <=10 and sum >=8:
    print("Élève moyen")
elif sum <=7 and sum >=0:
    print("Élève devant faire des efforts")    



    