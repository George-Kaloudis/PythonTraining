'''
Python Mini Project Ασκηση 2.2
'''

import random as rn
import time
while True:
    num=rn.randint(0,36)
    print("-"*12)
    if num==0:
        print("Κληρώθηκε το 0")
    else:
        print("Ο αριθμός είναι ο:", num)
        if num<=17:
            print("Μικρός")    
        else:
            print("Μεγάλος")
            
        if ((num in range(1,11) or num in range(19,29)) and num%2==1) or ((num in range(11,19) or num in range(29,37)) and num%2==0):
            print("Κόκκινος")    
        else:
            print("Μαύρος")
            
        if num%2==0:
            print("Ζυγός")    
        else:
            print("Μονός")
    print("-"*12)
    action=input("Enter: Επόμενη Κλήρωση,      ‘q’+Enter: Τερματισμός:")
    if action=="q":
        break
    elif action=="":
        continue
    else:
        print("Λάθος είσοδος. Συνέχιση κληρώσεων")
        continue
        

