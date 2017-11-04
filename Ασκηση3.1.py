'''
Python Mini Project Ασκηση 3.1
'''
import random as rn
import time
N = int(input("Εισηγαγε το πληθος των ψευδοτυχαίων αριθμών στη λιστα:"))
L = [rn.randint(1,100) for i in range(N)]
temp=None

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if L[j+1]<L[j]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
print("Ορίστε η ταξινομημένη λίστα με", N, "τυχαίους αριθμούς απο το 1 μεχρι το 100:\n", L)
            
time.sleep(10)