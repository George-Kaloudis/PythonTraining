'''
Python Mini Project Ασκηση 5.1
'''
import time, math, random as rn

def stats(l):
    s1=0
    s2=0
    m=0
    sd=0
    for number in l:
        s1+=number
    m=s1/len(l)

    for number in l:
        s2+=(number-m)**2
    sd=math.sqrt((1/(len(l)-1))*s2)
    return sd,m


N=0
L=[]

N=int(input("Πλήθος ακεραίων στην λίστα:"))
L=[rn.randint(1,20) for i in range(N)]
SD,M = stats(L)

print("Λιστα:",L)

print("Μέσος όρος = ",'{:.2f}'.format(M),",Τυπική απόκλιση = ",'{:.2f}'.format(SD))
time.sleep(10)
