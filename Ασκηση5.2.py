'''
Python Mini Project Ασκηση 5.2
'''
import time

def myrange(N, logos):
    x=1
    i=0
    while(i<N):
        yield x
        x=x*logos
        i+=1

for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)


time.sleep(10)
