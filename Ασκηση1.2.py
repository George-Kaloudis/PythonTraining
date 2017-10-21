'''
Python Mini Project Ασκηση 1.2
'''

import math
import time

R = 6372.8

#Η εισαγωγή των γεωγραφικών συντεταγμένων καθε σημείου

π1 = math.radians(float(input('Εισήγαγε το γεωγραφικό πλάτος του πρώτου σημείου:\n')))
μ1 = math.radians(float(input('Εισήγαγε το γεωγραφικό μήκος του πρώτου σημείου:\n')))

π2 = math.radians(float(input('Εισήγαγε το γεωγραφικό πλάτος του δεύτερου σημείου:\n')))
μ2 = math.radians(float(input('Εισήγαγε το γεωγραφικό μήκος του δεύτερου σημείου:\n')))

#Επεξεργασια των δεδομένων

Δπ = π2 - π1

Δμ = μ2 - μ1

α = (math.sin(Δπ/2)**2) + math.cos(π1)*math.cos(π2)*(math.sin(Δμ/2)**2)
c = 2*math.asin(math.sqrt(α))

d = R * c

print('Η αποσταση των δύο σημείων ειναι:', d, 'km')

time.sleep(5)