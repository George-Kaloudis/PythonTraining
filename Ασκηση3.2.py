'''
Python Mini Project Ασκηση 3.2
'''

inp=None
L=[]
while True:
    inp=input("Εισήγαγε Ακέραιο(με μηδενικο μπροστα αν θες να εισαχθει στν αρχη της λιστας)/r για να αφαιρεσεις ενα στιχειο απο το τελος(η΄απο την αρχή αν βαλεις 0 μπροστα)/q για να βγεις απο το πρόγραμμα:")
    if inp=="q":
        break
    elif inp[0]=="0" and len(inp)!=1:
        inp=inp[1:]
        if inp=="r" and len(L)!=0:
            L.pop(0)
        elif inp=="r" and len(L)==0:
            print("Η λίστα δεν έχει στοιχεία οπότε δεν μπορείς να αφαιρέσεις κάποιο.\n")
            continue
        else:
            L.insert(0,int(inp))
    else:
        if inp=="r" and len(L)!=0:
            L.pop()
        elif inp=="r" and len(L)==0:
            print("Η λίστα δεν έχει στοιχεία οπότε δεν μπορείς να αφαιρέσεις κάποιο.\n")
            continue
        else:
            L.append(int(inp))

    print(L)
        
        
    
