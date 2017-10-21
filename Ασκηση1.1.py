'''
Python Mini Project Ασκηση 1.1
'''

import math
import time

#Η εισαγωγή των δύο ακεραίων

x = int(input('Εισήγαγε τον πρώτο ακέραιο:\n'))
y = int(input('Εισήγαγε τον δεύτερο ακετραιο:\n'))

#Η εκτύπωση των ζητουμένων

print('Το πηλίκο της διαίρεσης x διά y:\n', '{:10d}'.format(x//y))

print('Το υπόλοιπο της διαίρεσης x διά y:\n', '{:10d}'.format(x%y))

print('Ο λογάριθμος με βάση y του x:\n', '{:10.5f}'.format(math.log(x, y)))
	
print('Η τετραγωνική ρίζα του x:\n', '{:10.5f}'.format(math.sqrt(x)))

print('H εκθετική ποσότητα e εις την x:\n', '{:10.5f}'.format(math.exp(x)))

time.sleep(5)
